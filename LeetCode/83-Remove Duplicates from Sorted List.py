import ast
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def list_to_linked(self, l):
        self.val = l[0]
        temp = self
        for i in range(1, len(l)):
            temp.next = ListNode(l[i], None)
            temp = temp.next
        return self

    def __str__(self):
        string_list = []
        temp = self
        while temp is not None:
            string_list.append(temp.val)
            temp = temp.next
        return str(string_list)


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while True:
            if not temp or not temp.next:
                break
            while temp.val == temp.next.val:
                temp.next = temp.next.next
                if not temp or not temp.next:
                    break
            else:
                temp = temp.next
        return head


if __name__ == '__main__':
    l1 = ListNode()
    l1.list_to_linked(ast.literal_eval(input()))
    s = Solution()
    print(s.deleteDuplicates(l1))
