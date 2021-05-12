class Solution {
    public String longestPalindrome(String s) {

        int i = 0;
        String res = "";
        while (i < s.length()) {
            int index = i;
            while (index < s.length() - 1 && s.charAt(index) == s.charAt(index + 1)) {
                index += 1;
            }
            int[] k = extend(i, index, s.length(), s);
            int a = k[0], b = k[1];
            if (b - a + 1 > res.length()) {
                res = s.substring(a, b + 1);
            }
            i = index + 1;
        }
        return res;
    }

    public int[] extend(int start, int end, int n, String s) {
        while (start >= 1 && end < n - 1) {
            if (s.charAt(start - 1) == s.charAt(end + 1)) {
                start--;
                end++;
            } else {
                break;
            }
        }
        return new int[]{start, end};
    }
}
