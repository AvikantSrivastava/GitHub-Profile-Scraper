import json
import requests
from helpme import save_json, extract_data, group_with_same_key


class repo():
    def __init__(self , username , project_name):
        self.username = username
        self.project_name = project_name
    
    def get_repo_stats(self):
        RepoURL = 'https://api.github.com/repos/{}/{}'.format(self.username , self.project_name)
        RepoDataFromGithub = requests.get(RepoURL).json()
     
        DataNeeded = [
            'name',
            'html_url',
            'description',
            'forks',
            'open_issues',
            'language',
            'git_url',
            ]

        self.RepoData = extract_data(DataNeeded, RepoDataFromGithub)
        save_json('output_of_Repo' , self.RepoData)
        return json.dumps(self.RepoData , indent = True)
        
    def get_sha_values(self):
        CommitURL = 'https://api.github.com/repos/{}/{}/commits'.format(self.username, self.project_name)

        CommitListFromGithub = requests.get(CommitURL).json()

        # CommitListExtracted = group_with_same_key(CommitListFromGithub,'sha')
        CommitIDList = []
        for i in range(len(CommitListFromGithub)):
            CommitIDList.append(CommitListFromGithub[i]['sha'])
        return CommitIDList

        # save_json('CommitListFromGithub', CommitListFromGithub)

repoo = repo('avikantsrivastava' , '100-days-of-ML-Code')
data = repoo.get_repo_stats()
repoo.get_sha_values()
# print(data)