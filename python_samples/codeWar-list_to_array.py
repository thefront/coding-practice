def list_to_array(lst):
    result = []
    item = lst
    """
    print item.value
    result.append(item.value)

    item = item.next
    print item.value
    result.append(item.value)

    item = item.next
    print item.value
    result.append(item.value)
    """
    while item is not None:
        result.append(item.value)
        item = item.next
    return result

# Test cases
u = None
Test.assert_equals(list_to_array(u), [])

u = LinkedList(4, LinkedList(25, LinkedList(30)))
Test.assert_equals(list_to_array(u), [4, 25, 30])

u = LinkedList(2, LinkedList(40, LinkedList(43, LinkedList(25, LinkedList(125)))))
Test.assert_equals(list_to_array(u), [2, 40, 43, 25, 125])

# clever
def list_to_array(lst):
    return ([lst.value] + list_to_array(lst.next)) if lst else []
