# import threading
# import time
# import os

# def clearAfter15():
#     clear = lambda: os.system('cls')
#     clear()

# string_variable="Help me out!"
# t = threading.Timer(1*6, clearAfter15)
# t.start()
# print(string_variable)


# import time

# # Set the time limit in seconds (e.g., 3 hours = 3 * 60 * 60 seconds)
# time_limit = 3 * 60 * 60
# # time_limit = 16 * 1 * 1


# # Start time
# start_time = time.time()

# # Loop until the time limit is reached
# while time.time() - start_time < time_limit:
#     # Delay for one hour (3600 seconds)
#     # delay = 3600
#     delay = 25
#     time.sleep(delay)

#     # Print the message after the delay
#     print("Delayed message!")

# # Print a final message after the time limit is reached
# # print("Time limit reached. Exiting...")




import datetime
import time

# Set the time limit in hours
time_limit_hours = 3

# Get the current local time
current_time = datetime.datetime.now()

# Calculate the end time by adding the time limit to the current time
end_time = current_time + datetime.timedelta(hours=time_limit_hours)

# Loop until the end time is reached
while datetime.datetime.now() < end_time:
    # Delay for one hour (3600 seconds)
    # delay = 3600
    delay = 5
    time.sleep(delay)

    # Print the message after the delay
    print("Delayed message!",current_time)

# Print a final message after the time limit is reached
print("Time limit reached. Exiting...")