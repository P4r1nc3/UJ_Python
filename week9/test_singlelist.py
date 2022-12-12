from singlelist import SingleList, Node

def test_insert_head():
    list = SingleList()
    list.insert_head(Node(1))
    list.insert_head(Node(2))
    list.insert_head(Node(3))

    assert list.head.data == 3
    assert list.head.next.data == 2
    assert list.tail.data == 1
    assert list.tail.next == None
    assert list.length == 3

def test_insert_tail():
    list = SingleList()
    list.insert_tail(Node(1))
    list.insert_tail(Node(2))
    list.insert_tail(Node(3))

    assert list.head.data == 3
    assert list.head.next.data == 2
    assert list.tail.data == 3
    assert list.tail.next == None
    assert list.length == 3

def test_remove_head():
    list = SingleList()
    list.insert_head(Node(1))
    list.insert_head(Node(2))
    list.insert_head(Node(3))

    assert list.remove_head().data == 3
    assert list.length == 2
    assert list.remove_head().data == 2
    assert list.length == 1
    assert list.remove_head().data == 1
    assert list.length == 0

def test_remove_tail():
    list = SingleList()
    list.insert_tail(Node(1))
    list.insert_tail(Node(2))
    list.insert_tail(Node(3))
   
    assert list.remove_tail().data == 3
    assert list.length == 2
    assert list.remove_tail().data == 2
    assert list.length == 1
    assert list.remove_tail().data == 1
    assert list.length == 0

def test_join():
    list1 = SingleList()
    list1.insert_tail(Node(1))
    list1.insert_tail(Node(2))
    list1.insert_tail(Node(3))

    list2 = SingleList()
    list2.insert_tail(Node(4))
    list2.insert_tail(Node(5))
    list2.insert_tail(Node(6))
    list1.join(list2)

    assert list2.count() == 0

    for i in range(1, 7):
        assert list1.remove_head().data == i

def test_clear():
    list = SingleList()
    list.insert_tail(Node(1))
    list.insert_tail(Node(2))
    list.insert_tail(Node(3))
    list.clear()
    
    assert list.head is None
    assert list.tail is None
    assert list.count() == 0