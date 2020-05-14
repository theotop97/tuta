import os
import yaml

'''
通过yaml文件来读取测试时使用的环境配置
yaml文件确保要放在主目录下

    yamlName:yaml配置文件的名字
'''

def loadConfig(yamlName):
    # 找到config的路径

    yamlPath = os.path.abspath(".") + r"/config/" + yamlName
    return yaml.load(open(yamlPath, 'r', encoding='utf-8').read())

