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
        struct __1286102216592__
        {
            int vint;
            std::string vstr;
            float vfloat;
            bool vbool;
        };
        struct __1286094064784__
        {
            int a;
            float b;
        };
        int a;
        std::vector<int> b;
        std::map<std::string, float> c;
        __1286102216592__ d;
        std::vector<__1286094064784__> e;
    };
    struct demo2 
    {
        int a;
        float b;
        bool c;
        std::string d;
    };
}