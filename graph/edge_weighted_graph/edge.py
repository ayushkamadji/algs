class Edge:
    def __init__(self, v: int, w: int, weight: float) -> None:
        self.v = v
        self.w = w
        self.weight = weight

    def either(self) -> int:
        return self.v

    def other(self, vertex: int) -> int:
        if vertex == self.v:
            return self.w
        else:
            return self.v

    def compare_to(self, that) -> int:
        if type(that) is not Edge:
            raise TypeError('type mismatch')  
        if self.weight < that.weight:
            return -1
        elif self.weight > that.weight:
            return 1
        else:
            return 0

    def to_string(self) -> str:
        return f'{self.v}->{self.w} {self.weight}'
