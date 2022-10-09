"""entrainement à l'app1
"""
import math
from random import randint
from ppoint import PPoint

class Point:
    """un Point à deux coordonnées
    """
    def __init__(self, abscisse, ordonnee):
        """constructeur de Point

        Parameters
        ----------
        abscisse : float
            abscisse
        ordonnee : float
            ordonnee
        """
        self.abscisse = abscisse
        self.ordonnee = ordonnee

    def falls_in_rectangle(self, rectangle):
        """le point fait-il partie d'un rectangle ?

        Parameters
        ----------
        rectangle: Rectangle
            le rectangle à comparer
        """
        return bool(rectangle.lowleft.abscisse < self.abscisse < rectangle.upright.abscisse \
        and rectangle.lowleft.ordonnee < self.ordonnee < rectangle.upright.ordonnee)

    def distance(self, point):
        """Calcule la distance du point courant à un autre point dont
        les coordonnées sont passées en argument

        Parameters
        ----------
        abscisse_autre : int
            abscisse de l'autre point
        ordonnee_autre : int
            ordonnee de l'autre point
        """
        ecart_abscisses = (self.abscisse - point.abscisse)**2
        ecart_ordonnees = (self.ordonnee - point.ordonnee)**2
        return math.sqrt(ecart_abscisses + ecart_ordonnees)

class Rectangle:
    """classe Rectangle défini en deux points
    """
    def __init__(self, lowleft, upright):
        """construit un rectangle

        Parameters
        ----------
        lowleft : Point
            point en bas à gauche du rectangle
        upright : Point
            point en haut à droite du rectangle
        """
        self.lowleft = lowleft
        self.upright = upright

    def area(self):
        """_summary_
        """
        return (math.fabs( self.upright.abscisse - self.lowleft.abscisse) * (math.fabs(self.upright.ordonnee - self.lowleft.ordonnee)))

class Person:
    """classe Personne avec un nom et un age
    """
    def __init__(self, name, age):
        """_summary_

        Parameters
        ----------
        name : str
            nom
        age : int
            age
        """
        self.name = name
        self.age =age



point1 = Point(10, 20)
print(type(point1))

point2 = PPoint(1, 2)
print(type(point2))
print(point1.abscisse)
person1 = Person("John", 65)
print(type(person1))
print(person1.name)

point3 = Point(3, 4)
print(point1.distance(point3))
rectanglex = Rectangle(Point(5,6), Point(7,9))
print(point3.falls_in_rectangle(rectanglex))

rectangle_int = Rectangle(Point(randint(0,9), randint(0, 9)),
                          Point(randint(10, 19),  randint(10, 19)))

print("Rectangle Coordinates: ",
      rectangle_int.lowleft.abscisse, ",",
      rectangle_int.lowleft.ordonnee, " and ",
      rectangle_int.upright.abscisse, ",",
      rectangle_int.upright.ordonnee)

user_point = Point(float(input("Guess X: ")),
                   float(input("Guess Y: ")))
user_area  =float(input("Guess rectangle area: "))

print("Your point was inside rectangle: ",
      user_point.falls_in_rectangle(rectangle_int))
print("Your area was off by: ",
      rectangle_int.area() - user_area)
