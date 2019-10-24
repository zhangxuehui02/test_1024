import yaml
import os
from config import  BASE_URL
def read_yaml(fileame):
    with open(BASE_URL+ os.sep+'data'+os.sep+fileame,'r',encoding='utf-8')as f:
        return yaml.load(f)
if __name__ == '__main__':
    arr =[]
    for data in read_yaml('data.yaml').values():
        arr.append(tuple(data.values()))
    print(arr)
