/**
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */

class Solution {
    //  PLAN
    // # 1. Find the middle node and split in half
    // # 2. Reverse the second half
    // # 3. Merge the second list with the first list

    // # REMEMBER: Odd, middle. Even, second middle. Middle is part of second list
    // # HENCE: [1, 2, 3, 4] -> [1, 4, 2, 3] and [1, 2, 3, 4, 5] -> [1, 5, 2, 4, 3]

    // # EDGE CASES:
    // # 1. Singleton list

    // # Time: O(n). Space: O(1)
    fun reorderList(head: ListNode?): Unit {
        var slow = head
        var fast = head?.next

        while (fast != null && fast?.next != null) {
            slow = slow?.next
            fast = fast?.next?.next
        }

        val middle = slow?.next
        slow?.next = null

        var prev: ListNode? = null
        var curr = middle

        while (curr != null) {
            val temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        }

        var dummy: ListNode? = ListNode(-1)
        var node: ListNode? = dummy

        var first = head
        var second = prev

        while (first != null && second != null) {
            var first_next = first?.next
            var second_next = second?.next

            node?.next = first
            node = node?.next

            node?.next = second
            node = node?.next

            first = first_next
            second = second_next
        }

        node?.next = if (first != null) first else second
    }
}
