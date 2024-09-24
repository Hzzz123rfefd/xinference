from xinference.client import Client


url = ""                  # your url
# authority if need
user = ""
password = ""
api_key = ""

# create client,api_key is option
client = Client(url,api_key=api_key)
model = client.get_model("mistral-instruct-v0.3")

# Chat to LLM
answer = model.chat(
   messages=    [
       {"content": "You are a helpful assistant.", "role": "user"}
    ],
   generate_config={"max_tokens": 1024}
)
print(answer)
