class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> map = new HashMap<>();
        Stack<Character> stack = new Stack<>();
        map.put(')', '(');
        map.put(']', '['); 
        map.put('}', '{');
        for (int i = 0; i < s.length(); i++){
            if ("({[".indexOf(s.charAt(i)) != -1){
                stack.push(s.charAt(i));
            } else {
                if (stack.isEmpty() || map.get(s.charAt(i)) != stack.peek()) {
                    return false;
                } else {
                    stack.pop();
                }
            }
        } 
        return stack.isEmpty();     
    }
}