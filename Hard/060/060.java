import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

class Solution {
    String ans = "";
    List<Integer> res;

    public String getPermutation(int n, int k) {
        res = new ArrayList<>();
        for (int i = 1; i < n + 1; i++) {
            res.add(i);
        }
        getRes(n, k, res);
        return ans;
    }

    public void getRes(int n, int k, List<Integer> res) {
        if (n == 0) {
            return;
        }
        if (k == 1) {
            ans = ans.concat(res.stream()
                    .map(Object::toString)
                    .collect(Collectors.joining("")));
            return;
        }
        int times = factorial(res.size() - 1);
        for (int i = 1; i < res.size() + 1; i++) {
            if (times * i > k-1) {
                ans = ans.concat(Integer.toString(res.get(i - 1)));
                res.remove(i - 1);
                getRes(n - 1, k - times * (i - 1), res);
                break;
            }
        }
    }

    public int factorial(int num) {
        if (num <= 1) {
            return 1;
        } else {
            return num * factorial(num - 1);
        }
    }

    public static void main(String[] args) {
        Solution a = new Solution();
        System.out.println(a.getPermutation(4, 9));
    }
}
