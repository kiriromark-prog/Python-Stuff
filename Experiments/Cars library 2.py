import requests
import sys


CAR_MODEL = "Land cruiser"  
API_KEY = "insert API key" 

# 2. API ENDPOINT
API_URL = "https://api.api-ninjas.com/v1/cars"


def get_car(model_name):
    headers = {"X-Api-Key": API_KEY}
    params = {"model": model_name}

    try:
        resp = requests.get(API_URL, headers=headers, params=params, timeout=10)
    except requests.RequestException as e:
        raise SystemExit(f"Network error: {e}")

    if resp.status_code != 200:
        raise SystemExit(f"Failed to fetch car `{model_name}` (status {resp.status_code}). Server says:\n{resp.text}")

    if "application/json" not in resp.headers.get("Content-Type", ""):
        raise SystemExit(f"Expected JSON, but got something else. Server raw response:\n{resp.text}")

    try:
        data = resp.json()
    except requests.exceptions.JSONDecodeError:
        raise SystemExit(f"Could not decode JSON. Raw response was:\n{resp.text}")

    if not data:
        raise SystemExit(f"No car data found for model: `{model_name}`")

    car_data = data[0]
    
    result = {
        "make": car_data.get("make"),
        "model": car_data.get("model"),
        "year": car_data.get("year"),
        "class": car_data.get("class"),
        "transmission": "Automatic" if car_data.get("transmission") == "a" else "Manual",
        "specs": {
            "Engine Cylinders": car_data.get("cylinders"),
            "Displacement (L)": car_data.get("displacement"),
            "Fuel Type": car_data.get("fuel_type"),
            "City MPG": car_data.get("city_mpg"),
            "Highway MPG": car_data.get("highway_mpg"),
            "Drive Type": car_data.get("drive"),
        }
    }
    return result


def main():

    info = get_car(CAR_MODEL)

    print(f"Make: {info['make'].title()}")
    print(f"Model: {info['model'].title()}")
    print(f"Year: {info['year']}")
    print(f"Class: {info['class']}")
    print(f"Transmission: {info['transmission']}")
    print("Specifications:")
    for spec, val in info['specs'].items():
        print(f"  - {spec}: {val}")


if __name__ == "__main__":
    main()
