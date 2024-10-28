from .one import One
from package2.two import Two

def printXY():
    print("printXY(): START")
    one = One()
    two = Two()


def main():
    print("START MAIN form ./resources/main.py")
    printXY()

if __name__ == "__main__":
    print(f"{__name__=} {__file__=} {__package__=}")
    main()