import httpx
from prefect import flow, task
from prefect.events import emit_event


@task(retries=3)
def get_forecast(lat: float, lon: float) -> float:
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": ["temperature_2m", "snowfall"],  # or use current: for current weather
        "forecast_days": 1,  # default is 7
    }
    expected_weather = httpx.get(base_url, params=params)
    return expected_weather


@flow(log_prints=True)
def check_weather(lat: float = 38.9, lon: float = -77.0, min_cm=1):

    response = get_forecast(lat, lon)
    data = response.json()["hourly"]
    expected_temp_c = float(data["temperature_2m"][0])  # predicted temp
    expected_snow_cm = float(data["snowfall"][0])  # predicted snowfall

    desired_coil_state = None  # keep current state
    if expected_snow_cm >= min_cm and expected_temp_c < 0:
        # Turn on the heater coil
        desired_coil_state = "on"
    elif expected_temp_c > 0:
        # Turn off the heater coil
        desired_coil_state = "off"
        # Emit an event to share the desired state of the heater coil
    if desired_coil_state:
        emit_event(
            event="coil.state.desired",
            resource={"prefect.resource.id": "heater coil state"},
            payload={"desired_state": f"{desired_coil_state}"},
        )

    with open("weather.csv", "w+") as w:
        w.write(str(expected_temp_c))

    # read the file
    with open("weather.csv", "r") as r:
        print(r.read())


if __name__ == "__main__":
    # check_weather()

    # create deployment
    flow.from_source(
        source="https://github.com/discdiver/event-driven-workflows-course.git",
        entrypoint="module_7/ice_damn_prevention.py:check_weather",
    ).deploy(name="ice_damn_forecast", work_pool_name="managed1")
