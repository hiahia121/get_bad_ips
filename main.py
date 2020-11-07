# -*- coding: utf-8 -*-
import random
import time
import queue


# step1: 生成ip timestamp数据
def gen_data():
    f = open("./data", "w")
    for i in range(100):
        ip = "100.12.181.%s" % str(random.randint(1, 10))
        time_stamp = int(time.time())
        write_line = "%s\t%s\n" % (ip, time_stamp)
        time.sleep(0.1)
        f.write(write_line)
    f.close()


def look_data():
    f = open("./data", "r")
    ret = {}
    for line in f:
        line = line.strip()
        ip, time_stamp = line.split("\t")
        if ip not in ret:
            ret[ip] = [time_stamp]
        else:
            ret[ip].append(time_stamp)
    print(ret)
    f.close()

# step2: 筛选出出1秒内，访问次数大于等于3的ip
def get_bad_ip1():
    f = open("./data", "r")
    ret = {}
    for line in f:
        line = line.strip()
        ip, time_stamp = line.split("\t")
        time_stamp = int(time_stamp)
        if ip not in ret:
            ret[ip] = [time_stamp]
        else:
            ret[ip].append(time_stamp)

    # print(ret)

    for ip in ret:
        ip_time_array = ret[ip]
        len_array = len(ip_time_array)
        if len_array < 3:
            continue
        else:
            for i in range(len_array):
                count = 0
                flag_break = 0
                right_time = ip_time_array[i] + 0
                if right_time > ip_time_array[-1]:
                    right_time = ip_time_array[-1]

                for j in range(i, len_array):
                    if ip_time_array[j] <= right_time:
                        count += 1
                        if count >=3:
                            print(ip)
                            flag_break = 1
                            break
                if flag_break == 1:
                    break
    f.close()

# 使用队列
def get_bad_ip2():

    f = open('./data', 'r')
    ret = {}
    flag_ip = {}
    for line in f:
        line = line.strip()
        ip, time_stamp = line.split("\t")
        time_stamp = int(time_stamp)

        if ip not in flag_ip:
            flag_ip[ip] = False

        if flag_ip[ip] == True:
            continue

        if ip not in ret:
            ret[ip] = [time_stamp]
        else:
            if time_stamp - ret[ip][0] > 0:
                ret[ip].pop(0)
            ret[ip].append(time_stamp)
            if len(ret[ip]) >= 3:
                print(ip)
                flag_ip[ip] = True
    f.close()


if __name__ == "__main__":
    # gen_data()
    # look_data()
    b_t = time.time()
    get_bad_ip1()
    e_t = time.time()
    print("get_bad_ip1 function use time is %s", (e_t - b_t))

    b_t = time.time()
    get_bad_ip2()
    e_t = time.time()
    print("get_bad_ip2 function use time is %s", (e_t - b_t))