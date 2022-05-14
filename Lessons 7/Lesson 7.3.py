class Cell:
    __count: int
    def __init__(self, count: int):
        assert count > 0, "Надо больше 0!"
        self.__count = count
    def __add__(self, other: 'Cell'):
        self.validateItem(other)
        value = self.count + other.count
        return Cell(value)
    def __sub__(self, other: 'Cell'):
        self.validateItem(other)
        value = self.count - other.count
        assert value > 0, "Разница меньше 0!"
        return Cell(value)
    def __mul__(self, other: 'Cell'):
        self.validateItem(other)
        value = self.count * other.count
        return Cell(value)
    def __truediv__(self, other: 'Cell'):
        self.validateItem(other)
        value = round(self.count / self.count)
        return Cell(value)
    def __str__(self):
        return str(self.__count)
    def validateItem(self, other):
        assert isinstance(other, self.__class__), "только между клетками"
    @property
    def count(self) -> int:
        return self.__count
    @staticmethod
    def makeOrder(cellObj: 'Cell', countRow: int) -> str:
       items = '*' * cellObj.count
       chunks = [
           items[idx: idx + countRow]
           for idx in range(0, len(items), countRow)
       ]
       return '\n'.join(chunks)
first = Cell(5)
second = Cell(4)
huge = Cell(16)
print(first + second)
print(first - second)
print(first * second)
print(first / second)
print(Cell.makeOrder(huge, 5))
