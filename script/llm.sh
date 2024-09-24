curl -X 'POST' \
  'http://<XINFERENCE_HOST>:<XINFERENCE_PORT>/v1/chat/completions' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "<MODEL_UID>",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "What is the largest animal?"
        }
    ],
    "max_tokens": 512,
    "temperature": 0.7
  }'