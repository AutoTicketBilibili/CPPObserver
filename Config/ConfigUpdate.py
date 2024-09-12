import json

import BasicInfo


def updateConfig(key, value):
    BasicInfo.config[key] = value
    writeConfig()


def updateCookie(key, value):
    cookie = BasicInfo.config["Cookie"].split(";")
    cookieNew = ""
    for part in cookie:
        if not part.startswith(key):
            cookieNew += (part + ";")
    cookieNew += (key + "=" + value)
    updateConfig("Cookie", cookieNew)
    BasicInfo.headers["Cookie"] = BasicInfo.config["Cookie"]


def writeConfig():
    file = open("config.json", 'w', encoding='utf-8')
    json.dump(BasicInfo.config, file, indent=4, ensure_ascii=False)
