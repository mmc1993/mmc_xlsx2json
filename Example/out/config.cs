#include <vector>
#include <map>

namespace config {
    struct Sheet1 {
        struct __2189022310416__ {
            bool b;
            float n;
            string s;
        };
        struct __2189021229200__ {
            bool b;
            float n;
            string s;
        };
        struct __2189029249680__ {
            bool b;
            float n;
            string s;
        };
        struct __2189029260624__ {
            bool b;
            float n;
            string s;
        };
        struct __2189029245520__ {
            __2189029260624__ t;
        };
        float id;
        bool b;
        float n;
        string s;
        std::vector<bool> b_list;
        std::vector<float> n_list;
        std::vector<string> s_list;
        std::map<string, bool> b_dict;
        std::map<string, float> n_dict;
        std::map<string, string> s_dict;
        __2189022310416__ t;
        std::vector<__2189021229200__> t_list;
        std::vector<std::map<string, float>> d_list;
        std::map<string, __2189029249680__> t_dict;
        __2189029245520__ t_type;
    };
}