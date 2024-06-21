"""
Usage:
python3 -m fastchat.serve.huggingface_api --model lmsys/vicuna-7b-v1.5
python3 -m fastchat.serve.huggingface_api --model lmsys/fastchat-t5-3b-v1.0
"""
import argparse
import pickle
import torch
import pandas as pd
from fastchat.model import load_model, get_conversation_template, add_model_args
from huggingface_hub import login

login("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")

def load_text_from_file(file_name):
    my_prompt = "Classify the given tweet into one or more of the following 10 labels and the output should be a comma separated list of labels with nothing else: government_critique,money_aid_resource_allocation,societal_critique,deserving_undeserving_of_resources,harmful_generalization,not_in_my_backyard,media_portrayal,personal_interaction_observation_of_homelessness,solutions_interventions,filtered_out. Tweet: " 

    ip_texts = []
    if file_name.endswith(".txt"): # BRIHI
        with open(file_name, "r") as f:
            ip_texts = [my_prompt + line.rstrip("\n") for line in f]
    if file_name.endswith(".pkl"):
        with open(file_name, "rb") as f:
            ip_text = pickle.load(f)
            ip_texts = [my_prompt + line.rstrip("\n") for line in ip_text]
    if file_name.endswith(".csv"):
        ip_text = pd.read_csv(file_name)
        tweets = ip_text['Input.tweet1'].tolist()
        ip_texts = [my_prompt + line.rstrip("\n") for line in tweets]
    for i in range(5):
        print(ip_texts[i])
    return ip_texts

@torch.inference_mode()
def main(args):
    print("GPUS: ", args.num_gpus)
    print("DEVICE: ", args.device)
    # Load model
    model, tokenizer = load_model(
        args.model_path,
        device=args.device,
        num_gpus=args.num_gpus,
        max_gpu_memory=args.max_gpu_memory,
        load_8bit=args.load_8bit,
        cpu_offloading=args.cpu_offloading,
        revision=args.revision,
        debug=args.debug,
    )

    # get inputs
    text_inputs = load_text_from_file(args.file)

    # Build the prompt with a conversation template
    all_prompts = []
    for i in range(len(text_inputs)):
        msg = text_inputs[i]
        conv = get_conversation_template(args.model_path)
        conv.append_message(conv.roles[0], msg)
        conv.append_message(conv.roles[1], None)
        prompt = conv.get_prompt()
        all_prompts.append(prompt)
    print("Created all prompts!", len(all_prompts))


    # Run inference
    msg_and_output = {}
    for i in range(len(text_inputs)):
        if i%1==0: print(i)
        ct_msg = text_inputs[i]#.split("User: ")[1]
        ct_prompt = all_prompts[i]
        inputs = tokenizer([ct_prompt], return_tensors="pt").to(args.device)

        output_ids = model.generate(
            **inputs,
            do_sample=True if args.temperature > 1e-5 else False,
            temperature=args.temperature,
            repetition_penalty=args.repetition_penalty,
            max_new_tokens=args.max_new_tokens,
        )

        if model.config.is_encoder_decoder:
            output_ids = output_ids[0]
        else:
            output_ids = output_ids[0][len(inputs["input_ids"][0]) :]
        outputs = tokenizer.decode(
            output_ids, skip_special_tokens=True, spaces_between_special_tokens=False
        )
        msg_and_output[ct_msg] = outputs
        print(outputs, "\n\n")

        # Print results # old
        # print(f"{conv.roles[0]}: {msg}")
        # print(f"{conv.roles[1]}: {outputs}")

    with open("jaspreet_llama.pkl", "wb") as fw:
        pickle.dump(msg_and_output, fw)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    add_model_args(parser)
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--repetition_penalty", type=float, default=1.0)
    parser.add_argument("--max-new-tokens", type=int, default=1024)
    parser.add_argument("--debug", action="store_true")
    parser.add_argument("--file", type=str, required=True)
    args = parser.parse_args()

    # Reset default repetition penalty for T5 models.
    if "t5" in args.model_path and args.repetition_penalty == 1.0:
        args.repetition_penalty = 1.2

    main(args)