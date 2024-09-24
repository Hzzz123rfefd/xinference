curl -X 'POST' \
  'http://114.67.101.49:4321/v1/rerank' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "bge-reranker-base",
    "query": "A man is eating pasta.",
    "documents": [
        "A man is eating food.",
        "A man is eating a piece of bread.",
        "The girl is carrying a baby.",
        "A man is riding a horse.",
        "A woman is playing violin."
    ]
  }'

