try:
    class square:
        def __init__(self, side):
            self.side = side
        def place(self):
            return self.side * self.side
        def perimeter(self):
            return 4 * self.side

    myobj = square(int(input("������� ������� ������� ��������\n")))
    myobj2 = square(int(input("������� ������� ������� ��������\n")))
    print(f"������� ������� �������� = {myobj.place()}")
    print(f"�������� ������� �������� = {myobj2.perimeter()}") #������ �����, ������ � �����
    # ������ �� �������� square, �� ������ - �������, ����� - �������, ������� - ����������� ����� ��� "�������",
    # �� ��� �� ��������
except ValueError:
    print("������� �� �����")