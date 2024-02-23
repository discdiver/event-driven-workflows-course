import os
import httpx


PREFECT_API_URL = "https://api.prefect.cloud/api/accounts/9b649228-0419-40e1-9e0d-44954b5c0ab6/workspaces/d137367a-5055-44ff-b91c-6f7366c9e4c4"
# replace account and workspace ids
PREFECT_API_KEY = os.environ.get("PREFECT_API_KEY_EVENT_COURSE")

id = "8711bdb9-bf23-48a2-bf3e-2ceb096d68ea"
# replace with the id of the automation to delete
# could get the id from the response of the create_automation function
# or from the URL in the UI

headers = {"Authorization": f"Bearer {PREFECT_API_KEY}"}
endpoint = f"{PREFECT_API_URL}/automations/{id}"


def delete_automation(endpoint: str = endpoint, headers: dict = headers):
    response = httpx.delete(endpoint, headers=headers)
    print(response)


if __name__ == "__main__":
    delete_automation()
