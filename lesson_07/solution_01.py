"""Используя условие первой задачи из урока, проверить то же самое только для коней."""

def is_f_b_e_o(x1, y1, x2, y2):
    if abs(x1-x2) == 1 and abs(y1-y2) == 2 or abs(x1-x2) == 2 and abs(y1-y2) == 1:
        return True
    return False

def main():
    x1 = int(input("enter x1"))
    y1 = int(input("enter y1"))
    x2 = int(input("enter x2"))
    y2 = int(input("enter y2"))

    if is_f_b_e_o (x1, y1, x2, y2):
        print ("yes")
    else:
        print("no")

if __name__ == "__main__":
    main()