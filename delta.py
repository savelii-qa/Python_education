class Delta:
    def __init__(self, side1, side2, side3):

        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

        if type(side1) != int or type(side2) != int or type(side3) != int:
            raise TypeError("Incorrect type")
        elif side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError("Value can not be less or equal 0")
        else:
            side1 + side2 < side3 and side1 + side2 < side3 and side2 + side3 < side1
            raise TypeError("Triangle not exist")

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def area(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        a = (p * (p - self.side1) * (p - self.side2) * (p - self.side3)) ** 0.5
        if a == 0:
            return "Error, incorrect sides values"
        else:
            return a

    def type(self):
        sides_tuple = (self.side1, self.side2, self.side3)
        sides_tuple_sorted = sorted(sides_tuple)
        hypotenuse = int(sides_tuple_sorted[2])
        katet1 = int(sides_tuple_sorted[1])
        katet2 = int(sides_tuple_sorted[0])
        if hypotenuse ** 2 == (katet2 ** 2) + (katet1 ** 2):
            return "Triangle is rectangular"
        elif self.side1 == self.side2 == self.side3:
            return "Triangle is equilateral"
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return "Triangle is isosceles"
        else:
            return "Triangle is versatile"


tr1 = Delta(1, 1, 1)
print(tr1.perimeter())
# assert tr1.perimeter() == 6, "Should be 6"

tr2 = Delta(4, 5, 3)
print(tr2.area())
# assert tr2.area() == 6.0, "Should be 6.0"

tr3 = Delta(3, 4, 5)
print(tr3.type())
# assert tr3.type() == "Triangle is rectangular"

tr3 = Delta(4, 4, 4)
print(tr3.type())
# assert tr3.type() == "Triangle is equilateral"

tr3 = Delta(4, 4, 5)
print(tr3.type())
# assert tr3.type() == "Triangle is isosceles"

tr3 = Delta(1, 2, 3)
print(tr3.type())
# assert tr3.type() == "Triangle is versatile"
