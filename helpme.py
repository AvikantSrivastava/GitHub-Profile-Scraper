import json

def save_json(filename , json_data):
    with open('{}.json'.format(filename), 'w') as fp:
        json.dump(json_data, fp , indent= True)



def extract_data(DataNeeded, DataFromGithub, ):
    Data = {}
    for (k, v) in DataFromGithub.items():

            if k in DataNeeded:
                Data[k] = v
    
    return Data
    
