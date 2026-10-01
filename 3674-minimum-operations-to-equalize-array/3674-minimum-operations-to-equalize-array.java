class Solution {
    public int minOperations(int[] nums) {
        /*
         * Idea:
         * - If all elements are already equal, no operation is needed.
         * - Otherwise, choose the entire array as the subarray.
         * - The bitwise AND of all elements is calculated.
         * - Replacing every element with this AND makes all elements equal.
         * - Therefore, at most 1 operation is always enough.
         *
         * So:
         * - All elements equal -> 0
         * - Otherwise -> 1
         *
         * Example:
         * [1,2]
         * 1 & 2 = 0
         * [1,2] -> [0,0]
         * Answer = 1
         *
         * Time Complexity: O(n)
         * Space Complexity: O(1)
         */

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[0]) {
                return 1;
            }
        }

        return 0;
    }
}