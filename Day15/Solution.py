def insert(head, data):
    new_node = Node(data)
    if head is None:
        head = new_node
    else:
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
    return head


class Solution:
    pass
