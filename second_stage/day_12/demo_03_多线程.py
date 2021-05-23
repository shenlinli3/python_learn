# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/23 14:05
@Author  : zero
"""

# 进程和线程
# 进程：电脑上安装了一个QQ程序，可以启动多次，并且它们是独立运行的，一个挂掉了，其它的不受影响
# 线程：打开一个浏览器，浏览器中可以开多个窗口，每个窗口都可以独立的进行任务
# 线程的执行顺序是操作系统随机调度
import threading
import time


# print(f"主线程开始 {threading.current_thread()}")
# def test():
#     print(f"{time.strftime('%Y%m%d%H%M%S')} 程序开始：{threading.current_thread()}")
#     for i in range(1, 6):
#         print(f"{threading.current_thread()} -> {i}")
#         time.sleep(0.5)
#     time.time()
#     print(f"{time.strftime('%Y%m%d%H%M%S')} 程序结束：{threading.current_thread()}")
#
# t1 = threading.Thread(target=test, name="新线程1")
# t2 = threading.Thread(target=test, name="新线程2")
# t1.start()
# t2.start()
#
# time.sleep(10)
# print(f"主线程结束 {threading.current_thread()}")


# 线程安全问题
# lock = threading.Lock()  # 初始化一个线程锁
money = 1000
def change_balance(x):
    global money
    for i in range(10000000):
        # lock.acquire()  # 加锁
        money += x
        money -= x
        # lock.release()  # 释放锁

t1 = threading.Thread(target=change_balance, name="线程01", args=[8,])
t2 = threading.Thread(target=change_balance, name="线程02", args=[5,])
t1.start()
t2.start()
time.sleep(10)
print(money)