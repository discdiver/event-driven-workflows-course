from prefect import flow


if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/discdiver/event-driven-workflows-course.git",
        entrypoint="module_2/project_solution_recommend.py:recommend_shares",
    ).deploy(
        name="recommend-deployment",
        work_pool_name="managed2",
    )
