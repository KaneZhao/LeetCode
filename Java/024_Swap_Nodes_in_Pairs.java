/**
 * 
 * Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
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
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode pre = dummy;
        while (pre.next != null){
            if (pre.next.next != null) {
                ListNode cur = pre.next;
                pre.next = cur.next;
                cur.next = pre.next.next;
                pre.next.next = cur;
                pre = cur;
            } else {
                break;
            }           
        }    
        return dummy.next;         
    }
}