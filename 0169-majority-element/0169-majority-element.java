import java.util.*;

// Class containing the majority element logic
class Solution {
    // Function to find the majority element in an array
    public int majorityElement(int[] nums) {
        // Size of the given array
        int n = nums.length;
        
        // Count variable
        int cnt = 0;
        
        // Candidate element
        int el = 0;
        
        // Step 1: Find the potential majority element
        for (int i = 0; i < n; i++) {
            if (cnt == 0) {
                cnt = 1;
                el = nums[i];
            } else if (el == nums[i]) {
                cnt++;
            } else {
                cnt--;
            }
        }
        
        // Step 2: Verify the candidate
        int cnt1 = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] == el) {
                cnt1++;
            }
        }
        
        // Return the element if it's a majority
        if (cnt1 > (n / 2)) {
            return el;
        }
        
        // No majority found
        return -1;
    }
}

// Separate Main class for execution
public class Main {
    public static void main(String[] args) {
        int[] arr = {2, 2, 1, 1, 1, 2, 2};
        
        // Create an instance of Solution class
        Solution sol = new Solution();

        // Call the majorityElement function
        int ans = sol.majorityElement(arr);
        
        // Print the majority element
        System.out.println("The majority element is: " + ans);
    }
}
