# Name: Todd Mizera
#Date: 1/21/24

from Queue import Queue
from Call import Call
from datetime import date
import time  # Use to pause application
import random  # use to generate random numbers

# displays author's name and the date in the output
print("Name: Todd Mizera")
print("Date: ", date.today())

# Create a list
calls = []

# read call records into list
input_file_name = "CallsData.csv"
with open(input_file_name) as infile:
    for line in infile:
        # split the line based on commas
        s = line.split(',')
        client_id = int(s[0])
        client_name = s[1]
        client_phone = s[2]
        # create a call object based on the data from the line
        a_call = Call(client_id, client_name, client_phone)
        # add the cal object to the list
        calls.append(a_call)

# Queue object for our calls
calls_waiting = Queue()
call_number = 0

# how long is the simulation
seconds = int(input("How many seconds would you like to simulate "))

# run the simulation for given number of seconds
for i in range(seconds):
    print("-" * 40)
    time.sleep(2)
    random_event = random.randint(1, 3)
    # do the event based on the random number generated
    if random_event == 1:
        print("Call was received. Caller added to Queue")
        calls_waiting.enqueue(calls[call_number])
        call_number += 1  # set up the next call
        print("\t Number of calls waiting in Queue: ",
              calls_waiting.get_length())
    elif random_event == 2:
        print("Call sent to representative for seervice")
        if calls_waiting.get_length() > 0:
            print("Caller Information")
            print(calls_waiting.dequeue())
        else:
            print("The Call waiting Queue is empty")
        print("\t Number of calls waiting in queue", calls_waiting.get_length())
    else:
        print("Nothing Happened in this second of time")
        print("\t Number of calls waiting in queue", calls_waiting.get_length())

print("The Automatic Call Distributor Simulation has completed.")
