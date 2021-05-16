import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

class Solution {
    //递归实现
    public List<Integer> lexicalOrder(int n) {
        List<Integer> res = new ArrayList<>();
        for(int i = 1; i <= 9; i++){
            dfs(res, i, n);
        }
        return res;
    }
    public void dfs(List<Integer> res, int i, int n){
        if(i > n)
            return;
        res.add(i);
        for(int j = 0; j <= 9; j++){
            dfs(res,i*10+j,n);
        }
    }

    //用栈实现
    public List<Integer> lexicalOrder1(int n) {
        List<Integer> res = new ArrayList<>();
        Stack<Integer> stack = new Stack<>();
        for(int i = Math.min(n,9); i > 0; i--){
            stack.push(i);//保证数据的从小到大排序在进栈时从大到小进
        }
        while(!stack.isEmpty()){
            int x = stack.pop();
            res.add(x);
            for(int i = 9; i >=0; i--){
                if(x*10+i <= n){//保证数据的从小到大排序在进栈时从大到小进
                    stack.push(x*10+i);
                }
            }
        }
        return res;
    }
}
