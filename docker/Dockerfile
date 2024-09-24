FROM registry.cn-hangzhou.aliyuncs.com/xprobe_xinference/xinference:latest
COPY authority.json authority.json
CMD ["xinference-local", "-H", "0.0.0.0", "--auth-config", "authority.json"]