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
    # Simple Example 1: Make self.x read-only
    # So the method x takes the place of the attribute x.
    # The property decorator makes the method accessible using 
    #   attribute notation.
    @property
    def x(self):
        return self._x

def main():
    a = SimpleClass(7, 11, "Amy")
    print(a)
    a.y = 114
    print(a)
    # This should fail.
    a.x = -13
    print(a)

if __name__ == "__main__":
    main()