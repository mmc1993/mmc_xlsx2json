#include <string>
#include <vector>
#include <map>

namespace config {
    struct demo0 {

        int a;
        float b;
        bool c;
        std::string d;
    };
    struct demo1 {
        struct __1846230013392__ {
            int vint;
            std::string vstr;
            float vfloat;
            bool vbool;
        };
        struct __1846263117328__ {
            int a;
            float b;
        };
        int a;
        std::vector<int> b;
        std::map<std::string, float> c;
        __1846230013392__ d;
        std::vector<__1846263117328__> e;
    };
    struct demo2 {

        int a;
        float b;
        bool c;
        std::string d;
    };
}