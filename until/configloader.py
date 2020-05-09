import os
import yaml

def loadConfig(yamlName):
    rootPath = os.path.dirname(os.path.abspath(__file__)).split('until')[0]
    yamlPath = os.path.join(rootPath, yamlName)
    return yaml.load(open(yamlPath, 'r', encoding='utf-8').read(), yaml.FullLoader)
