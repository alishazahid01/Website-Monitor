import requests
import time

def website_monitor(url,response_time_limit):

    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    response_time = end_time - start_time
    try:
        if response.status_code == 200:
            print(f"The website {url} is up and running")
        
        else:
            print(f"The website {url} is down. Status Code: {response}")
    
    except requests.exceptions.RequestException:
        print(f"An error ocurred while accessing {url}. The website may be down")
    
    performance_measure(response_time, response_time_limit)

def performance_measure(response_time, response_time_limit):

    try:
        if response_time > response_time_limit:
            print(f"Alert: {url} is down or not performing optimally. Response time: {response_time} seconds")
        
        else:
            print(f"Response time: {response_time} seconds")
    
    except requests.exceptions.RequestException:
        print(f"An error occur while accessing the website...")


if __name__ == "__main__":

    url = input("Enter the website url: ")
    response_time_limit = 2.0
    website_monitor(url,response_time_limit)
