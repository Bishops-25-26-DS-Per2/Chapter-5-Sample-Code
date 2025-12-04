import pickle
import atexit

@atexit.register
def save_my_data() -> None:
    save_data(instances)

class SimpleClass:
    def __init__(self, x: int, y: int, s: str):
        self.x = x
        self.y = y
        self.s = s
    def __str__(self) -> str:
        return f"SimpleClass({self.x}, {self.y}, '{self.s}')"
    def __repr__(self) -> str:
        return self.__str__()

def save_data(data: list) -> None:
    with open("saved_data.dat", "wb") as datafile:
        pickle.dump(data, datafile)

def read_data() -> list:
    with open("saved_data.dat", "rb") as datafile:
        data = pickle.load(datafile)
    return data

instances = [SimpleClass(42, 24, "Jackson"), SimpleClass(17, 111, "Emma")]
x = 4/0
print(instances)
