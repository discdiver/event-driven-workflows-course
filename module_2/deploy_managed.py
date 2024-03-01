from prefect import flow


if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/discdiver/event-driven-workflows-course.git",
        entrypoint="module_2/weather2_tasks.py:pipeline",
    ).deploy(
        name="fetch-temp",
        work_pool_name="managed1",
    )
