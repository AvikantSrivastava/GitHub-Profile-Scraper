import json
import requests

def save_json(filename , json_data):
    with open('{}.json'.format(filename), 'w') as fp:
        json.dump(json_data, fp , indent= True)

class repo():
    def __init__(self , username , project_id):
        self.username = username
        self.project_id = project_id
    
    def get_repo_stats(self):
        RepoURL = 'https://api.github.com/repos/{}/{}'.format(self.username , self.project_id)
        RepoDataFromGithub = requests.get(RepoURL).json()
        
        # RepoData = {}
        # RepoData['name']
        DataNeeded = [
            'name',
            'html_url',
            'description',
            'forks',
            'open_issues',
            'language',
            'git_url',
            ]

        RepoData = {}

        for (k, v) in RepoDataFromGithub.items():
            # print("Key: " + k)
            # print("Value: " + str(v))
            if k in DataNeeded:
                RepoData[k] = v
        

        print(json.dumps(RepoData , indent = True))

        return RepoData
        

        # print(RepoDataFromGithub[1]['description'])
        # print(json.dumps(RepoDataFromGithub , indent= True))

    def get_commits(self):
        CommitURL = 'https://api.github.com/repos/{}/{}/commits?sha=master'.format(self.username , self.project_id)
        
        CommitDataFromGithub = requests.get(RepoURL).json()

        print


repoo = repo('avikantsrivastava' , '100-days-of-ML-Code')
repoo.get_repo_stats()