import threading
import time

import API.APIGetNoticeList
import API.APIBroadcast
import API.APIMail
import BasicVoid

task = "公告监听"


def runObserver():
    BasicVoid.sendInfo("正在启动"+task+"线程......")
    thread = threading.Thread(target=observer, name=task+"线程", args=())
    thread.start()


def observer():
    noticeList = []
    while True:
        try:
            time.sleep(1)
            newList = []
            data = API.APIGetNoticeList.getNoticeList()
            for notice in data:
                noticeID = notice["id"]
                noticeName = notice["works"]["name"]
                noticeAuthor = notice["works"]["user"]["nickname"]
                newList.append(noticeID)
                if not noticeList:
                    continue
                if noticeID not in noticeList:
                    message = "公告更新提醒\r\n"
                    message += ("标题：" + noticeName + "\r\n")
                    message += ("作者：" + noticeAuthor)
                    BasicVoid.sendInfo(message)
                    API.APIBroadcast.sendBroadcast(message)
                    API.APIMail.sendMail(message)
            noticeList = newList
        except Exception as e:
            BasicVoid.sendWarn(str(repr(e)))
            BasicVoid.sendWarn(task+"报错啦！再试试！")

