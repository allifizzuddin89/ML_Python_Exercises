import json
import requests
import pathlib

response = requests.get("https://jsonplaceholder.typicode.com/todos")
# with open("response.txt", "w+"):
#     json.loads(response, response1) #revised!!!
todos = json.loads(response.text)
print(todos == response.json())
print(type(todos))
#print(todos[:])

#assignment 1
#determine which user has complete the task

#map of userId to number of complete TODOs for that user
todos_by_user = {}

#increment complete TODOs count for each user.
for todo in todos:
    if todo["completed"]:
        try:
            #increment the existing user's account
            todos_by_user[todo["userId"]] += 1
            print("The todos user is ",todos_by_user[todo["userId"]])
            #print("The userId is {}".format(userId)) #error
        except KeyError:
            #this user has not been seen. set their count to 1
            todos_by_user[todo["userId"]] = 1

#create a sorted list of (userId, num_complete) pairs
top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
print(top_users, end=" ")

#get the maximum number of complete TODOs
max_complete = top_users[0][1]
print("\nmax complete is {}".format(max_complete))

#create a list of all users who have completed
#the maximum number of TODOs
users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)
print("max users are {}".format(max_users))
print(pathlib.Path(__file__).parent) #check current dir, import pathlib

