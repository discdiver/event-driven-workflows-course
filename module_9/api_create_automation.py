import os
import httpx


PREFECT_API_URL = "https://api.prefect.cloud/api/accounts/9b649228-0419-40e1-9e0d-44954b5c0ab6/workspaces/d137367a-5055-44ff-b91c-6f7366c9e4c4"
# replace account and workspace ids
PREFECT_API_KEY = os.environ.get("PREFECT_API_KEY_EVENT_COURSE")

data = {
    "name": "Run deployment to sell stock when a flow runs!",
    "description": "",
    "enabled": True,
    "trigger": {
        "match": {},
        "match_related": {
            "prefect.resource.id": "prefect.flow.5c933ae4-dd43-4705-90eb-cfdeb4c028fb"
        },
        "after": [],
        "expect": ["prefect.flow-run.Completed"],
        "for_each": [],
        "posture": "Reactive",
        "threshold": 1,
        "within": 0.0,
        "metric": None,
    },
    "actions": [
        {
            "type": "run-deployment",
            "source": "selected",
            "deployment_id": "706abffa-7590-4a68-9258-79c2f8c7ef7a",
            "parameters": None,
        }
    ],
    "actions_on_trigger": [],
    "actions_on_resolve": [],
}

headers = {"Authorization": f"Bearer {PREFECT_API_KEY}"}
endpoint = f"{PREFECT_API_URL}/automations/"


def create_automation(
    endpoint: str = endpoint, headers: dict = headers, data: dict = data
):
    response = httpx.post(endpoint, headers=headers, json=data)

    print(response.json())


if __name__ == "__main__":
    create_automation()
