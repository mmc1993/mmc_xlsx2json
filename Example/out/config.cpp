#include <string>
#include <vector>
#include <map>

namespace config {
    struct Sheet1 {
        struct __2148925449936__ {
            bool b;
            float n;
            std::string s;
        };
        struct __2148911181200__ {
            bool b;
            float n;
            std::string s;
        };
        struct __2148925459920__ {
            bool b;
            float n;
            std::string s;
        };
        struct __2148925457104__ {
            bool b;
            float n;
            std::string s;
        };
        struct __2148925471888__ {
            __2148925457104__ t;
        };
        float id;
        bool b;
        float n;
        std::string s;
        std::vector<bool> b_list;
        std::vector<float> n_list;
        std::vector<std::string> s_list;
        std::map<std::string, bool> b_dict;
        std::map<std::string, float> n_dict;
        std::map<std::string, std::string> s_dict;
        __2148925449936__ t;
        std::vector<__2148911181200__> t_list;
        std::vector<std::map<std::string, float>> d_list;
        std::map<std::string, __2148925459920__> t_dict;
        __2148925471888__ t_type;
    };
}