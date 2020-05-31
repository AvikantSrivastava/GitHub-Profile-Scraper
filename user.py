import json
import requests
from helpme import extract_data
# from pprint import pprint

# Username = input("Enter Your Username")
# Username = 'avikantsrivastava'

# UserURL = 'https://api.github.com/users/{}'.format(Username)

# UserDataFromGithub = requests.get(UserURL).json()


class User():

    def __init__(self, Username):
        self.Username = Username
        self.UserURL = 'https://api.github.com/users/{}'.format(self.Username)        

    def get_user_stats(self):

        # this is data from github, we dont need all of it
        UserDataFromGithub = requests.get(self.UserURL).json()
        DataNeeded = [
            'name',
            'type',
            'company',
            'blog',
            'location',
            'email',
            'public_repos',
            'followers'
        ]
        self.UserData = extract_data(DataNeeded, UserDataFromGithub)
        return json.dumps(self.UserData, indent= True)


avikant = User('avikantsrivastava')
data = avikant.get_user_stats()
print(data)