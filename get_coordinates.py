import argparse
import requests


def make_api_call(ip_address):
    api_key = "SOME_NUM"
    ipstack_request = "http://api.ipstack.com/" + ip_address \
        + "?access_key=" + api_key
    response = requests.get(ipstack_request)
    print(response.json())
    return response.json()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ip_address")
    args = parser.parse_args()
    make_api_call(args.ip_address)