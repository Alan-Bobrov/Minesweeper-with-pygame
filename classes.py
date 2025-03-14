from random import randint

class Field:
    dict_hards = {
        "Beginner" : (9, 9, 10),
        "Intermediate" : (16, 16, 40),
        "Expert" : (30, 16, 99)
    }

    def __init__(self, hard) -> None:
        self.hard = hard
        self.num_mines = self.dict_hards[hard][2]
        self.colums_num = self.dict_hards[hard][1]
        self.rows_num = self.dict_hards[hard][0]
        field =  [[Position(0, 0, "None", "None") for __ in range(self.rows_num)]]
        field += [[Position(0, 0, "None", "None")] + [Position(X, Y) for X in range(self.rows_num)] + [Position(0, 0, "None", "None")] for Y in range(self.colums_num)]
        field += [[Position(0, 0, "None", "None") for __ in range(self.rows_num)]]
        self.field = field


    def setting_mines(self) -> None: #Need to change, look normal
        for _ in range(self.num_mines):
            while True:
                X = randint(1, self.rows_num)
                Y = randint(1, self.colums_num)
                if self.field[Y][X].status == "free":
                    self.field[Y][X].symbol = " M"
                    self.field[Y][X].status = "mine"
                    break

    def open_something(self, find_status, new_status) -> None:  #Need to change, look normal
        changes = 0
        while True:
            for i in range(1, self.L_and_W[1] + 1):
                for j in range(1, self.L_and_W[0] + 1):
                    if self.field[i][j].status == find_status:
                        list_places = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1)]
                        list_places.extend([(i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)])

                        for item in list_places:
                            if self.field[item[0]][item[1]].status == "open":
                                self.field[i][j].status = new_status
                                changes += 1
                                break
            if changes == 0:
                break
            changes = 0

    def count_near_mines(self) -> None: #Need to do
        pass
    
    def print_field_console(sefl, status=True) -> None: #Need to do
        pass

    def test_win(self) -> bool: #Need to change, look normal
        for i in self.field:
            for j in i:
                if j.status in ("free", "num"):
                    return False
        return True

    def move(self, first_move=False) -> str: #Need to do
        pass

class Position:
    def __init__(self, X, Y, status="free", symbol="  ") -> None: #Maybe need to change
        self.X = X
        self.Y = Y
        self.status = status
        self.symbol = symbol

    def actions_positions(self): #Need to do
        pass

f = Field(hard="Expert")
f.setting_mines()
for i in f.field:
    for j in i:
        print(j.symbol, end="   ")
    print()