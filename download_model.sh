model_dir=${HOME}/models
mkdir -p ${model_dir}

echo "model directory: $(pwd)"

model_id='deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B'

export HF_HUB_ENABLE_HF_TRANSFER=1 
export HF_ENDPOINT=https://hf-mirror.com

# download model
cd ${model_dir}
git clone git@hf.co:${model_id}

