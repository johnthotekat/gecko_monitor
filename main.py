import os
import tempfile

import requests
import time
import json
import datetime
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Cross-platform beep setup
try:
    import winsound


    def beep():
        winsound.Beep(440, 1000)

except ImportError:
    def beep():
        print("\a")


def fetch_coins_list():
    url = "https://api.coingecko.com/api/v3/coins/list"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises a HTTPError if the response code was unsuccessful
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch coins list: {e}")
        return None


def save_coins_list(coins, filename="coins_list.json"):
    try:
        with open(filename, 'w') as file:
            json.dump(coins, file)
        logging.info(f"Saved {len(coins)} coins to {filename}")
    except Exception as e:
        logging.error(f"Failed to save coins list: {e}")


def load_previous_coins_list(filename="previous_coins_list.json"):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.info("Previous coins list not found. Assuming first run.")
        return []
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON from {filename}: {e}")
        return []


def compare_and_alert_new_coins(current_coins, previous_coins):
    current_coins_set = set(coin['id'] for coin in current_coins)
    previous_coins_set = set(coin['id'] for coin in previous_coins)
    new_coins_set = current_coins_set - previous_coins_set

    if new_coins_set:
        logging.info("New crypto(s) added:")
        for new_coin_id in new_coins_set:
            new_coin_details = next((coin for coin in current_coins if coin['id'] == new_coin_id), None)
            if new_coin_details:
                logging.info(
                    f"ID: {new_coin_details['id']}, Symbol: {new_coin_details['symbol']}, Name: {new_coin_details['name']}")
        beep()
    else:
        logging.info("No new cryptos added since the last check.")


def main():
    while True:
        current_coins = fetch_coins_list()
        if current_coins is not None:
            # Load the previous list of coins to compare
            previous_coins = load_previous_coins_list()

            # Convert both lists to sets for easy comparison
            current_coins_set = set(json.dumps(coin, sort_keys=True) for coin in current_coins)
            previous_coins_set = set(json.dumps(coin, sort_keys=True) for coin in previous_coins)

            # Compare the current and previous sets
            if current_coins_set != previous_coins_set:
                # Only if there is a change, save the current list as the new 'previous' list
                timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                save_coins_list(current_coins, f"coins_list_{timestamp}.json")
                save_coins_list(current_coins, "previous_coins_list.json")
                logging.info("Cryptocurrency list updated with new changes.")
            else:
                logging.info("No changes detected in the cryptocurrency list.")

            # Regardless of changes, check and alert for new coins
            compare_and_alert_new_coins(current_coins, previous_coins)

        # Adjust the sleep time as necessary to respect API rate limits
        logging.info("Waiting before the next check...")
        time.sleep(100)  # Wait time due to api rate limits,  you can implement much more intelligent stuff, I'm just writing this quick coz I needed the code ready in like 20 minutes. 


if __name__ == "__main__":
    main()
