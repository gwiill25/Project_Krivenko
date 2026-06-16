#Создайте класс «Матрица», который имеет атрибуты количества строк и столбцов. 
#Добавьте методы для сложения, вычитания и умножения матриц.class Matrix:
class Matritsa:
    def __init__(self, stroki, stolbtsy, dannye=None):
        self.stroki, self.stolbtsy = stroki, stolbtsy
        self.dannye = dannye if dannye else [[0] * stolbtsy for _ in range(stroki)]

    def vyvesti(self):
        [print(row) for row in self.dannye]

    def _check_size(self, other):
        if self.stroki != other.stroki or self.stolbtsy != other.stolbtsy:
            raise ValueError("Размеры матриц не совпадают")

    def slozhit(self, other):
        self._check_size(other)
        return Matritsa(self.stroki, self.stolbtsy, 
                       [[self.dannye[i][j] + other.dannye[i][j] for j in range(self.stolbtsy)] for i in range(self.stroki)])

    def vychest(self, other):
        self._check_size(other)
        return Matritsa(self.stroki, self.stolbtsy, 
                       [[self.dannye[i][j] - other.dannye[i][j] for j in range(self.stolbtsy)] for i in range(self.stroki)])

    def umnozit(self, other):
        if self.stolbtsy != other.stroki:
            raise ValueError("Число столбцов первой != числу строк второй")
        return Matritsa(self.stroki, other.stolbtsy,
                       [[sum(self.dannye[i][k] * other.dannye[k][j] for k in range(self.stolbtsy)) for j in range(other.stolbtsy)] for i in range(self.stroki)])

if __name__ == "__main__":
    m1 = Matritsa(2, 2, [[1, 2], [3, 4]])
    m2 = Matritsa(2, 2, [[5, 6], [7, 8]])
    
    print("Матрица 1:"); m1.vyvesti()
    print("\nМатрица 2:"); m2.vyvesti()
    print("\nСложение:"); m1.slozhit(m2).vyvesti()
    print("\nВычитание:"); m1.vychest(m2).vyvesti()
    print("\nУмножение:"); m1.umnozit(m2).vyvesti()
    
    m3 = Matritsa(2, 3, [[1, 2, 3], [4, 5, 6]])
    m4 = Matritsa(3, 2, [[7, 8], [9, 10], [11, 12]])
    print("\nУмножение 2x3 * 3x2 = 2x2:"); m3.umnozit(m4).vyvesti()