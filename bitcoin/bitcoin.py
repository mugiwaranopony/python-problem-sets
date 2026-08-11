import os
import sys

import requests


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    api_key = os.getenv("COINCAP_API_KEY")

    if not api_key:
        sys.exit("Missing CoinCap API key")

    url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        price = float(response.json()["data"]["priceUsd"])
    except (requests.RequestException, KeyError, ValueError):
        sys.exit("Unable to retrieve Bitcoin price")

    total = bitcoins * price
    print(f"${total:,.4f}")


if __name__ == "__main__":
    main()