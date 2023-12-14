import requests

print(requests.get('http://localhost:8000').json()) # fazendo uma requisição na api
print(requests.get('http://localhost:8000/items/4').json())
print(requests.get('http://localhost:8000/items/2/?q=detalhe').json())