try:
    class square:
        def __init__(self, side):
            self.side = side
        def place(self):
            return self.side * self.side
        def perimeter(self):
            return 4 * self.side

    myobj = square(int(input("¬ведите сторону первого квадрата\n")))
    myobj2 = square(int(input("¬ведите сторону второго квадрата\n")))
    print(f"ѕлощадь первого квадрата = {myobj.place()}")
    print(f"ѕериметр второго квадрата = {myobj2.perimeter()}") #вообще метод, обьект и класс
    # стоило бы называть square, тк обьект - квадрат, класс - квадрат, площадь - переводитс€ также как "квадрат",
    # но это не нагл€дно
except ValueError:
    print("¬ведено не число")