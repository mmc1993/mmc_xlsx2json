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
        struct __2345451679056__ {
            int vint;
            std::string vstr;
            float vfloat;
            bool vbool;
        };
        struct __2345412524240__ {
            int a;
            float b;
        };
        int a;
        std::vector<int> b;
        std::map<std::string, float> c;
        __2345451679056__ d;
        std::vector<__2345412524240__> e;
    };
    struct demo2 {

        int a;
        float b;
        bool c;
        std::string d;
    };
}