from prefect import flow


@flow(log_prints=True)
def print_issue(issue_number: str, issue_text: str, user_login_name: str) -> None:
    print(f"Issue #{issue_number} from {user_login_name} reads: {issue_text}")
    print("Now go do other things with this information (summarize, respond, etc)")


if __name__ == "__main__":
    print_issue.from_source(
        source="https://github.com/discdiver/event-driven.git",
        entrypoint="flow.py:print_issue",
    ).deploy(name="gh-issue-deploy", work_pool_name="prefect-managed")
