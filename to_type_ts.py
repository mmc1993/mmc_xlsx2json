# MIT License
# 
# Copyright (c) 2024 mmc
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# coding=utf-8

def clsid(obj):
    return "__%d__" % id(obj)

def sid(obj):
    return str(id(obj))

#   生成字符串
def indent(count):
    return "".join(" " for i in range(count * 4))

def to_type(namespace, type_desc_all):
    body = "\n".join([gen_from_file(type_desc[0],    \
                                    type_desc[1])
                      for type_desc in type_desc_all])
    return "declare namespace %s {\n%s\n}" % (namespace, body)

def fill_noname_types(type_desc, list):
    for sub in type_desc.subs:
        fill_noname_types(sub, list)
    if type_desc.get_type_name() == "t":
        list.append(type_desc)

def gen_from_file(type_name, type_descs):
    #   过滤注释类型
    type_descs = [type_desc for type_desc in \
                  type_descs if type_desc != None]
    
    #   收集内联类型
    noname_types = []
    for type_desc in type_descs:
        fill_noname_types(type_desc, noname_types)

    #   为内联类型生成名字
    name_map = {}
    for type_desc in noname_types:
        name_map[sid(type_desc)] = "_noname_%s_%d" \
                        % (type_name, len(name_map))

    struct_text = gen_structs(name_map, noname_types, 1)
    member_text = gen_members(name_map, type_descs,   2)
    if len(struct_text) > 0: struct_text += "\n"
    return "{0}{1}class {2} {{\n{3}\n{1}}}".format(  \
            struct_text, indent(1), type_name, member_text)


def gen_structs(name_map, type_descs, depth):
    format = "{0}class {2}\n{0}{{\n{1}\n{0}}}"
    return "\n".join([format.format(indent(depth),          \
        gen_struct(name_map, type_desc, depth + 1),         \
        name_map[sid(type_desc)]) for type_desc in type_descs])

def gen_struct(name_map, type_desc, depth):
    return "".join(gen_members(name_map, type_desc.subs, depth))

def gen_members(name_map, type_descs, depth):
    return "\n".join([gen_member(name_map, type_desc, depth) + ";" for type_desc in type_descs])

#   生成成员
def gen_member(name_map, type_desc, depth):
    typekey = type_desc.get_type_name()
    if typekey == "i" or typekey == "f":
        if len(type_desc.name) != 0:
            return "%spublic %s: number" % (indent(depth), type_desc.name)
        else:
            return "number"
    elif typekey == "s":
        if len(type_desc.name) != 0:
            return "%spublic %s: string" % (indent(depth), type_desc.name)
        else:
            return "string"
    elif typekey == "b":
        if len(type_desc.name) != 0:
            return "%spublic %s: Boolean" % (indent(depth), type_desc.name)
        else:
            return "Boolean"
    elif typekey == "list":
        memeber = gen_member(name_map, type_desc.subs[0], depth)
        if len(type_desc.name) != 0:
            return "%spublic %s: Array<%s>" % (indent(depth), type_desc.name, memeber)
        else:
            return "Array<%s>" % memeber
    elif typekey == "dict":
        memeber = gen_member(name_map, type_desc.subs[1], depth)
        if len(type_desc.name) != 0:
            return "%spublic %s: Map<string, %s>" % (indent(depth), type_desc.name, memeber)
        else:
            return "Map<string, %s>" % memeber
    elif type_desc.get_type_name() == "t":
        if len(type_desc.name) != 0:
            return "%spublic %s: %s" % (indent(depth), type_desc.name, name_map[sid(type_desc)])
        else:
            return "%s" % name_map[sid(type_desc)]
    assert False, "类型解析错误: 未知类型 %s" % type_desc.type

