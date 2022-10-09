"""_summary_
"""

from ppoint import PPoint

class Point:
    """_summary_
    """
    def __init__(self, abscisse, ordonnee):
        """_summary_

        Parameters
        ----------
        abscisse : _type_
            _description_
        ordonnee : _type_
            _description_
        """
        self.abscisse = abscisse
        self.ordonnee = ordonnee

    def falls_in_rectangle(self, lowleft, upright):
        """_summary_

        Parameters
        ----------
        lowleft : _type_
            _description_
        upright : _type_
            _description_
        """
        if lowleft[0] < self.abscisse < upright[0] \
        and lowleft[1] < self.ordonnee < upright[1]:
            return True
        else:
            return False

class Rectangle:
    """_summary_
    """
    def __init__(self, point_a, point_b):
        """_summary_

        Parameters
        ----------
        point_a : int
            _description_
        point_b : int
            _description_
        """
        self.point_a = point_a
        self.point_b = point_b

point1 = Point(10, 20)
print(type(point1))

point2 = PPoint(1, 2)
print(type(point2))
print(point1.abscisse)


class Person:
    """_summary_
    """
    def __init__(self, name, age):
        """_summary_

        Parameters
        ----------
        name : _type_
            _description_
        age : _type_
            _description_
        """
        self.name = name
        self.age =age

person1 = Person("John", 65)
print(type(person1))
print(person1.name)

point3 = Point(3, 4)
print(point3.falls_in_rectangle((5,6),(7,9)))