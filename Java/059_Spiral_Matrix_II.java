class Solution {
    public int[][] generateMatrix(int n) {
        int[][] res = new int[n][n];
        int i = 0, j = 0, num = 1;
        while (true) {
            while (j < n - 1 && res[i][j + 1] == 0){
                res[i][j++] = num++;
            }
            while (i < n - 1 && res[i + 1][j] == 0){
                res[i++][j] = num++;
            }
            while (j > 0 && res[i][j - 1] == 0){
                res[i][j--] = num++;
            }
            while (i > 0 && res[i - 1][j] == 0){
                res[i--][j] = num++;
            }
            if (num >= n * n){
                break;
            }             
        }
        res[i][j] = num;
        return res;
    }
}