import math

class Figure:
    '''The class it's used for implemet the lessthan method __lt__ equal for all figures'''
    def __init__(self, sortType = 'a'):
        if sortType != 'a' and sortType != 'p':
            raise Exception('Invalid argument: sortType must be a or p, default = a')
        self._sortType = sortType

    def __lt__(self, other):
        if self._sortType == 'p':
            return self.calculate_perimeter() < other.calculate_perimeter()
        else:
            return self.calculate_area() < other.calculate_area()

class RegularPoligon(Figure):
    def __init__(self, l, sortType = 'a'):
        super().__init__(sortType)
        self._lato = l
        self._height = (l/2) / math.tan( math.pi/self._n )

    def calculate_area(self):
        return self._n * self._lato * self._height / 2

    def calculate_perimeter(self):
        return self._lato * self._n

class Pentagon(RegularPoligon):
    def __init__(self, l, sortType = 'a'):
        self._n = 5
        super().__init__(l, sortType = 'a')

class Hexagon(RegularPoligon):
    def __init__(self, l, sortType = 'a'):
        self._n = 6
        super().__init__(l, sortType = 'a')

class EquiTriangle(Figure):
    def __init__(self, l, sortType = 'a'):
        super().__init__(sortType)
        self._lato = l
        self._height = (l**2 - (l/2)**2)**(0.5)

    def calculate_area(self):
        return self._lato * self._height / 2

    def calculate_perimeter(self):
        return self._lato * 3

class Circle(Figure):
    def __init__(self, r, sortType = 'a'):
        super().__init__(sortType)
        self._radius = r

    def calculate_area(self):
        return math.pi * self._radius**2

    def calculate_perimeter(self):
        return 2 * math.pi * self._radius

class Rectangle(Figure):
    def __init__(self, a, b, sortType = 'a'):
        super().__init__(sortType)
        self._l1 = a
        self._l2 = b

    def calculate_area(self):
        return self._l1 * self._l2

    def calculate_perimeter(self):
        return 2*self._l1 + 2*self._l2

class Square(Rectangle):
    def __init__(self, l, sortType = 'a'):
        super().__init__(l, l, sortType)

class OrderedElements:

    def __init__(self, l):
        self.cache = sorted(l)

    def __iter__(self):
        self.cache_index = -1
        self.cache_max = len(self.cache) - 1
        return self

    def __next__(self):
        self.cache_index += 1

        if self.cache_index > self.cache_max:
            raise StopIteration

        return self.cache[self.cache_index]