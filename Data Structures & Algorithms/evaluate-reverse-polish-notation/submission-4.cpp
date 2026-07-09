class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        vector<int> stack;
        int left, right;
        for(auto& num: tokens){
            if ((num != "+") && (num != "-") && (num != "*") && (num != "/")){
                stack.push_back(stoi(num));
            } else {
                right = stack.back();
                stack.pop_back();
                left = stack.back();
                stack.pop_back();
                if (num == "+") {
                    stack.push_back(left + right);
                } else if (num == "-") {
                    stack.push_back(left - right);
                } else if (num == "*"){
                    stack.push_back(left * right);
                } else {
                    bool neg = false;
                    if ((left > 0 and right < 0) or (left < 0 and right > 0))
                        neg = true;
                    int quo = abs(left) / abs(right);
                    if (neg){
                        stack.push_back(-quo);
                    } else {
                        stack.push_back(quo);
                    }
                }
            }
        }
        return stack.back();
    }
};
