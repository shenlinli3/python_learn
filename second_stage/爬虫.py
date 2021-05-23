# -*- coding: utf-8 -*-

"""
@Time    : 2021/05/21 19:20
@Author  : shenlinli

"""

import requests
import re
import threading
import time
if __name__ == '__main__':
    # print(len(list01))
    # print(list01[len(list01)-1])

    def get_content(head_html,list_):
        # tmp = []
        # i  = 0
        while list_:
            url = head_html + list_[0][0]
            print(url)
            res = requests.get(url)
            res.encoding = res.apparent_encoding
            content_pattern = "<div id=\"content\">(.+?)</div>"
            ress = re.search(content_pattern, res.text)

            content = str(ress.group(1))
            content = content.replace("&nbsp;&nbsp;&nbsp;&nbsp;", "\t")
            content = content.replace("<br><br>", "\n")
            threadLock = threading.Lock()
            with open("三寸人间.txt", "a", encoding="utf-8") as fw:
                threadLock.acquire()
                fw.write("\t\t\t\t" + list_[0][1] + "\n")
                fw.write(content)
                threadLock.release()


            list_ = list_[1:]
        # for i in range(1,11):
        #     threading.Thread(target=get_content,name=f"线程{i}",args=["https://www.biquge.com.cn/",list_all[0:i*20]])


    head_html = "https://www.biquge.com.cn"
    res = requests.get("https://www.biquge.com.cn/book/31833/")
    # print(res.text)
    res.encoding = res.apparent_encoding
    # print(type(res.text))
    novel_head_pattern = "<dd><a href=\"(.+?)\"\s*(?:class=\"empty\")?>(.+?)</a></dd>"
    list_all = re.findall(novel_head_pattern, res.text)

    # get_content(head_html,list_all[0:3])
    print(len(list_all))
    for i in range(1,11):
        threading.Thread(target=get_content,name=f"Thread{i}",args=[head_html,list_all[:137]]).start()
        list_all = list_all[137:]

    time.sleep(200)
    print(list_all)