class MySeq:
    def __init__(self, n):
        self.n = n

    def __getitem__(self, item):
        if isinstance(item, int):
            if item > self.n:
                raise IndexError
            return item * 10
        if isinstance(item, slice):
            result = []
            start = item.start or 0
            stop = item.stop or self.n + 1
            step = item.step or 1
            for i in range(start, stop, step):
                result.append(i*10)
            return result
        raise TypeError

    def __len__(self):
        return self.n


x = MySeq(10)
print(x[5])
print(x[2:5])
print(x[2::])
print(x[::])

