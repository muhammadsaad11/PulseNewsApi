import requests
# import schedule
import time
from datetime import datetime

def hit_api_and_save():

    api_url = 'https://newsapi.org/v2/everything?q=mortgage+AND+appraisal&sortBy=publishedAt&language=en&apiKey=e8f37b515ebb44d9a0b038c6e3c19361'

    try:
        # Make the GET request
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Save the response to a file (you can change the file name)
            with open(f'response_news_mortgage.json', 'w', encoding='utf-8') as file:
                file.write(response.text)
            print(f"API request successful at {datetime.now()}")
        else:
            print(f"API request failed with status code {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")


print("Server Running...")
# Schedule the job to run every day at a specific time (change 'HH:MM' to your desired time)
# schedule.every().day.at('13:45').do(hit_api_and_save)

# # Run the scheduling loop
# while True:
#     schedule.run_pending()
#     time.sleep(1)

hit_api_and_save()
