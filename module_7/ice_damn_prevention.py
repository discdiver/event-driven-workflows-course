import httpx
from prefect import flow, task
from prefect.events import emit_event


@task(retries=3)
def get_weather_forecast(lat: float, lon: float) -> float:
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
def snow_forecast(lat: float = 38.9, lon: float = -77.0, min_cm=1):

    response = get_weather_forecast(lat, lon)
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


if __name__ == "__main__":
    snow_forecast().from_source().deploy(name="ice_damn_forecast", workpool="managed1")
