# coding=utf-8

def clsid(obj):
    return "__%d__" % id(obj)

#   生成字符串
def indent(count):
    return "".join(" " for i in range(count * 4))

def to_type(namespace, key_words_lut, body_template, file_struct_wraps):
    body = "\n".join([gen_from_file(key_words_lut,          \
                                    file_struct_wrap[0],    \
                                    file_struct_wrap[1])
        for file_struct_wrap in file_struct_wraps])
    return body_template % (namespace, body)

def collect_struct(parser_wrap, result):
    for sub in parser_wrap.subs:
        collect_struct(sub, result)
    if parser_wrap.get_type_name() == "t":
        result.append(parser_wrap)

def gen_from_file(key_words_lut, file_struct_name, file_struct_parser_wraps):
    file_struct_parser_wraps = [file_struct_parser_wrap for file_struct_parser_wrap in \
                                file_struct_parser_wraps if file_struct_parser_wrap != None]

    struct_list = []
    for file_struct_parser_wrap in file_struct_parser_wraps:
        collect_struct(file_struct_parser_wrap, struct_list)

    struct_text = gen_structs(key_words_lut, struct_list, 2)
    member_text = gen_members(key_words_lut, file_struct_parser_wraps, 2)
    if len(struct_text) > 0: struct_text += "\n"
    format = "{0}{1}{2} {3} \n{0}{{\n{4}{5}\n{0}}};"
    return format.format(indent(1),                 \
                         key_words_lut["scope"],    \
                         key_words_lut["class"],    \
                         file_struct_name,          \
                         struct_text, member_text)

def gen_structs(key_words_lut, struct_list, depth):
    #   0 缩进
    #   1 class 作用域
    #   1 class 关键字
    #   2 类体
    #   3 类名
    format = "{0}{1}{2} {4}\n{0}{{\n{3}\n{0}}};"
    return "\n".join([
        format.format(indent(depth), 
        key_words_lut["scope"], key_words_lut["class"],         \
        gen_struct(parser_wrap, key_words_lut, depth + 1),      \
        clsid(parser_wrap)) for parser_wrap in struct_list])

def gen_struct(parser_wrap, key_words_lut, depth):
    return "".join(gen_members(key_words_lut, parser_wrap.subs, depth))

#   生成成员
def gen_member(key_words_lut, parser_wrap, depth):
    typekey = parser_wrap.get_type_name()
    if typekey == "i" \
    or typekey == "s" \
    or typekey == "b" \
    or typekey == "f":
        if len(parser_wrap.name) != 0:
            #   \t|public|type|name
            return "%s%s%s %s" % (indent(depth),            \
                                  key_words_lut["scope"],   \
                                  key_words_lut[typekey],   \
                                  parser_wrap.name)
        else:
            #   type
            return key_words_lut[typekey]
    elif typekey == "list":
        memeber = gen_member(key_words_lut, parser_wrap.subs[0], depth)
        if len(parser_wrap.name) != 0:
            #   \t|public|List|type|name
            return "%s%s%s<%s> %s" % (indent(depth),            \
                                      key_words_lut["scope"],   \
                                      key_words_lut[typekey],   \
                                      memeber, parser_wrap.name)
        else:
            #   List|type
            return "%s<%s>" % (key_words_lut[typekey], memeber)
    elif typekey == "dict":
        memeber = gen_member(key_words_lut, parser_wrap.subs[1], depth)
        if len(parser_wrap.name) != 0:
            #   \t|public|dict|type|name
            return "%s%s%s<%s, %s> %s" % (indent(depth),                \
                                              key_words_lut["scope"],   \
                                              key_words_lut[typekey],   \
                                              key_words_lut["s"], memeber, parser_wrap.name)
        else:
            #   dict|type
            return "%s<%s, %s>" % (key_words_lut[typekey], key_words_lut["s"], memeber)
    elif parser_wrap.get_type_name() == "t":
        if len(parser_wrap.name) != 0:
            #   \t|public|type|name
            return "%s%s%s %s" % (indent(depth), key_words_lut["scope"],   \
                                  clsid(parser_wrap), parser_wrap.name)
        else:
            #   type
            return "%s" % (clsid(parser_wrap))
    assert False, "类型解析错误: 未知类型 %s" % parser_wrap.type

def gen_members(key_words_lut, parser_wraps, depth):
    return "\n".join([gen_member(key_words_lut, parser_wrap, depth) + ";" for parser_wrap in parser_wraps])
