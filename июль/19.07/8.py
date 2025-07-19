class Triangle:
    def __init__(self, height1, height2, width):
        self.height1 = height1
        self.height2 = height2
        self.width = width


    @property
    def perimetr(self):
        return self.height1 + self.height2 + self.width


class Equ_triangle(Triangle):
    def __init__(self, height1):
        super().__init__(height1, height1, height1)


fig1 = Triangle(4,4,6)
fig2 = Equ_triangle(6)

print(fig1.perimetr)
print(fig2.perimetr)

