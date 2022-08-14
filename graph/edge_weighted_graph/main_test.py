import pytest
import edge
import graph

def test_testing():
    assert True

def test_edge_create():
    e = edge.Edge(0, 1, 0.5)
    ##
    assert e.v == 0
    assert e.w == 1
    assert e.weight == 0.5

def test_edge_either_other():
    e = edge.Edge(0, 1, 0.5)
    either = e.either()
    ##
    assert either == 0 or either == 1
    if either == 0:
        assert e.other(either) == 1
    if either == 1:
        assert e.other(either) == 0

def test_edge_compare():
    e1 = edge.Edge(0, 1, 0.5)
    e2 = edge.Edge(0, 1, 0.5)
    e3 = edge.Edge(0, 1, 0.6)
    ##
    assert e1.compare_to(e2) == 0
    assert e1.compare_to(e3) == -1
    assert e3.compare_to(e1) == 1


def test_graph_create():
    g = graph.Graph(4)
    ##
    assert g.V == 4
    assert g.E() == 0
    assert g.adjacent_of(0) == []
    assert g.edges == []


def test_graph_add_edge():
    g = graph.Graph(4)
    e = edge.Edge(0, 1, 0.5)
    g.add_edge(e)
    ##
    assert g.V == 4
    assert g.E() == 1
    assert g.adjacent_of(0) == [e]
    assert g.edges == [e]
    assert g.adjacent_of(1) == [e]
    assert g.edges == [e]