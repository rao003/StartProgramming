import dataclasses, math, typing

@dataclasses.dataclass
class Vektor:
    x: float = 0.0
    y: typing.Any = 0.0

    def betrag(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

va = Vektor(3.0, 4.5)
vb = Vektor(3.0, 4.0)
va.y = 4.0
if va == vb:
    print("Vektoren sind gleich")
print(va)
print("Betrag:", va.betrag())

vc = Vektor(1.8)
print(vc)

vd = Vektor(y=9.1)
print(vd)
