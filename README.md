## Introduction
The get_coordinates.py script accepts an IP address in the command line and checks its validity. If the IP address is valid (in the format a.b.c.d, with a-d being numbers in the range 0-255 without leading zeros), the script queries the IPstack API and prints the latitude and longitude of the IP address.

## Requirements
The script utilises the requests library. This is listed in the requirements.txt file and can be installed with:

    pip install -r requirements.txt


Use of the IPstack API requires an API key. The script retrieves API_KEY from the environment - to use the script, it is necessary to add a valid API_KEY to the environment variables:

    export API_KEY=your_api_key


## Using the script
After setup, the script can be run from the command line:

    python3 get_coordinates.py 134.201.250.155

Without additional flags, this will print the following:

    34.0655517578125, -118.24053955078125

The optional flag '-f' or '-full' can be added for more complete information about the input and output values:

    python3 get_coordinates.py 134.201.250.155 --full

Full output:

    IP address: 134.201.250.155
    latitude: 34.0655517578125
    longitude: -118.24053955078125

