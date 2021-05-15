class Solution {
    public int myAtoi(String s) {
        int ans = 0;
        int factor = 1;
        int end = 0;
        s = s.trim();
        if (s.length() == 0) {
            return 0;
        }
        if (s.charAt(0) == '-') {
            factor = -1;
        }
        if (s.charAt(0) == '-' || s.charAt(0) == '+') {
            s = s.substring(1);
        }
        if (s.length() == 0) {
            return 0;
        }
        while (s.length() > 0 && s.charAt(0) == '0') {
            s = s.substring(1);
        }
        for (int i = 0; i < s.length(); i++) {
            if (Character.isDigit(s.charAt(i))) {
                end++;
            } else {
                break;
            }
        }
        if (end == 0) {
            return 0;
        }
        long mid = 0L;
        if (end > 10) {
            if (factor > 0) {
                return Integer.MAX_VALUE;
            } else {
                return Integer.MIN_VALUE;
            }
        }
        mid = Long.parseLong(s.substring(0, end));
        if (mid > Math.pow(2, 31) && factor < 0) {
            ans = Integer.MIN_VALUE;
        } else if (mid > Math.pow(2, 31) - 1 && factor > 0) {
            ans = Integer.MAX_VALUE;
        } else {
            ans = (int) (factor * mid);
        }
        return ans;
    }
}
