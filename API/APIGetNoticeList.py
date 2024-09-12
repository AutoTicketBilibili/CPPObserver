import BasicInfo
from BasicVoid import sendInfo


def getNoticeList():
    url = ("https://www.allcpp.cn/allcpp/eventMain/notice/getList.do?pageindex=1&pagesize=15&id=" +
           BasicInfo.config["eventID"])
    data = BasicInfo.sessionBot.get(url, headers=BasicInfo.headers, timeout=(9.05, 15.05))
    return data.json()
