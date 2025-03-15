from random import randint

class Field:
    # num X, num Y, num mines
    dict_hards = { 
        "1 Beginner" : (9, 9, 10),
        "2 Intermediate" : (16, 16, 40),
        "3 Expert" : (30, 16, 99)
    }

    def __init__(self, hard) -> None: # done
        self.hard = hard
        for key in self.dict_hards.keys():
            if str(hard) in key.split():
                self.num_mines = self.dict_hards[key][2]
                self.Y_num = self.dict_hards[key][1]
                self.X_num = self.dict_hards[key][0]
                self.free_flag_num = self.dict_hards[key][2]
        field =  [[Cell(0, 0, "None", "None") for __ in range(self.X_num + 2)]]
        field += [[Cell(0, 0, "None", "None")] + [Cell(X, Y) for X in range(self.X_num)] + [Cell(0, 0, "None", "None")] for Y in range(self.Y_num)]
        field += [[Cell(0, 0, "None", "None") for __ in range(self.X_num + 2)]]
        self.field = field


    def setting_mines(self) -> None: #done
        for _ in range(self.num_mines):
            while True:
                X = randint(1, self.X_num)
                Y = randint(1, self.Y_num)
                if self.field[Y][X].status == "free":
                    self.field[Y][X].symbol = "M"
                    self.field[Y][X].status = "mine"
                    break

    def open_something(self, finding_status, new_status) -> None:  #Meybe done, look normal
        changes = 0
        while True:
            for Y in range(1, self.Y_num + 1):
                for X in range(1, self.X_num + 1):
                    if self.field[Y][X].status == finding_status:
                        list_near_cells = ([X - 1, Y - 1], [X, Y - 1], [X + 1, Y - 1], [X - 1, Y], [X + 1, Y], [X - 1, Y + 1], [X, Y + 1], [X + 1, Y + 1])

                        for cell in list_near_cells:
                            if self.field[cell[1]][cell[0]].status == "open":
                                self.field[Y][X].status = new_status
                                changes += 1
                                break
            if changes == 0:
                break
            changes = 0

    def count_near_mines(self) -> None: #done
        for Y in range(1, self.Y_num + 1):
            for X in range(1, self.X_num + 1):
                if self.field[Y][X].status != "mine":
                    list_near_cells = ([X - 1, Y - 1], [X, Y - 1], [X + 1, Y - 1], [X - 1, Y], [X + 1, Y], [X - 1, Y + 1], [X, Y + 1], [X + 1, Y + 1])
                    count_near_mine = 0
                    for cell in list_near_cells:
                        if self.field[cell[1]][cell[0]].status == "mine":
                            count_near_mine += 1
                    self.field[Y][X].status = "num"
                    self.field[Y][X].symbol = str(count_near_mine)
    
    def print_field_console(self, status=False) -> None: #done
        if status:
            for Y in range(1, self.Y_num + 1):
                for X in range(1, self.X_num + 1):
                    print(self.field[Y][X].status, end=" ")
                print()
        else:
            for Y in range(1, self.Y_num + 1):
                for X in range(1, self.X_num + 1):
                    print(self.field[Y][X].symbol, end=" ")
                print()

    def test_win(self) -> bool: #Need to change, look normal
        for i in self.field:
            for j in i:
                if j.status in ("free", "num"):
                    return False
        return True

    def move(self, X, Y, first_move=False) -> str: #Need to do
        if first_move:
            self.field[Y][X].status = "open"
            self.field[Y][X].sumbol = " "

            list_near_cells = ([X - 1, Y - 1], [X, Y - 1], [X + 1, Y - 1], [X - 1, Y], [X + 1, Y], [X - 1, Y + 1], [X, Y + 1], [X + 1, Y + 1])
            for cell in list_near_cells:
                if self.field[Y][X].status != "None":
                    self.field[Y][X].status = "open"
                    self.sumbol = " "
        else:


class Cell:
    def __init__(self, X, Y, status="free", symbol="  ") -> None: #Maybe need to change
        self.X = X
        self.Y = Y
        self.status = status
        self.symbol = symbol

    def actions_with_cells(self): #Need to do
        pass

f = Field(hard=1)
f.setting_mines()
f.count_near_mines()
f.print_field_console()
# CTRL + /