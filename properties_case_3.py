class Circle:
    # This is a *class* attribute. Python will also make a copy of
    #   each class attribute into each instance.
    PI = 3.14159265358979

    def __init__(self, radius: float):
        self.radius = radius

    # Essentially a computed attribute; self.r matches self.radius
    @property
    def r(self) -> float:
        return self.radius
    
    # Use Case #3: Validation of input
    @property
    def radius(self) -> float:
        return self._radius

    # Computed attribute that gives an alternate route to the data
    @property
    def circumference(self) -> float:
        return self.radius * self.PI * 2

    # By using self.radius instead of self._radius, we call the setter
    #   for radius, which means that this will call the validation code
    #   that we wrote for the setter method.
    @r.setter
    def r(self, new_r: float) -> None:
        self.radius = new_r

    # This allows us to change the value of radius
    # Notice: the method has the same name as the one above!! Weird.
    # So now you can be sure that you have a non-negative float value for
    #   the radius.
    @radius.setter
    def radius(self, new_radius: float) -> None:
        if new_radius < 0:
            msg = "Dude. Don't make a negative radius.  Bad form."
            raise ValueError(msg)
        self._radius = float(new_radius)

    @circumference.setter
    def circumference(self, new_circumference: float) -> None:
        self.radius = new_circumference / (2*self.PI)

    @classmethod
    def from_circumference(cls, circumference: float) -> 'Circle':
        """Class methods are often used as alternate constructors.
        
        Notice that cls refers to the class."""
        radius = circumference / (2*cls.PI)
        return Circle(radius)

    # Can also do @staticmethod if you'd like.

def main():
    c1 = Circle(5)
    print(c1.radius)
    print(c1.r)
    c1.circumference = 42
    print(c1.r)
    c2 = Circle.from_circumference(811)
    print(c2.radius)

if __name__ == "__main__":
    main()