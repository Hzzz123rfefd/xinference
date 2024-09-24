## environment
```bash
# docker版本要求大于19.0
# 安装 NVIDIA 容器工具包
sudo yum clean all
sudo yum makecache fast
sudo yum install -y nvidia-container-toolkit
# 配置 Docker 使用 NVIDIA 运行时
sudo tee /etc/docker/daemon.json <<EOF
{
    "default-runtime": "nvidia",
    "runtimes": {
        "nvidia": {
            "path": "nvidia-container-runtime",
            "runtimeArgs": []
        }
    }
}
EOF
# 重启
sudo systemctl restart docker
```

## pull base image
```bash
docker pull registry.cn-hangzhou.aliyuncs.com/xprobe_xinference/xinference:latest
```

## deploy xinference service by docker 
* 1、authority settiing
refer to docker/authority.json
* 2、xinference_path
model cache path,refer to run.sh
* 3、finetune_model_path
finetine model cache path,refer to run.sh
* 4、port
port on the post 
```bash
cd docker
sh -x run.sh
```

