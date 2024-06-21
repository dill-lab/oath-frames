SAVE_PATH=$1
# TEST_FILE=$2
MODEL_NAME="google/flan-t5-xl" #t5-large like
current_time=$(date +'%m%d%Y_%H_%M_%S')

deepspeed \
    --include=localhost:0,1,2,3 \
    --master_port 61000 \
    --deepspeed ds_config.json \
    evaluate_classification.py \
    --model_name_or_path "${MODEL_NAME}" \
    --token "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" \
    --do_predict \
    --test_file "../final_flan_data/test.csv" \
    --resume_from_checkpoint "./outputs/${SAVE_PATH}/" \
    --output_dir "./outputs/${SAVE_PATH}/" \
    --text_column "Input.tweet1" \
    --summary_column "finer_updated" \
    --source_prefix "Classify the given tweet into one or more of the following 10 labels: government_critique,money_aid_resource_allocation,societal_critique,deserving_undeserving_of_resources,harmful_generalization,not_in_my_backyard,media_portrayal,personal_interaction_observation_of_homelessness,solutions_interventions,0. Tweet: " \
    --max_source_length 1024 \
    --max_target_length 100 \
    --output_dir "./outputs/${SAVE_PATH}/" \
    --per_device_eval_batch_size=1 \
    --overwrite_output_dir \
    --predict_with_generate \
    --gradient_checkpointing 1 \
    --overwrite_cache true \
