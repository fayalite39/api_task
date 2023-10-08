import argparse
from logging import error
from os import getenv
import requests


def fetch_credentials():
    api_key = getenv("API_KEY")
    if not api_key:
        error("Failed to fetch API key from the environment.")
        return exit(1)
    return api_key


def validate_ip(ip_address: str) -> bool:
    """
    Verifies that the IP address provided is valid.
    A valid IP address has the form a.b.c.d, where a-d are numbers in the
    range 0-255. The numbers cannot have leading zeroes.
    """
    try:
        octet_list = ip_address.split(".")
        assert len(octet_list) == 4
        for octet in octet_list:
            assert octet.isnumeric()
            if len(octet) > 1:
                # no leading 0 allowed
                assert octet[0] != "0"
            assert int(octet) in range (256)
        return True
    except AssertionError:
        error("Invalid IP address provided.")
        return False
            

def make_api_call(ip_address):
    if not validate_ip(ip_address):
        return exit(1)
    api_key = fetch_credentials()
    if not api_key:
        return exit(1)
    ipstack_request = "http://api.ipstack.com/" + ip_address \
        + "?access_key=" + api_key
    try:
        response = requests.get(ipstack_request).json()
    except:
        error("Network error.")
        return exit(1)
    if response.get("success") == False:
        print(response["error"]["info"])
        return exit(1)
    return response


def get_lat_long(ip_address):
    response = make_api_call(ip_address)
    if not response:
        return exit(1)
    latitude = response.get("latitude")
    longitude = response.get("longitude")
    print(f"{latitude}, {longitude}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ip_address")
    args = parser.parse_args()
    get_lat_long(args.ip_address)