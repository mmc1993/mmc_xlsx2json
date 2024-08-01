# coding=utf-8

#   描述: xlsx输出json
#   作者: mmc
#   日期: 2020-03-21

import os
import sys
sys.path.append("..")

import tojson
import gen_struct_define_cpp
import gen_struct_define_cs

#   Json输入目录
JSON_I = os.getcwd() + "/in/"
#   Json输出目录
JSON_O = os.getcwd() + "/out/"
#   结构化输出目录
STRUCT_O = os.getcwd() + "/out/config.cpp"
#   命名空间
NAMESPACE = "config"

def Write(url, data):
    with open(url, "w", encoding = "utf-8") as f:
        f.write(data)

def Export():
    output_json_list = []
    parser_wrap_list = []
    for name in os.listdir(JSON_I):
        split = os.path.splitext(name)
        if split[1] == ".xlsx" and split[0][0] != "~":
            name, output_json, parser_wrap = tojson.ToJson(JSON_I + name)
            output_json_list.append((name, output_json))
            parser_wrap_list.append((name, parser_wrap))

    #   写入Json
    try: os.rmdir(JSON_O)
    except: pass
    try: os.mkdir(JSON_O)
    except: pass

    for info in output_json_list:
        print(info[0])
        Write(JSON_O + info[0] + ".json", info[1])

    #   写入C#
    # Write(STRUCT_O, gen_struct_define_cs.gen(NAMESPACE, parser_wrap_list))
    Write(STRUCT_O, gen_struct_define_cpp.gen(NAMESPACE, parser_wrap_list))

if __name__ == "__main__":
    try:
        Export()
    except AssertionError as e:
        print("> 异常: %s" % e)
    print("> ---Export End---")

