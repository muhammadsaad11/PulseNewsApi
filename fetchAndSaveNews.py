import requests
# import schedule
import time
from datetime import datetime

def hit_api_and_save():
    # Replace 'YOUR_API_ENDPOINT' with the actual API endpoint you want to hit
    # api_url = 'https://newsapi.org/v2/everything?q=technology+OR+AI+OR+startup+OR+Silicon+Valley&sortBy=popularity&apiKey=e8f37b515ebb44d9a0b038c6e3c19361'

    # currently using this one
    # api_url = 'https://newsapi.org/v2/everything?q=technology&sortBy=popularity&apiKey=e8f37b515ebb44d9a0b038c6e3c19361'


    # api_url = 'https://newsapi.org/v2/top-headlines?category=technology&country=us&apiKey=e8f37b515ebb44d9a0b038c6e3c19361'

    # api_url = 'https://newsapi.org/v2/everything?q=tech&sortBy=publishedAt&apiKey=e8f37b515ebb44d9a0b038c6e3c19361'

    # api_url = 'https://newsapi.org/v2/everything?q=technology&sortBy=publishedAt&apiKey=e8f37b515ebb44d9a0b038c6e3c19361'
    
    # api_url = 'https://newsapi.org/v2/everything?q=technology+AND+AI&sortBy=publishedAt&language=en&apiKey=e8f37b515ebb44d9a0b038c6e3c19361'

    api_url = 'https://newsapi.org/v2/everything?q=(technology+AND+AI)+NOT+(Celebrity+AND+Actor+AND+Actress+AND+Film+AND+Star+AND+Hollywood+AND+Award+AND+Shows+AND+Grammy+AND+Oscar+AND+Met+AND+Gala+AND+Emmy+AND+Religion+AND+Religious+AND+leaders+AND+Genocide+AND+Crime+AND+Stalker+AND+Weapon+AND+Babies)&sortBy=publishedAt&language=en&apiKey=e8f37b515ebb44d9a0b038c6e3c19361'

    try:
        # Make the GET request
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Save the response to a file (you can change the file name)
            with open(f'response_news12.json', 'w', encoding='utf-8') as file:
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
