import json
import requests
from helpme import save_json, extract_data


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

        RepoData = extract_data(DataNeeded, RepoDataFromGithub)

        

        # print(json.dumps(RepoData , indent = True))
        save_json('test2' , RepoData)

        return json.dumps(RepoData , indent = True)
        

        # print(RepoDataFromGithub[1]['description'])
        # print(json.dumps(RepoDataFromGithub , indent= True))

    # def get_commits(self):
    #     CommitURL = 'https://api.github.com/repos/{}/{}/commits?sha=master'.format(self.username , self.project_id)
        
    #     CommitDataFromGithub = requests.get(RepoURL).json()

    #     print


repoo = repo('avikantsrivastava' , '100-days-of-ML-Code')
data = repoo.get_repo_stats()
print(data)