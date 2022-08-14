from MinBinaryHeap import MinBinaryHeap
import pytest


def test_init():
    heap = MinBinaryHeap()
    assert heap.size() == 0


def test_insert():
    heap = MinBinaryHeap()
    ##
    heap.insert(2, "A", "value")
    assert heap.size() == 1
    assert heap.map == {"A": 0}
    ##
    heap.insert(1, "B", "value")
    assert heap.size() == 2
    peek1 = heap.peek()
    assert peek1.__dict__ == {"key": 1,
                              "id": "B", "value": "value", "order": 1}
    assert heap.map == {"A": 1, "B": 0}
    ##
    heap.insert(0, "C", "value")
    peek2 = heap.peek()
    assert peek2.__dict__ == {"key": 0,
                              "id": "C", "value": "value", "order": 2}
    assert heap.map == {"A": 1, "B": 2, "C": 0}


# @pytest.mark.skip(reason="")
def test_pop():
    heap = MinBinaryHeap()
    heap.insert(2, "A", "value")
    heap.insert(1, "B", "value")
    heap.insert(0, "C", "value")
    ##
    pop1 = heap.pop()
    assert pop1.__dict__ == {"key": 0,
                             "id": "C", "value": "value", "order": 2}
    assert heap.size() == 2
    assert heap.map == {"A": 1, "B": 0}
    ##
    pop2 = heap.pop()
    assert pop2.__dict__ == {"key": 1,
                             "id": "B", "value": "value", "order": 1}
    assert heap.size() == 1
    assert heap.map == {"A": 0}
    ##
    pop3 = heap.pop()
    assert pop3.__dict__ == {"key": 2,
                             "id": "A", "value": "value", "order": 0}
    assert heap.size() == 0
    assert heap.map == {}


def test_pop_2():
    heap = MinBinaryHeap()
    heap.insert(0, "A", "value")
    result = heap.pop()
    assert heap.is_empty()
    assert result.__dict__ == {
        "key": 0, "id": "A", "value": "value", "order": 0}


def test_decrease_key():
    heap = MinBinaryHeap()
    heap.insert(2, "A", "value")
    heap.insert(5, "B", "value")
    heap.insert(1, "C", "value")
    heap.insert(17, "D", "value")

    assert heap.map == {"C": 0, "A": 2, "B": 1, "D": 3}

    heap.decrease_key("D", 0)
    assert heap.map == {"C": 1, "A": 2, "B": 3, "D": 0}


def test_exist():
    heap = MinBinaryHeap()
    heap.insert(2, "A", "value")
    heap.insert(5, "B", "value")
    heap.insert(1, "C", "value")
    heap.insert(17, "D", "value")

    assert heap.exist("A") == True
    assert heap.exist("B") == True
    assert heap.exist("C") == True
    assert heap.exist("D") == True
    assert heap.exist("E") == False
