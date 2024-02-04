/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function(head) {
    let i = head, j = head, length = 0, counter = 1;
    
    while(i){
        i = i.next;
        length++
    }
    
    let mid = Math.floor(length/2);
    
    while(counter <= mid){
          j = j.next;
        counter++;
    }
    return j;
};