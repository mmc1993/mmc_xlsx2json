# coding=utf-8

#   描述: xlsx输出json
#   作者: mmc
#   日期: 2020-03-21

import os
import sys
sys.path.append("..")
import mmc_xlsl2json

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
    file_struct_wraps = []
    for fname in os.listdir(in_dir):
        split = os.path.splitext(fname)
        if split[1] == ".xlsx" and split[0][0] != "~":
            in_fullpath = in_dir + fname
            name, json, wrap = mmc_xlsl2json.to_json.to_json(in_fullpath)
            file_struct_wraps.append((name, wrap))
            Write(out_dir + name + ".json", json)
            print(in_fullpath, "=>", name)

    #   写入C#
    cs_key_words_lut = {
        "scope": "public ",
        "class": "class",
        "i": "int",
        "b": "bool",
        "f": "float",
        "s": "string",
        "list": "List",
        "dict": "Dict",
    }
    cs_body_template = "using System.Collections.Generic;\n\nnamespace %s {\n%s\n}"
    Write(out_type_dir + "type_define.cs", mmc_xlsl2json.to_type.to_type("demo.config", cs_key_words_lut, cs_body_template, file_struct_wraps))

    cpp_key_words_lut = {
        "scope": "",
        "class": "struct",
        "i": "int",
        "b": "bool",
        "f": "float",
        "s": "std::string",
        "list": "std::vector",
        "dict": "std::map",
    }
    cpp_body_template  = "#include <string>\n#include <vector>\n#include <map>\n\nnamespace %s {\n%s\n}"
    Write(out_type_dir + "type_define.cpp", mmc_xlsl2json.to_type.to_type("demo::config", cpp_key_words_lut, cpp_body_template, file_struct_wraps))

if __name__ == "__main__":
    try:
        Export()
    except AssertionError as e:
        print("> 异常: %s" % e)
    print("> ---Export End---")

