## 概述
这是一个由Python实现，将excel数据格式转换为json数据格式的工具，具有以下特点：
* 扩展性强
* 实现简洁，代码量少
* 操作简单，执行极快
* 支持多种类型，适用范围广
* 支持任意层数数据结构嵌套
* 支持输出多种语言的结构信息，以便于语法补全和序列化支持

## 支持类型
| 类型    | 语法       | 示例                 |
| -----   | ---------- | -------------------- |
| int     | int        | int        var_name  |
| str     | str        | str        var_name  |
| bool    | bool       | bool       var_name  |
| float   | float      | float      var_name  |
| list<T> | [T]        | [i]        var_name  |
| dict<T> | {T}        | {i}        var_name  |
| struct  | <T a, U b> | <i a, f b> var_name  |


## 使用方法
1. 安装python3：[python官网](https://www.python.org/)
2. 安装openpyxl：控制台输入 `pip install openpyxl`
3. 参考`Example/export.py`示例或直接使用`Example/export.py`

## 示例
### 示例1
* 输入excel信息 *(表名demo0)*

| i a | f b | b c | s d |
| --- | --- | --- | --- |
| 0	  | 0   | 0   | "你好1" |
| 1   | 1   | 1   | "你好2" |
| 2   | 0   | 0   | "你好3" |

* 输出json信息
```Json
{
"0": {"a": 0, "b": 0, "c": false, "d": "你好1"},
"1": {"a": 1, "b": 1, "c": true, "d": "你好2"},
"2": {"a": 2, "b": 0, "c": false, "d": "你好3"}
}
```

* 输出C#结构信息
```C#
public class demo0
{
    public int a;
    public float b;
    public bool c;
    public string d;
};
```

* 输出C++结构信息
```C++
struct demo0
{
    int a;
    float b;
    bool c;
    std::string d;
};
```

### 示例2
* 输入excel内容 *(表名demo1)*

|i a | [i] b     | {f} c                    | <i vint, s vstr, f vfloat, b vbool> d | [<i a, f b>] e |
| -- | --------- | ------------------------ | ------------------------------------- | -------------- |
| 0	 | [0, 1, 2] | {"a": 0, "b": 1, "c": 2} | <1, "1", 1, 1>                        | [<0, 1>]       |
| 1  | [0, 1, 2] | {"a": 0, "b": 1, "c": 2} | <1, "1", 1, 1>                        | [<0, 1>]       |
| 2  | [0, 1, 2] | {"a": 0, "b": 1, "c": 2} | <1, "1", 1, 1>                        | [<0, 1>]       |

* 输出json信息
```Json
{
"0": {"a": 0, "b": [0, 1, 2], "c": {"a": 0, "b": 1, "c": 2}, "d": {"vint": 1, "vstr": "1", "vfloat": 1, "vbool": true}, "e": [{"a": 0, "b": 1}]},
"1": {"a": 1, "b": [0, 1, 2], "c": {"a": 0, "b": 1, "c": 2}, "d": {"vint": 1, "vstr": "1", "vfloat": 1, "vbool": true}, "e": [{"a": 0, "b": 1}]},
"2": {"a": 2, "b": [0, 1, 2], "c": {"a": 0, "b": 1, "c": 2}, "d": {"vint": 1, "vstr": "1", "vfloat": 1, "vbool": true}, "e": [{"a": 0, "b": 1}]}
}
```

* 输出C#结构信息
```C#
public class demo1
{
    public class __1876340187152__
    {
        public int vint;
        public string vstr;
        public float vfloat;
        public bool vbool;
    };
    public class __1876325246288__
    {
        public int a;
        public float b;
    };
    public int a;
    public List<int> b;
    public Dictionary<string, float> c;
    public __1876340187152__ d;
    public List<__1876325246288__> e;
};
```

* 输出C++结构信息
```C++
struct demo1
{
    struct __1876340187152__
    {
        int vint;
        std::string vstr;
        float vfloat;
        bool vbool;
    };
    struct __1876325246288__
    {
        int a;
        float b;
    };
    int a;
    std::vector<int> b;
    std::map<std::string, float> c;
    __1876340187152__ d;
    std::vector<__1876325246288__> e;
};
```