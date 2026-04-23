[engineering tool.py](https://github.com/user-attachments/files/27022138/engineering.tool.py)
class rectangle:
    def __init__(self):
        self.a: float = float(input("what is the length: "))
        self.b: float = float(input("what is the width: "))
        self.area: float = self.a * self.b

    def calculation_rectangle(self):
        self.xg: float = self.a / 2
        self.yg: float = self.b / 2
        self.s_xx: float = (self.b * self.a**3) / 12
        self.s_yy: float = (self.a * self.b**3) / 12
        self.I_xx: float = self.s_xx + (self.area * self.yg**2)
        self.I_yy: float = self.s_yy + (self.area * self.xg**2)
        self.I_ox: float = self.I_xx - (self.area * self.yg**2)
        self.I_oy: float = self.I_yy - (self.area * self.xg**2)
        return {
            "shape": "rectangle",
            "area": self.area,
            "xg": self.xg,
            "yg": self.yg,
            "s_xx": self.s_xx,
            "s_yy": self.s_yy,
            "I_xx": self.I_xx,
            "I_yy": self.I_yy,
            "I_ox": self.I_ox,
            "I_oy": self.I_oy,
        }


class circle:
    def __init__(self):
        self.r: float = float(input("what is the radius: "))
        self.area: float = 3.14 * self.r**2

    def calculation_circle(self):
        self.xg: float = 0
        self.yg: float = 0
        self.s_xx: float = (3.14 * self.r**4) / 4
        self.s_yy: float = (3.14 * self.r**4) / 4
        self.I_xx: float = self.s_xx + (self.area * self.yg**2)
        self.I_yy: float = self.s_yy + (self.area * self.xg**2)
        self.I_ox: float = self.I_xx - (self.area * self.yg**2)
        self.I_oy: float = self.I_yy - (self.area * self.xg**2)
        return {
            "shape": "circle",
            "area": self.area,
            "xg": self.xg,
            "yg": self.yg,
            "s_xx": self.s_xx,
            "s_yy": self.s_yy,
            "I_xx": self.I_xx,
            "I_yy": self.I_yy,
            "I_ox": self.I_ox,
            "I_oy": self.I_oy,
        }


class triangle:
    def __init__(self):
        self.ab: float = float(input("what is the base: "))
        self.bc: float = float(input("what is the height: "))
        self.ac: float = float(input("what is the hypotenuse: "))
        self.area: float = 0.5 * self.ab * self.bc

    def calculation_triangle(self):
        if self.ab != self.ac and self.bc != self.ac:
            self.xg: float = self.ab / 3
            self.yg: float = self.bc / 3
            self.s_xx: float = (self.ab * self.bc**3) / 36
            self.s_yy: float = (self.bc * self.ab**3) / 36
        elif self.ab == self.ac:
            self.xg: float = self.ab / 2
        elif self.bc == self.ac:
            self.yg: float = self.bc / 2
        self.I_xx: float = self.s_xx + (self.area * self.yg**2)
        self.I_yy: float = self.s_yy + (self.area * self.xg**2)
        self.I_ox: float = self.I_xx - (self.area * self.yg**2)
        self.I_oy: float = self.I_yy - (self.area * self.xg**2)
        return {
            "shape": "triangle",
            "area": self.area,
            "xg": self.xg,
            "yg": self.yg,
            "s_xx": self.s_xx,
            "s_yy": self.s_yy,
            "I_xx": self.I_xx,
            "I_yy": self.I_yy,
            "I_ox": self.I_ox,
            "I_oy": self.I_oy,
        }


def get_Calculation():
    if decision == "rectangle":
        obj = rectangle()
        return obj.calculation_rectangle()
    elif decision == "circle":
        obj = circle()
        return obj.calculation_circle()
    elif decision == "triangle":
        obj = triangle()
        return obj.calculation_triangle()


decision = input("what is the shape: ")
result = get_Calculation()
import pandas as pd

if result:
    df = pd.DataFrame([result])
    print(df)
