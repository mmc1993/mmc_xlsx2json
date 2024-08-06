#include <string>
#include <vector>
#include <map>

namespace config {
    struct demo0 
    {
        int a;
        float b;
        bool c;
        std::string d;
    };
    struct demo1 
    {
        struct __2811434835984__
        {
            int vint;
            std::string vstr;
            float vfloat;
            bool vbool;
        };
        struct __2811420222800__
        {
            int a;
            float b;
        };
        int a;
        std::vector<int> b;
        std::map<std::string, float> c;
        __2811434835984__ d;
        std::vector<__2811420222800__> e;
    };
    struct demo2 
    {
        int a;
        float b;
        bool c;
        std::string d;
    };
}