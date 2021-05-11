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
}
