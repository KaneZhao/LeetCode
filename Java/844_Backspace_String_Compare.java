class Solution {
    public boolean backspaceCompare(String s, String t) {
        return helper(s).equals(helper(t));
    }

    private String helper(String str) {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == '#') {
                if (!stack.isEmpty()) {
                    stack.pop();
                }
            } else {
                stack.push(str.charAt(i));
            }
        }

        StringBuilder sb = new StringBuilder();
        for (Character ch : stack) {
            sb.append(ch);
        }
        String res = sb.toString();
        return res;
    }
}

// class Solution {
//     public boolean backspaceCompare(String s, String t) {
//         int i = s.length() - 1, j = t.length() - 1;
//         int cnts = 0, cntt = 0;
//         while (i >= 0 || j >= 0){
//             while (i >= 0 && (s.charAt(i) == '#' || cnts > 0)) {
//                 cnts += (s.charAt(i--) == '#') ? 1 : -1;
//             }
//             while (j >= 0 && (t.charAt(j) == '#' || cntt > 0)) {
//                 cntt += (t.charAt(j--) == '#') ? 1 : -1;
//             }
//             if (i < 0 || j < 0) return i == j;
//             if (s.charAt(i--) != t.charAt(j--)) return false;
//         }
//         return i == j;
//     }
// }