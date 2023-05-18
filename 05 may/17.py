from typing import Optional


#
#
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
#     count = 0
#     while head.next:
#         count += 1
#
#     return head[count // 2:]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def leafSimilar(root1: list, root2: list) -> bool:
    pass


# head = [1, 2, 3, 4, 5]
# head = ListNode([1, 2, 3, 4, 5, 6])

# print(middleNode(head))

root1 = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
root2 = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]

print(leafSimilar(root1, root2))
