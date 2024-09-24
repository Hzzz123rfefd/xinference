# xinference
nlp model deploy
Official documents: https://inference.readthedocs.io/zh-cn/latest/
## Installation
Operating System: Linux
```bash
conda create -n xinfernece python=3.10
conda activate xinfernece
git clone https://github.com/Hzzz123rfefd/xinference.git
cd xinfernece
pip install -r requirements.txt
```
## Usage
### start xinfernece service
```bash
xinference-local --host 0.0.0.0 --port 9997 
```
If you need to set permissions, you can write the following permission JSON file:
```json
{
    "auth_config": {
        "algorithm": "HS256",
        "secret_key": "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7",
        "token_expire_in_minutes": 30
    },
    "user_config": [
        {
            "username": "user1",
            "password": "secret1",
            "permissions": [
                "admin"
            ],
            "api_keys": [
                "sk-72tkvudyGLPMi",
                "sk-ZOTLIY4gt9w11"
            ]
        },
        {
            "username": "user2",
            "password": "secret2",
            "permissions": [
                "models:list",
                "models:read"
            ],
            "api_keys": [
                "sk-35tkasdyGLYMy",
                "sk-ALTbgl6ut981w"
            ]
        }
    ]
}
```
目前，Xinference 内部定义了以下几个接口权限：

*   models\:list: 获取模型列表和信息的权限。
*   mmodels\:read: 使用模型的权限。
*   mmodels\:register: 注册模型的权限。
*   mmodels\:unregister: 取消注册模型的权限。
*   mmodels\:start: 启动模型的权限。
*   mmodels\:stop: 停止模型的权限。
*   madmin: 管理员拥有所有接口的权限。
then you can strart xinference service:
```bash
xinference-local --host 0.0.0.0 --port 9997 --auth-config /path/to/your_json_config_file
```
### deploy model
now you can deploy your model,there are three deployment methods for mdoels
#### Deploy in browser interface
This is the simplest and most intuitive way to deploy the model, just enter it in the browser http://ip:port Ready to access deployment
#### Deploy on the terminal
* rerank model
```bash
xinference launch --model-name bge-reranker-base --model-type rerank
```
#### Deploy with code 
TODO:

### Call model
now you can call your model by two ways
#### Call on the terminal
* rerank model 
```bash
sh -x script/rerank.sh
```
* llm model
```bash
sh -x script/llm.sh
```

#### Call with code
* rerank model 
```bash
python client_rerank.py
```
* llm model
```bash
sh -x script/llm.sh
```
### Model cache path
#### models from huggingface
```bash
cd ~/.cache/huggingface/hub
```
#### models from modelscope
```bash
cd ~/.cache/modelscope/hub
```
#### xinference cache path
```bash
cd ~/.xinference/cache/
```
请注意xinference cache path中不保存真正的模型，只是软连接，如果模型从huggingface下载，则软连接到~/.cache/huggingface/hub里的，如果模型从modelscope下载，则软连接到~/.cache/modelscope/hub里的，