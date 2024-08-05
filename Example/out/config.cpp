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
        struct __3147673060304__ {
            int vint;
            std::string vstr;
            float vfloat;
            bool vbool;
        };
        struct __3147673084048__ {
            int a;
            float b;
        };
        int a;
        std::vector<int> b;
        std::map<std::string, float> c;
        __3147673060304__ d;
        std::vector<__3147673084048__> e;
    };
    struct demo2 {

        int a;
        float b;
        bool c;
        std::string d;
    };
}