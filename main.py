import requests
from datetime import  datetime

USERNAME = "cptptag"
TOKEN = "jfpo153j67li457li4"

pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": "jfpo153j67li457li4",
    "username": "cptptag",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
#POST new profile
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
#POST graph
# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)
today = datetime.now()
today_formatted = today.strftime("%Y%m%d")

pixel_post = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_parameters["id"]}"
pixel_update = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_parameters["id"]}/{today_formatted}"
pixel_delete = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_parameters["id"]}/{today_formatted}"

pixel_parameters = {
    "date": today_formatted,
    "quantity": "20"
}
# #POST pixel
response = requests.post(url=pixel_post, json=pixel_parameters, headers=headers)
print(response.text)

pixel_put_params = {
    "quantity": "15"
}

# #PUT Pixel
# response = requests.put(url=pixel_update, json=pixel_put_params, headers=headers)
# print(response.text)

# #DELETE Pixel
# response = requests.delete(url=pixel_delete, headers=headers)
# print(response.text)