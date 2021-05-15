class Solution {
    public boolean isPalindrome(int x) {
        StringBuilder rev = new StringBuilder(Integer.toString(x));
        return rev.toString().equals(rev.reverse().toString());
    }
}
