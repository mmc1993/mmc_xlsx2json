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
        struct __2278458827664__
        {
            int vint;
            std::string vstr;
            float vfloat;
            bool vbool;
        };
        struct __2278458633488__
        {
            int a;
            float b;
        };
        int a;
        std::vector<int> b;
        std::map<std::string, float> c;
        __2278458827664__ d;
        std::vector<__2278458633488__> e;
    };
    struct demo2
    {
        int a;
        float b;
        bool c;
        std::string d;
    };
}