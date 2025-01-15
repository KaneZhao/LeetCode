class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int row = matrix.length, col = matrix[0].length;
        int [] res = new int[row * col];
        int i = 0, j = 0, cur = 0;
        while (true) {
            while (j < col - 1 && matrix[i][j + 1] != 101) {
                res[cur++] = matrix[i][j];
                matrix[i][j++] = 101;
            }
            while (i < row - 1 && matrix[i + 1][j] != 101) {
                res[cur++] = matrix[i][j];
                matrix[i++][j] = 101;
            }
            while (j > 0 && matrix[i][j - 1] != 101) {
                res[cur++] = matrix[i][j];
                matrix[i][j--] = 101;
            }
            while (i > 0 && matrix[i - 1][j] != 101) {
                res[cur++] = matrix[i][j];
                matrix[i--][j] = 101;
            }
            if (cur == row * col - 1) {
                break;
            }
        }
        res[cur] = matrix[i][j];
        return Arrays.stream(res).boxed().collect(Collectors.toList());
    }
}