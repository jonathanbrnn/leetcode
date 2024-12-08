#include <map>
#include <functional>
#include <iostream>

using namespace std; 

template <typename Key, typename Value>
class DefaultDict {
    private: 
        std::map<Key, Value> data; 
        std::function<Value()> default_factory; 
    
    public: 
        DefaultDict(std::function<Value()> factory) : default_factory(factory) {};
        Value& operator[](const Key& key) {
            if (data.find(key) == data.end()) {
                data[key] = default_factory();
            }
            return data[key];
        }

        const std::map<Key, Value>& get_data() const {
            return data;
        }
        
};

class Solution {
public:
    char repeatedCharacter(std::string s) {
        DefaultDict<char, int> dict([]() {return 0;} );

        for(int i = 0; i < s.size(); i++)
        {
            dict[s[i]]++; 
            if(dict[s[i]] == 2) {return s[i];}
        } 
        return 'j'; 
    }
};