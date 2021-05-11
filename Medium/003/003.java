import java.util.ArrayList;
import java.util.List;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        List<Character> list = new ArrayList<>();
        int maxLength = 0;
        for (int i = 0; i < s.length(); i++) {
            Character character = s.charAt(i);
            if (!list.contains(character)){
                list.add(character);
                maxLength = Integer.max(list.size(), maxLength);
            }else{
                int index = list.indexOf(character);
                list = list.subList(index+1, list.size());
                list.add(character);
            }
        }
        return maxLength;
    }
    
    public int lengthOfLongestSubstring2(String s) {
        Set<Character> set = new HashSet<>();
        int maxLength = 0;
        int right = 0;
        for (int i = 0; i < s.length(); i++) {
            if (right!=0){
                set.remove(s.charAt(i-1));
            }
            while (right<s.length() &&!set.contains(s.charAt(right))){
                set.add(s.charAt(right));
                right++;
            }
            maxLength = Math.max(maxLength, right-i);

        }
        return maxLength;
    }
}
