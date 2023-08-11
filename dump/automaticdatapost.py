# import time
# import requests
# import schedule

# # Set the time limit in seconds
# time_limit = 4  # 1 hour

# # Define the data to be posted
# data = {
      
#             "role_name": "Mar"
                        
# }

# # Set the URL of your Django API endpoint
# url = 'http://127.0.0.1:9999/manage_role_list'

# # Start time

# # schedule.every(1).minute.do(post_data)
# start_time = time.time()

# # Loop until the time limit is reached
# while time.time() - start_time < time_limit:
#     try:
#         # Send a POST request to the Django API
#         response = requests.post(url, data=data)
#         if response.status_code == 200:
#             print("Data posted successfully!")
#         else:
#             print("Failed to post data. Status code:", response.status_code)
#     except requests.exceptions.RequestException as e:
#         print("An error occurred:", e)

#     # Delay for a specific interval before posting again
#     delay = 1 # Delay in seconds (e.g., 60 seconds = 1 minute)
#     time.sleep(delay)

# print("Time limit reached. Exiting...")


import time
import requests
import schedule

# Set the time limit in seconds
time_limit = 4  # 1 hour

# Define the data to be posted
data =    {
            
            "module_name": "Inventory",
            "module_slug": "Inventory",
            "status": "Active"
        }

# Set the URL of your Django API endpoint
url = 'http://127.0.0.1:9999/manage_module_list'

# Function to post data
def post_data():
    try:
        # Send a POST request to the Django API
        response = requests.post(url, data=data)
        if response.status_code == 201:
            print("Data posted successfully!")
        else:
            print("Failed to post data. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

# Schedule the data posting
schedule.every(1).seconds.do(post_data)
# schedule.every(1).minute.do(post_data)


schedule.every(10).minutes.do(post_data)

# After every hour geeks() is called.
schedule.every().hour.do(post_data)

# Every day at 12am or 00:00 time bedtime() is called.
schedule.every().day.at("00:00").do(post_data)

# After every 5 to 10mins in between run work()
schedule.every(5).to(10).minutes.do(post_data)

# Every monday good_luck() is called
schedule.every().monday.do(post_data)

# Every tuesday at 18:00 sudo_placement() is called
schedule.every().tuesday.at("18:00").do(post_data)


# Start time
start_time = time.time()

# Loop until the time limit is reached
while time.time() - start_time < time_limit:
    schedule.run_pending()
    time.sleep(1)

print("Time limit reached. Exiting...")