# 测试代码连接

from xinference.client import Client

url = ""                  # your url
# authority if need
user = ""
password = ""
api_key = ""

# create client,api_key is option
client = Client(url,api_key=api_key)

# login if need
# client.login(user, password)

# launch_model if need
# model_uid = client.launch_model(model_name="bge-reranker-base", model_type="rerank")

# get model through id
model = client.get_model("bge-reranker-base")
# model = client.get_model("bge-reranker-base")

# use model
query =  "A man is eating pasta."
corpus = [
    "A man is eating food.",
    "A man is eating a piece of bread.",
    "The girl is carrying a baby.",
    "A man is riding a horse.",
    "A woman is playing violin."
]

# print result
print(model.rerank(corpus, query))

