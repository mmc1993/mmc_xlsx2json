#include <string>
#include <vector>
#include <map>

namespace demo::config {
    struct demo0
    {
        int a;
        float b;
        bool c;
        std::string d;
    };
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
    struct demo2
    {
        int a;
        float b;
        bool c;
        std::string d;
    };
}