public class NQueensFixed {
    
    public static void printBoard(int[][] board, int n) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(board[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }

    
    public static boolean isSafe(int[][] board, int row, int col, int n) {
        for (int i = 0; i < row; i++) {
            if (board[i][col] == 1)
                return false;
        }

        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 1)
                return false;
        }

        for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {
            if (board[i][j] == 1)
                return false;
        }

        return true;
    }


    public static boolean solveNQueens(int[][] board, int row, int n) {
        
        if (row == n) {
            System.out.println("Final N-Queens Matrix:");
            printBoard(board, n);
            return true;
        }


        for (int col = 0; col < n; col++) {
            if (isSafe(board, row, col, n)) {
                board[row][col] = 1; 
                if (solveNQueens(board, row + 1, n)) {
                    return true;
                }
                board[row][col] = 0; 
            }
        }

        return false;
    }

    
    public static void main(String[] args) {
        int n = 4;
        int firstRow = 0;
        int firstCol = 1;

        int[][] board = new int[n][n];

        // Place first queen manually
        board[firstRow][firstCol] = 1;

        // Start solving from next row
        boolean success = solveNQueens(board, firstRow + 1, n);

        if (!success) {
            System.out.println("No solution possible with this first queen position.");
        }
    }
}
