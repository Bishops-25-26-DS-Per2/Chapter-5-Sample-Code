class SimpleClass:
    def __init__(self, x: int, y: int, s: str):
        # To make self.x read-only, use self._x to store its value.
        self._x = x
        self.y = y
        self.s = s
    def __str__(self) -> str:
        return f"SimpleClass({self.x}, {self.y}, '{self.s}')"
    def __repr__(self) -> str:
        return self.__str__()
    # Use Case #1 for @property: Make self.x read-only.
    # So the method x takes the place of the attribute x.
    # The property decorator makes the method accessible using 
    #   attribute notation.
    @property
    def x(self):
        return self._x
    # Use Case #2 for @property: Make a computed attribute.
    # So this allows you to create something that behaves like an attribute
    #   that isn't actually an attribute.
    # As it is, this attribute is read-only also.
    # So, this allows the code to behave like the way the human would think 
    #   about the code -- this is really an attribute of the object, so let 
    #   the code behave like an attribute.
    @property
    def sum(self):
        return self.x + self.y

class Circle:
    def __init__(self, radius: float):
        self.radius = float(radius)
    # Essentially a computed attribute; self.r matches self.radius
    @property
    def r(self) -> float:
        return self.radius
    
    # Use Case #3: Validation of input
    @property
    def radius(self) -> float:
        return self._radius

    # This allows us to change the value of radius
    # Notice: the method has the same name as the one above!! Weird.
    # So now you can be sure that you have a non-negative float value for
    #   the radius.
    @radius.setter
    def radius(self, new_radius: float) -> None:
        if new_radius < 0:
            msg = "Dude. Don't make a negative radius.  Bad form."
            raise ValueError(msg)
        self._radius = new_radius

def main():
    c1 = Circle(5)
    print(c1.radius)
    print(c1.r)

if __name__ == "__main__":
    main()