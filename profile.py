import json
import requests
# from pprint import pprint

# Username = input("Enter Your Username")
# Username = 'avikantsrivastava'

# UserURL = 'https://api.github.com/users/{}'.format(Username)

# UserDataFromGithub = requests.get(UserURL).json()


class User():

    def __init__(self, Username):
        self.Username = Username
        self.UserURL = 'https://api.github.com/users/{}'.format(self.Username)
        # this is data from github, we dont need all of it
        UserDataFromGithub = requests.get(self.UserURL).json()


        # this it the data we need
        self.Name = UserDataFromGithub['name']
        self.UserType = UserDataFromGithub['type']
        self.Company = UserDataFromGithub['company']
        self.Blog = UserDataFromGithub['blog']
        self.Location = UserDataFromGithub['location']
        self.Email = UserDataFromGithub['email']
        self.PublicRepo = UserDataFromGithub['public_repos']
        self.Followers = UserDataFromGithub['followers']

    def get_json(self):
        UserData = self.__dict__
        # print(UserData)

        return json.dumps(UserData, indent= True)

    def pprint(self):
        # print(self.Name)
        # print(self.Location)
        print(self )

avikant = User('avikantsrivastava')
data = avikant.get_json()
print(data)