import os
import httpx


PREFECT_API_URL = "https://api.prefect.cloud/api/accounts/9b649228-0419-40e1-9e0d-44954b5c0ab6/workspaces/d137367a-5055-44ff-b91c-6f7366c9e4c4"
# replace account and workspace ids
PREFECT_API_KEY = os.environ.get("PREFECT_API_KEY_EVENT_COURSE")

data = {"sort": "NAME_ASC"}
headers = {"Authorization": f"Bearer {PREFECT_API_KEY}"}
endpoint = f"{PREFECT_API_URL}/automations/filter"


def call_prefect_api(
    endpoint: str = endpoint, headers: dict = headers, data: dict = data
):
    response = httpx.post(endpoint, headers=headers, json=data)

    print(f"# of automations: {len(response.json())}")

    for automation in response.json():
        print(automation)


if __name__ == "__main__":
    call_prefect_api()
