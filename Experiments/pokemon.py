import argparse
import requests
import sys

BASE_URL = "https://pokeapi.co/api/v2"


def get_pokemon(name_or_id):
    url = f"{BASE_URL}/pokemon/{name_or_id}"
    try:
        resp = requests.get(url, timeout=10)
    except requests.RequestException as e:
        raise SystemExit(f"Network error: {e}")

    if resp.status_code != 200:
        raise SystemExit(f"Failed to fetch Pokemon `{name_or_id}` (status {resp.status_code})")

    data = resp.json()
    result = {
        "name": data.get("name"),
        "id": data.get("id"),
        "height": data.get("height"),
        "weight": data.get("weight"),
        "types": [t["type"]["name"] for t in data.get("types", [])],
        "abilities": [a["ability"]["name"] for a in data.get("abilities", [])],
        "stats": {s["stat"]["name"]: s.get("base_stat") for s in data.get("stats", [])},
    }
    return result


def main(argv=None):
    p = argparse.ArgumentParser(description="Fetch Pokémon info from PokeAPI")
    p.add_argument("name", nargs="?", default="pikachu", help="Pokémon name or id")
    args = p.parse_args(argv)

    info = get_pokemon(args.name)

    print(f"Name: {info['name']}")
    print(f"ID: {info['id']}")
    print(f"Height: {info['height']}")
    print(f"Weight: {info['weight']}")
    print(f"Types: {', '.join(info['types']) or 'N/A'}")
    print(f"Abilities: {', '.join(info['abilities']) or 'N/A'}")
    print("Stats:")
    for stat, val in info['stats'].items():
        print(f"  - {stat}: {val}")


if __name__ == "__main__":
    main()
