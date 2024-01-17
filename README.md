Website Monitor Documentation
Introduction

The "Website Monitor" is a Python script that allows you to monitor the availability and performance of a website. It sends an HTTP GET request to the specified URL and measures the response time. If the website is down or its response time exceeds a defined limit, the script provides alerts and information about the website's status. This documentation provides an overview of the code structure, usage, and functionality of the Website Monitor script.
Getting Started

To use the Website Monitor script, follow these steps:

    Install the required Python libraries by running the following command:

    bash

pip install requests

Clone or download this repository to your local machine.

Open the Python script in your preferred code editor or integrated development environment (IDE).

Execute the script using the following command:

    python website_monitor.py

    Follow the prompts to enter the website URL you want to monitor and the response time limit.

Code Structure

The Website Monitor script consists of the following components:
1. website_monitor Function


import requests
import time

def website_monitor(url, response_time_limit):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    response_time = end_time - start_time
    try:
        if response.status_code == 200:
            print(f"The website {url} is up and running")
        else:
            print(f"The website {url} is down. Status Code: {response.status_code}")
    except requests.exceptions.RequestException:
        print(f"An error occurred while accessing {url}. The website may be down")
    performance_measure(response_time, response_time_limit)

This function is responsible for monitoring the website. It measures the response time of the website by sending an HTTP GET request to the specified URL. It also checks the HTTP status code to determine if the website is up or down.
2. performance_measure Function


def performance_measure(response_time, response_time_limit):
    try:
        if response_time > response_time_limit:
            print(f"Alert: {url} is down or not performing optimally. Response time: {response_time} seconds")
        else:
            print(f"Response time: {response_time} seconds")
    except requests.exceptions.RequestException:
        print(f"An error occurred while accessing the website...")

This function is responsible for measuring the performance of the website based on the response time. If the response time exceeds the specified limit, it raises an alert. Otherwise, it provides information about the response time.
3. Main Execution Block

if __name__ == "__main__":
    url = input("Enter the website URL: ")
    response_time_limit = 2.0
    website_monitor(url, response_time_limit)

The main execution block of the script prompts the user to enter the website URL and sets a default response time limit of 2.0 seconds. It then calls the website_monitor function to initiate the monitoring process.
Usage

    Run the Python script as described in the "Getting Started" section.

    Enter the website URL you want to monitor when prompted.

    The script will send an HTTP GET request to the specified URL and measure the response time.

    It will then check the HTTP status code to determine if the website is up or down.

    If the website is down, it will display an alert along with the HTTP status code.

    If the website is up, it will display the response time.

    Review the output to monitor the website's availability and performance.

Conclusion

The "Website Monitor" script provides a simple yet effective way to monitor the availability and performance of a website. By setting a response time limit, you can receive alerts when the website's performance falls below the defined threshold. This tool can be useful for website administrators and developers to ensure their websites are functioning optimally.
