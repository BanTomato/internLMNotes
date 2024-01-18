import os

# 下载模型
# os.system('huggingface-cli download --resume-download internlm/internlm-chat-7b --local-dir E:\Github\llmmodel'  )

from huggingface_hub import hf_hub_download  # Load model directly

hf_hub_download(repo_id="internlm/internlm-7b", filename="config.json")