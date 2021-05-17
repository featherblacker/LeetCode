import java.util.Arrays;

//超时
class Solution {
    int[] start;
    int[] end;
    int numOfRoutes = 0;

    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        this.start = new int[]{0, 0};
        this.end = new int[]{obstacleGrid.length - 1, obstacleGrid[0].length - 1};
        if (obstacleGrid[start[0]][start[1]] == 1){
            return 0;
        }
        findWays(obstacleGrid, start);

        return numOfRoutes;
    }

    public void findWays(int[][] obstacleGrid, int[] position) {

        if (Arrays.equals(position, end)) {
            numOfRoutes++;
            return;
        }
        if ((obstacleGrid[0].length > position[1] + 1) && obstacleGrid[position[0]][position[1] + 1] != 1) {
            position[1]++;
            findWays(obstacleGrid, position);
            position[1]--;
        }
        if ((obstacleGrid.length > position[0] + 1) && obstacleGrid[position[0] + 1][position[1]] != 1) {
            position[0]++;
            findWays(obstacleGrid, position);
            position[0]--;
        }
    }

    public static void main(String[] args) {
        Solution a = new Solution();
        System.out.println(a.uniquePathsWithObstacles(new int[][]{{1, 0}}));
    }
}


class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int n = obstacleGrid.length, m = obstacleGrid[0].length;
        int[] f = new int[m];

        f[0] = obstacleGrid[0][0] == 0 ? 1 : 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (obstacleGrid[i][j] == 1) {
                    f[j] = 0;
                    continue;
                }
                if (j - 1 >= 0 && obstacleGrid[i][j - 1] == 0) {
                    f[j] += f[j - 1];
                }
            }
        }
        
        return f[m - 1];
    }
}
