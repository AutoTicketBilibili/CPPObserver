import BasicInfo
from BasicVoid import sendInfo


def getTicketTypeList():
    url = "https://www.allcpp.cn/allcpp/ticket/getTicketTypeList.do?eventMainId=" + BasicInfo.config["eventID"]
    data = BasicInfo.sessionBot.get(url,headers=BasicInfo.headers,timeout=(9.05, 15.05))
    return data.json()
