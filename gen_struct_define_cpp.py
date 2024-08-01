# coding=utf-8

#   描述: Json转Cpp数据结构
#   作者: mmc
#   日期: 2020-03-20

def uid(parser):
    return "__%d__" % id(parser)

#   生成字符串
def indent(count):
    return "".join(" " for i in range(count * 4))

#   收集结构体类型
def collect_struct(parser_wrap, result):
    for sub in parser_wrap.subs:
        collect_struct(sub, result)
    if parser_wrap.get_type_name() == "struct":
        result.append(parser_wrap)

#   生成成员
def gen_member(parser_wrap, depth):
    if parser_wrap.get_type_name() == "int":
        if len(parser_wrap.name) != 0:
            return "%sint %s" % (indent(depth), parser_wrap.name)
        else:
            return "int"
    elif parser_wrap.get_type_name() == "str":
        if len(parser_wrap.name) != 0:
            return "%sstd::string %s" % (indent(depth), parser_wrap.name)
        else:
            return "std::string"
    elif parser_wrap.get_type_name() == "bool":
        if len(parser_wrap.name) != 0:
            return "%sbool %s" % (indent(depth), parser_wrap.name)
        else:
            return "bool"
    elif parser_wrap.get_type_name() == "float":
        if len(parser_wrap.name) != 0:
            return "%sfloat %s" % (indent(depth), parser_wrap.name)
        else:
            return "float"
    elif parser_wrap.get_type_name() == "list":
        memeber = gen_member(parser_wrap.subs[0], depth)
        if len(parser_wrap.name) != 0:
            return "%s%s<%s> %s" % (indent(depth), "std::vector", memeber, parser_wrap.name)
        else:
            return "%s<%s>" % ("std::vector", memeber)
    elif parser_wrap.get_type_name() == "dict":
        memeber = gen_member(parser_wrap.subs[1], depth)
        if len(parser_wrap.name) != 0:
            return "%s%s<std::string, %s> %s" % (indent(depth), "std::map", memeber, parser_wrap.name)
        else:
            return "%s<std::string, %s>" % ("std::map", memeber)
    elif parser_wrap.get_type_name() == "struct":
        if len(parser_wrap.name) != 0:
            return "%s%s %s" % (indent(depth), uid(parser_wrap), parser_wrap.name)
        else:
            return "%s" % (uid(parser_wrap))
    assert False, "类型解析错误: 未知类型[%s]" % parser_wrap.type

def gen_members(units, depth):
    members = [gen_member(unit, depth) + ";" for unit in units]
    return "\n".join(members)

#   生成结构
def gen_struct(parser_wraps, depth):
    structs = gen_members(parser_wraps.subs, depth)
    return "".join(structs)

def gen_structs(parser_wraps, depth):
    fmt = "{0}struct {1} {{\n{2}\n{0}}};"
    return "\n".join([fmt.format(           \
        indent(depth), uid(parser_wrap),    \
        gen_struct(parser_wrap,depth+1))    \
        for parser_wrap in parser_wraps])

def gen_from_file(parser_wraps, name):
    struct_list = []
    [collect_struct(parser_wrap, struct_list) for parser_wrap in parser_wraps]
    text_struct = gen_structs(struct_list,  2)
    text_member = gen_members(parser_wraps, 2)
    param = (indent(1), name, text_struct, text_member)
    return "{0}struct {1} {{\n{2}\n{3}\n{0}}};".format(*param)

def gen(namespace, parser_wrap_list):
    body = "\n".join([gen_from_file(parser_wrap[1],     \
                                    parser_wrap[0])     \
                    for parser_wrap in parser_wrap_list])
    fmt  = "#include <string>\n"
    fmt += "#include <vector>\n"
    fmt += "#include <map>\n\n"
    fmt += "namespace %s {\n%s\n}"
    return fmt % (namespace, body)