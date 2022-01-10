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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = None
        if list1 and list2:
            if list1.val < list2.val:
                merged = ListNode(list1.val, None)
                if list1:
                    list1 = list1.next
            else:
                merged = ListNode(list2.val, None)
                if list2:
                    list2 = list2.next
        elif list1:
            merged = ListNode(list1.val, None)
            if list1:
                list1 = list1.next
        elif list2:
            merged = ListNode(list2.val, None)
            if list2:
                list2 = list2.next
        else:
            return merged
        temp = merged
        while True:
            if list1 and list2:
                if list1.val < list2.val:
                    temp.next = ListNode(list1.val, None)
                    if list1:
                        list1 = list1.next
                else:
                    temp.next = ListNode(list2.val, None)
                    if list2:
                        list2 = list2.next

            elif list1:
                temp.next = ListNode(list1.val, None)
                if list1:
                    list1 = list1.next
            elif list2:
                temp.next = ListNode(list2.val, None)
                if list2:
                    list2 = list2.next
            else:
                break
            temp = temp.next
        return merged


if __name__ == '__main__':
    l1 = ListNode()
    l2 = ListNode()
    l1.list_to_linked(ast.literal_eval(input()))
    l2.list_to_linked(ast.literal_eval(input()))
    s = Solution()
    result = s.mergeTwoLists(l1, l2)
    print(result)
