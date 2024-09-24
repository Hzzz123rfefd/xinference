# image name
image_name="xinference:20240830"

# path of .xinference
xinference_path="/data2/xinference"
finetune_model_path="/data2/xiaohui/work/datagpt/saved_model"
port=9996

# create image
sudo docker build --network=host -t ${image_name} .

# create contain
sudo docker run -idt \
    --restart=always \
    -v ${xinference_path}/.xinference:/root/.xinference \
    -v ${xinference_path}/.cache/huggingface:/root/.cache/huggingface \
    -v ${finetune_model_path}:/root/.cache/finetune_model \
    -p ${port}:9997 \
    --gpus all \
    --name xinference \
    ${image_name}
