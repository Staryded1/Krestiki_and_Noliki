from rich.console import Console
from rich.table import Table

console = Console()


def show():
    # Отображение текущего состояния игрового поля
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()

def ask():
    # Получение координат от пользователя
    while True:
        cords = input("         Ваш ход: ").split()
        
        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue
        
        x, y = cords
        
        if not(x.isdigit()) or not(y.isdigit()):
            print(" Введите числа! ")
            continue
        
        x, y = int(x), int(y)
        
        if 0 > x or x > 2 or  0 > y or  y > 2 :
            print(" Координаты вне диапазона! ")
            continue
        
        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue
        
        return x, y

def check_win():
    # Проверка на победу
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            return "X"
        if symbols == ["0", "0", "0"]:
            return "0"
    return None

def print_winner_combination(combination):
    table = Table(title="Победная комбинация")
    for i, row in enumerate(field):
        new_row = []
        for j, value in enumerate(row):
            if (i, j) in combination:
                new_row.append(f"[green]{value}[/green]")
            else:
                new_row.append(value)
        table.add_row(*new_row)
    console.print(table)

def play():
    # Основной игровой цикл
    count = 0
    while True:
        count += 1
        show()
        if count % 2 == 1:
            print(" Ходит крестик!")
        else:
            print(" Ходит нолик!")
        
        x, y = ask()
        
        if count % 2 == 1:
            field[x][y] = "X"
        else:
            field[x][y] = "0"
        
        winner = check_win()
        if winner:
            show()
            print(f"Выиграл {winner}!!!")
            break
        
        if count == 9:
            show()
            print(" Ничья!")
            break

# Начало игры

field = [[" "] * 3 for i in range(3)]
play()