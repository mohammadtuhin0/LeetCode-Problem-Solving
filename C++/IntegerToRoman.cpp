#include <iostream>
#include <string.h>
#include <unordered_map>
using namespace std;
int main(){
    class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> value = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };

        int result = 0; 

        for (int i = 0; i < s.size(); i++) {
            int current = value[s[i]];

            if (i + 1 < s.size()) {
                int next = value[s[i + 1]];

                if (current < next)
                    result -= current;
                else
                    result += current;
            } 
            else {
                result += current;
            }
        }

        return result;
    }
};

}