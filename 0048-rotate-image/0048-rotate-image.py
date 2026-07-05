"""
=========================================
Problem: 48. Rotate Image (Medium)
=========================================

CHEAT SHEET:
* Trigger: "Rotate an image/matrix by 90 degrees" and "in-place".
* Trap: Creating a second empty matrix to copy numbers into (violates the O(1) space constraint), 
        or trying to build complex mathematical formulas to calculate 4-way cell swaps.
* Mechanism: 
    1. Transpose: Swap matrix[i][j] with matrix[j][i]. 
       (CRITICAL: The inner loop must start at j = i + 1 to only scan the upper triangle, avoiding double-swapping).
    2. Reverse: Run .reverse() on every single row to flip the mirrored columns into their final clockwise position.

Complexity:
* Time: O(N^2) where N is the number of rows/cols.
* Space: O(1) strictly in-place modification.
=========================================
"""

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # Step 1: Transpose the matrix (Swap across the top-left to bottom-right diagonal)
        for i in range(n):
            # Start j at i + 1 to only process the upper right triangle
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse every row to complete the 90-degree clockwise rotation
        for i in range(n):
            matrix[i].reverse()

# ---------------------------------------
# Driver Code for Local / GitHub Testing
# ---------------------------------------
if __name__ == "__main__":
    # Test Case 1
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("--- Original Matrix ---")
    for row in matrix:
        print(row)
        
    # Execute Rotation
    obj = Solution()
    obj.rotate(matrix)
    
    print("\n--- Rotated Matrix ---")
    for row in matrix:
        print(row)