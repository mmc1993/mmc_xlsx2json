# coding=utf-8

def uid(obj):
    return "__%d__" % id(obj)

#   生成字符串
def indent(count):
    return "".join(" " for i in range(count * 1))

def to_type(namespace, file_struct_wraps, key_words_lut, body_template):
    body = "\n".join([gen_from_file(file_struct_wrap[0],    \
                                    file_struct_wrap[1],    \
                                    key_words_lut)          \
        for file_struct_wrap in file_struct_wraps])
    return body_template % (namespace, body)

def collect_struct(parser_wrap, result):
    for sub in parser_wrap.subs:
        collect_struct(sub, result)
    if parser_wrap.get_type_name()=="t":
        result.append(parser_wrap)

def gen_from_file(file_struct_name, file_struct_parser_wraps, key_words_lut):
    file_struct_parser_wraps = [file_struct_parser_wrap for file_struct_parser_wrap in \
                                file_struct_parser_wraps if file_struct_parser_wrap != None]

    struct_list = []
    for file_struct_parser_wrap in file_struct_parser_wraps:
        collect_struct(file_struct_parser_wrap, struct_list)

    struct_text = gen_structs(struct_list, key_words_lut, 2)
    print(struct_text)
    # text_member = gen_members(file_struct_parser_wraps, 2)
    # param = (indent(1), file_struct_name, text_struct, text_member)
    # return "{0}public class {1} {{\n{2}\n{3}\n{0}}};".format(*param)
    return ""

def gen_structs(parser_wraps, key_words_lut, depth):
    format = "{0} {1} {{\n{2}\n{0}}};"
    return "\n".join([
        format.format(indent(depth), key_words_lut["struct"],       \
        uid(parser_wrap), gen_struct(parser_wrap, depth + 1))       \
        for parser_wrap in parser_wraps])

#   生成成员
def gen_member(parser_wrap, depth):
    if parser_wrap.get_type_name() == "i":
        if len(parser_wrap.name) != 0:
            return "%spublic int %s" % (indent(depth), parser_wrap.name)
        else:
            return "int"
    elif parser_wrap.get_type_name() == "s":
        if len(parser_wrap.name) != 0:
            return "%spublic string %s" % (indent(depth), parser_wrap.name)
        else:
            return "string"
    elif parser_wrap.get_type_name() == "b":
        if len(parser_wrap.name) != 0:
            return "%spublic bool %s" % (indent(depth), parser_wrap.name)
        else:
            return "bool"
    elif parser_wrap.get_type_name() == "f":
        if len(parser_wrap.name) != 0:
            return "%spublic float %s" % (indent(depth), parser_wrap.name)
        else:
            return "float"
    elif parser_wrap.get_type_name() == "list":
        memeber = gen_member(parser_wrap.subs[0], depth)
        if len(parser_wrap.name) != 0:
            return "%spublic %s<%s> %s" % (indent(depth), "List", memeber, parser_wrap.name)
        else:
            return "%s<%s>" % ("List", memeber)
    elif parser_wrap.get_type_name() == "dict":
        memeber = gen_member(parser_wrap.subs[1], depth)
        if len(parser_wrap.name) != 0:
            return "%spublic %s<string, %s> %s" % (indent(depth), "Dictionary", memeber, parser_wrap.name)
        else:
            return "%s<string, %s>" % ("Dictionary", memeber)
    elif parser_wrap.get_type_name() == "t":
        if len(parser_wrap.name) != 0:
            return "%spublic %s %s" % (indent(depth), uid(parser_wrap), parser_wrap.name)
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


