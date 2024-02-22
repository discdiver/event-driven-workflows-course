import os
import requests


PREFECT_API_URL = "https://api.prefect.cloud/api/me/"  # "https://api.prefect.cloud/api/accounts/9b649228-0419-40e1-9e0d-44954b5c0ab6/workspace/d137367a-5055-44ff-b91c-6f7366c9e4c4"

# replace account and workspace ids
PREFECT_API_KEY = os.environ.get("PREFECT_API_KEY_EVENT_COURSE")

# data = {"sort": "CREATED_DESC", "limit": 5, "artifacts": {"key": {"exists_": True}}}

headers = {"Authorization": f"Bearer {PREFECT_API_KEY}"}
endpoint = f"{PREFECT_API_URL}"

response = requests.get(endpoint, headers=headers)  # , json=data)
print(response)

assert response.status_code == 200

# for artifact in response.json():
#     print(artifact)
