from package1.one import One
from package2.two import Two

def printXY():
    print("printXY(): basba")
    one = One()
    two = Two()    


def main():
    print("START MAIN form ./main.py")
    printXY()

if __name__ == "__main__":
    main()