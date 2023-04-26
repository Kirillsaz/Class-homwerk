class Cell:
    def __init__(self, cells_num):
        self.cells_num = cells_num

    def __add__(self, other):
        return Cell(self.cells_num + other.cells_num)

    def __sub__(self, other):
        if self.cells_num - other.cells_num &gt; 0:
            return Cell(self.cells_num - other.cells_num)
        else:
            print("Ошибка. Разность клеток не может быть отрицательной.")

    def __mul__(self, other):
        return Cell(self.cells_num * other.cells_num)

    def __truediv__(self, other):
        return Cell(self.cells_num // other.cells_num)

    def make_order(self, cells_in_row):
        row = "*" * cells_in_row
        rows, remainder = divmod(self.cells_num, cells_in_row)
        result = row * rows + "*" * remainder
        return "\n".join([result[i:i+cells_in_row] for i in range(0, len(result), cells_in_row)])
