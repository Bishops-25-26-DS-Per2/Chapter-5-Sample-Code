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

def main():
    a = SimpleClass(7, 11, "Amy")
    print(a)
    print(a.sum)
    a.y = 114
    print(a)
    print(a.sum)
    # This should fail.
    a.x = -13
    print(a)

if __name__ == "__main__":
    main()