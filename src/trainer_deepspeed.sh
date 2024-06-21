# Does not include prediction/generation, need to figure out evals for it

MODEL_NAME=$1 #t5-large/ google/flan-t5-large like  /home/woojeong2/Decoding/LLaMA2-7B
current_time=$(date +'%m%d%Y_%H_%M_%S')

outputs="${MODEL_NAME}_${current_time}"

deepspeed \
    --include=localhost:0,1,2,3,4,5,6,7 \
    --master_port 62650 \
    run_classification.py \
    --deepspeed ds_config.json \
    --model_name_or_path "${MODEL_NAME}" \
    --token "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" \
    --do_train \
    --do_eval \
    --train_file "../final_flan_data/train.csv" \
    --validation_file "../final_flan_data/eval.csv" \
    --text_column "Input.tweet1" \
    --summary_column "finer_updated" \
    --source_prefix "Classify the given tweet into one or more of the following 10 labels: government_critique,money_aid_resource_allocation,societal_critique,deserving_undeserving_of_resources,harmful_generalization,not_in_my_backyard,media_portrayal,personal_interaction_observation_of_homelessness,solutions_interventions,0. Tweet: " \
    --max_source_length 1024 \
    --max_target_length 100 \
    --num_train_epochs 5 \
    --output_dir "./outputs/${outputs}" \
    --per_device_train_batch_size=16 \
    --per_device_eval_batch_size=16 \
    --overwrite_output_dir \
    --predict_with_generate \
    --save_total_limit 1 \
    --load_best_model_at_end \
    --save_strategy "epoch" \
    --evaluation_strategy "epoch" \
    --gradient_checkpointing 1 \
    --overwrite_cache true \
    # --use_cache false \


#    --dataset_name homeless \
#    --max_train_samples 100 \
