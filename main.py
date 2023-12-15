import requests

USERNAME = "cptptag"
TOKEN = "jfpo153j67li457li4"

pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": "jfpo153j67li457li4",
    "username": "cptptag",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


graph_parameters = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Mi",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
print(response.text)