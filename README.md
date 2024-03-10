# Gecko Listing Notifier

## Overview

The Gecko Listing Notifier is a Python script designed to monitor CoinGecko for new cryptocurrency listings. When the script detects a new listing, it alerts the user with a beep sound. This tool is perfect for cryptocurrency enthusiasts and investors looking to stay informed about the latest market additions.

## Features

- **Automatic Monitoring**: Periodically checks CoinGecko for new cryptocurrency listings.
- **Notification**: Alerts users with a beep sound when new listings are detected.
- **Change Detection**: Saves cryptocurrency listings only when changes are detected, minimizing unnecessary data storage.
- **Logging**: Provides detailed logs for monitoring script activity and troubleshooting.

## Prerequisites

Before you start, ensure you have the following installed:
- Python 3.6 or newer
- `requests` library

Python can be downloaded from the [official website](https://www.python.org/downloads/), and the `requests` library can be installed using pip:

```bash
pip install requests
```

## Installation

1. Clone the repository or download the source code to your local machine:

```bash
git clone https://github.com/johnthotekat/gecko_monitor.git
cd cryptocurrency-listing-notifier
```

2. No additional setup is required. The script uses Python's standard libraries, along with `requests` for API calls.

## Usage

To run the script, navigate to the project directory and execute:

```bash
python crypto_checker.py
```

Keep the script running to continuously monitor for new cryptocurrency listings. Ensure your system's sound is on to hear the beep notifications for new listings.

## How It Works

The script operates by performing the following steps:
- Fetches the current list of cryptocurrencies from CoinGecko.
- Compares this list with the previously fetched list, stored locally.
- If new listings are detected, the script emits a beep sound and logs the details of the new listings.
- The list of cryptocurrencies is saved with a timestamp if changes are detected, and the latest list is saved for future comparison.

## Monitoring and Logs

The script logs its operations, providing insights into its activity:
- When checks are performed and their results.
- Details of new cryptocurrency listings when found.
- Any errors or issues encountered during execution.

Logs are printed to the console and can be redirected to a file for permanent storage if needed.

## Customization

You can customize the script by modifying the source code. Some potential customizations include:
- Changing the API polling interval (default is every 5 minutes).
- Modifying the beep sound or notification method for non-Windows platforms.
- Adjusting the logging level or format for more or less detailed output.

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request with your improvements.
