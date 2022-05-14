class Matrix:
    value: list
    def __init__(self, value:list):
        self.value = value
    def __add__(self, other: 'Matrix'):
        try:
            rowsCount = len(self.value)
            itemsCount = len(self.value[0])
            newValue= [
                [
                    self.value[row][idx] + other.value[row][idx]
                    for idx in range(itemsCount)
                ]
                for row in range(rowsCount)
            ]
            return Matrix(newValue)
        except IndexError:
            print("Error")
            exit(1)
    def __str__(self):
        return "\n".join(
            str(row).strip('[]').replace(',', '')
            for row in self.value
        )
a = Matrix([
    [31, 22, 3],
    [37, 43, 2],
    [51, 86, 1]
])
b = Matrix([
    [5, 32, 3],
    [4, 6, 8],
    [64, 8, 5]
])
c = a + b
print(c)

