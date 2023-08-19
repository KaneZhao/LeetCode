/**
 * 
 * Given the head of a linked list, remove the nth node from the end of the list and return its head.
 */

 /**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode start = head, end = head, pre = dummy;
        int i = 1;
        while (end.next != null) {
            if (i < n) {
                i++;
            } else {
                start = start.next;
                pre = pre.next;
            }
            end = end.next;
        } 
        pre.next = start.next;
        return dummy.next;
    }
}