import argparse
from os import getenv
import requests


def fetch_credentials():
    api_key = getenv("API_KEY")
    return api_key


def make_api_call(ip_address):
    api_key = fetch_credentials()
    if not api_key:
        return exit(1)
    ipstack_request = "http://api.ipstack.com/" + ip_address \
        + "?access_key=" + api_key
    response = requests.get(ipstack_request)
    return response.json()


def get_lat_long(ip_address):
    response = make_api_call(ip_address)
    latitude = response.get("latitude")
    longitude = response.get("longitude")
    print(f"{latitude}, {longitude}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ip_address")
    args = parser.parse_args()
    get_lat_long(args.ip_address)