import asyncio
from kasa import SmartPlug  # pip install python-kasa
from prefect import flow


@flow(log_prints=True, retries=3)
async def update_smart_plug_state(desired_state: bool):
    """Update the state of a smart plug to the desired state
    works with the tp-link ep10 on kasa app

    Args:
        desired_state (bool): The desired state of the smart plug. True for on, False for off.
    """

    p = SmartPlug(host="192.168.1.161")
    # Replace with the IP of your device
    # running kasa discover from the CLI gives you the IP and other details

    await p.update()
    print(f"Name of device: {p.alias}")

    if desired_state == True:
        try:
            await p.turn_on()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            await p.update()
            print(p.state_information)
    if desired_state == False:
        try:
            await p.turn_off()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            await p.update()
            print(p.state_information)


if __name__ == "__main__":
    # test flow
    # asyncio.run(update_smart_plug_state(True))

    # create deployment
    flow.from_source(
        source="https://github.com/discdiver/event-driven-workflows-course.git",
        entrypoint="module_7/toggle_smart_switch.py:update_smart_plug_state",
    ).deploy(name="update_smart_plug", work_pool_name="managed1")
