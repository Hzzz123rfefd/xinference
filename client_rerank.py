# 测试代码连接
import socket
import requests
from xinference.client import Client


def check_url_reachability(url, timeout=1):
    try:
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.Timeout:
        return False
    except requests.exceptions.RequestException as e:
        return False

url = ""                  # your url

# authority if need
user = ""
password = ""
api_key = ""

# create client,api_key is option   
if(check_url_reachability(url, timeout = 1) == True):
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
else:
    print("can not connect to:",url)

