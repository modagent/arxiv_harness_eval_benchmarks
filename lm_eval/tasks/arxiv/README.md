## Dataset Modality
```
lm_eval --model hf \
    --model_args pretrained=gpt2 \
    --tasks dataset_modality \
    --device cpu \
    --log_samples \
    --limit 10 \
    --output_path output/output6.jsonl
```


## Model Modality
```
lm_eval --model hf \
    --model_args pretrained=gpt2 \
    --tasks model_modality \
    --device cpu \
    --log_samples \
    --limit 10 \
    --output_path output/output7.jsonl
```