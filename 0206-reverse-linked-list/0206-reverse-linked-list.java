/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    public ListNode reverseList(ListNode head) {

        // Previous node (initially null)
        ListNode prev = null;

        // Current node starts from head
        ListNode current = head;

        // Traverse the entire list
        while (current != null) {

            // Save the next node
            ListNode next = current.next;

            // Reverse the current node's pointer
            current.next = prev;

            // Move prev one step forward
            prev = current;

            // Move current one step forward
            current = next;
        }

        // prev becomes the new head
        return prev;
    }
}