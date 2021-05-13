import java.util.List;

class Solution {
    public String convert(String s, int numRows) {
        int cycle = numRows * 2 - 2;
        if (cycle == 0){
            return s;
        }
        int times = Math.floorDiv(s.length(), cycle);
        if (s.length() % cycle != 0) {
            times++;
        }
        s = s.concat("0".repeat(times * cycle - s.length()));
        String ans = "";
        for (int i = 0; i < numRows; i++) {
            for (int k = 0; k < times; k++) {
                if (i == 0 || i == numRows - 1) {
                    ans = ans.concat(String.valueOf(s.charAt(i + k * cycle)));
                } else {
                    ans = ans.concat(String.valueOf(s.charAt(i + k * cycle)) + String.valueOf(s.charAt(cycle - i + k * cycle)));
                }
            }
        }
        ans = ans.replace("0", "");
        return ans;
    }
}
