class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0, r = s.size();
        unsigned char lc, rc;
        while(l < r){
            lc = static_cast<unsigned char>(s[l]);
            while (l < r && !std::isalnum(lc)){
                l++;
                lc = static_cast<unsigned char>(s[l]);
            }
            rc = static_cast<unsigned char>(s[r]);
            while (l < r && !isalnum(rc)){
                r--;
                rc = static_cast<unsigned char>(s[r]);
            }
            if (l < r && tolower(lc) != tolower(rc)){
                return false;
            }
            l++;r--;
        }
        return true;
    }
};
