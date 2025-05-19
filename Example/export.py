# coding=utf-8

#   描述: xlsx输出json
#   作者: mmc
#   日期: 2020-03-21

import os
import sys
sys.path.append("../")
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import xlsl2json

#   输入
in_dir = os.getcwd() + "/in/"
#   输出
out_dir = os.getcwd() + "/out/"
#   类型输出
out_type_dir = os.getcwd() + "/out/"

try: os.rmdir(out_dir)
except: pass
try: os.mkdir(out_dir)
except: pass

def Write(url, data):
    with open(url, "w", encoding = "utf-8") as f:
        f.write(data)

def Export():
    type_desc = []
    for fname in os.listdir(in_dir):
        split = os.path.splitext(fname)
        if split[1] == ".xlsx" and split[0][0] != "~":
            in_fullpath = in_dir + fname
            name, json, desc = xlsl2json.to_json.to_json(in_fullpath)
            type_desc.append((name, desc))
            Write(out_dir + name + ".json", json)
            print(in_fullpath, "=>", name)

    Write(out_type_dir + "type_define.d.ts", xlsl2json.to_type_ts.to_type("XL", type_desc))

if __name__ == "__main__":
    try:
        Export()
    except AssertionError as e:
        print("> 异常: %s" % e)
    print("> ---Export End---")

