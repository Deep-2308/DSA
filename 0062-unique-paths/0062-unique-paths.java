class Solution {
    // Function to solve the problem using space optimization
    int func(int m, int n) {
        // Array for the previous row
        int[] prev = new int[n];

        // Iterate through rows
        for (int i = 0; i < m; i++) {
            // Array for the current row
            int[] temp = new int[n];

            for (int j = 0; j < n; j++) {
                // Base case
                if (i == 0 && j == 0) {
                    temp[j] = 1;
                    continue;
                }

                // Ways from above and left
                int up = (i > 0) ? prev[j] : 0;
                int left = (j > 0) ? temp[j - 1] : 0;

                // Total ways for current cell
                temp[j] = up + left;
            }

            // Update previous row
            prev = temp;
        }
        return prev[n - 1];
    }

    // Function to count total ways
    public int uniquePaths(int m, int n) {
        return func(m, n);
    }
}

// Separate main class
public class Main {
    public static void main(String[] args) {
        int m = 3;
        int n = 2;

        // Create Solution object
        Solution sol = new Solution();

        // Call and print result
        System.out.println("Number of ways: " + sol.uniquePaths(m, n));
    }
}