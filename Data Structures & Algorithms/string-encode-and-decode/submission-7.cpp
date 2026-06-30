class Solution {
public:

    string encode(vector<string>& strs) {
        vector<int> length_tracker;
        string encoded = "";
        for(string& s:strs){
            length_tracker.push_back(s.size());
            encoded += to_string(s.size()) + "#" + s;
        }
        cout << encoded;
        return encoded;
    }

    vector<string> decode(string s) {
        vector<string> res;
        int encoded_length = s.size();
        if (encoded_length == 0){
            return res;
        }
        int number, index = 0, word_index = 0;
        string num = "", word = "";
        
        while(index < encoded_length){
            word = "";
            if (s[index] == '#'){
                number = stoi(num);
                index += 1;
                for(word_index = 0; word_index < number; word_index++){
                    word += s[index + word_index];
                }
                res.push_back(word);
                index += word_index;
                num = "";
            } else {
                num += s[index];
                index += 1;
            }
        }
        return res;
        
    }
};
