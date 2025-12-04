import pickle

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

def main():
    instances = read_data()
    print(instances)


if __name__ == "__main__":
    main()