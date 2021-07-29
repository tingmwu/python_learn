import requests
import os, sys
# from configparser import ConfigParser


def get_tracker():
    print("获取tracker列表......")
    url = 'https://trackerslist.com/all_aria2.txt'
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.text
    except:
        print('failed get tracker from {}'.format(url))
        sys.exit(0)

def write_conf(trackers):
    path = './aria2.conf'

    data = ''
    with open(path, 'r+', encoding='utf-8') as fp:
        for line in fp.readlines():
            if (line.find("bt-tracker=") == 0):
                line = "bt-tracker=" + trackers
            data += line

    with open(path, 'w', encoding='utf-8') as fp: 
        fp.writelines(data)

if __name__ == '__main__':
    trackers = get_tracker()
#    print(trackers)
    write_conf(trackers)
    print("更新tracker成功！")
    os.system("pause")
    
    
