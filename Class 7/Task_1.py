class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return "\n".join([" ".join([str(i) for i in row]) for row in self.data])

    def __add__(self, other):
        # проверяем, что матрицы имеют одинаковый размер
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Матрицы должны иметь одинаковый размер")

        # складываем матрицы поэлементно
        result = [[self.data[row][col] + other.data[row][col]
                   for col in range(len(self.data[0]))]
                  for row in range(len(self.data))]
        return Matrix(result)

# пример использования
data1 = [[1, 2], [3, 4]]
data2 = [[5, 6], [7, 8]]
m1 = Matrix(data1)
m2 = Matrix(data2)
print(m1 + m2)
