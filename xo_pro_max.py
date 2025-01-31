#import
import random
#funtion
def update_playbook(The_playbook, player_1, player_2):
    # تحديث خلية اللاعب الأول
    if 1 <= player_1 <= 9:
        The_playbook[player_1 - 1] = "x"
    # تحديث خلية اللاعب الثاني
    if 1 <= player_2 <= 9:
        The_playbook[player_2 - 1] = "o"
    return The_playbook


def print_xo():
    a = The_playbook[0]
    b = The_playbook[1]
    c = The_playbook[2]
    d = The_playbook[3]
    f = The_playbook[4]
    g = The_playbook[5]
    h = The_playbook[6]
    p = The_playbook[7]
    o = The_playbook[8]

    print("",h, "|", p, "|", o)
    print("---+---+---")
    print("",d, "|", f, "|", g)
    print("---+---+---")
    print("",a, "|", b, "|", c)


def win_and_stop(The_playbook_after):
    win_for_o_or_x = "on_win"
    win_test = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "],
                [" ", " ", " "], [" ", " ", " "], [" ", " ", " "],
                [" ", " ", " "], [" ", " ", " "]]
    win_test[0] = [The_playbook_after[0], The_playbook_after[1], The_playbook_after[2]]
    win_test[1] = [The_playbook_after[3], The_playbook_after[4], The_playbook_after[5]]
    win_test[2] = [The_playbook_after[6], The_playbook_after[7], The_playbook_after[8]]
    win_test[3] = [The_playbook_after[0], The_playbook_after[3], The_playbook_after[6]]
    win_test[4] = [The_playbook_after[1], The_playbook_after[4], The_playbook_after[7]]
    win_test[5] = [The_playbook_after[2], The_playbook_after[5], The_playbook_after[8]]
    win_test[6] = [The_playbook_after[0], The_playbook_after[4], The_playbook_after[8]]
    win_test[7] = [The_playbook_after[2], The_playbook_after[4], The_playbook_after[6]]
    for i in range(8):
        if win_test[i] == ["x", "x", "x"]:
            win_for_o_or_x = "x_win"
        if win_test[i] == ["o", "o", "o"]:
            win_for_o_or_x = "o_win"

    return win_for_o_or_x


def funtion_test_draw(The_playbook):
    # التحقق إذا كانت أي خلية فارغة
    if " " in The_playbook:
        return "no_draw"
    return "yes_draw"


def win_or_draw(option_1, option_2):
    if option_1 == 1:
        while True:
            player_1 = int(input("Enter player 1:"))
            if player_1 in prevent_dtep_repeat:
                print("Enter another number")
            elif player_1 > 9 or player_1 < 1:
                print("Enter a number between 1 and 9")
            else:
                prevent_dtep_repeat.append(player_1)
                The_playbook_after = update_playbook(The_playbook, player_1, 10)
                win_for_o_or_x = win_and_stop(The_playbook_after)
                test_draw = funtion_test_draw(The_playbook_after)
                return win_for_o_or_x, test_draw
    elif option_1 == 2:
        while True:
            player_2 = int(input("Enter player 2:"))
            if player_2 in prevent_dtep_repeat:
                print("Enter another number")
            elif player_2 > 9 or player_2 < 1:
                print("Enter a number between 1 and 9")
            else:
                prevent_dtep_repeat.append(player_2)
                The_playbook_after = update_playbook(The_playbook, 10, player_2)
                win_for_o_or_x = win_and_stop(The_playbook_after)
                test_draw = funtion_test_draw(The_playbook_after)
                return win_for_o_or_x, test_draw
    elif option_1 == 3:
        while True:
            user_game = int(input("Enter play:"))
            if user_game in prevent_dtep_repeat:
                print("Enter another number")
            elif user_game > 9 or user_game < 1:
                print("Enter a number between 1 and 9")
            else:
                if option_2 == 2:
                    prevent_dtep_repeat.append(user_game)
                    update_playbook(The_playbook, user_game, 10)
                    return user_game
                prevent_dtep_repeat.append(user_game)
                The_playbook_after = update_playbook(The_playbook, user_game, 10)
                win_for_o_or_x = win_and_stop(The_playbook_after)
                test_draw = funtion_test_draw(The_playbook_after)
                return win_for_o_or_x, test_draw
    elif option_1 == 4:
        while True:
            user_game = int(input("Enter play:"))
            if user_game in prevent_dtep_repeat:
                print("Enter another number")
            elif user_game > 9 or user_game < 1:
                print("Enter a number between 1 and 9")
            else:
                if option_2 == 2:
                    prevent_dtep_repeat.append(user_game)
                    update_playbook(The_playbook, 10, user_game)
                    return user_game
                prevent_dtep_repeat.append(user_game)
                The_playbook_after = update_playbook(The_playbook, 10, user_game)
                win_for_o_or_x = win_and_stop(The_playbook_after)
                test_draw = funtion_test_draw(The_playbook_after)
                return win_for_o_or_x, test_draw


def funtion_pc_game(The_playbook_after, game_for_x_or_o):
    while True:
        if game_for_x_or_o == 1:
            # funtion pc game o
            stop, pc_game = test_win_for_o(The_playbook_after)
            if stop:
                update_playbook(The_playbook, 10, pc_game)
                win_for_o_or_x = win_and_stop(The_playbook_after)
                test_draw = funtion_test_draw(The_playbook_after)
                prevent_dtep_repeat.append(pc_game)
                return win_for_o_or_x, test_draw
            stop, pc_game = test_win_for_x(The_playbook_after)
            if stop:
                update_playbook(The_playbook, 10, pc_game)
                win_for_o_or_x = win_and_stop(The_playbook_after)
                test_draw = funtion_test_draw(The_playbook_after)
                prevent_dtep_repeat.append(pc_game)
                return win_for_o_or_x, test_draw
            stop, pc_game = funtion_option_for_pc(The_playbook_after, 1)
            if stop:
                update_playbook(The_playbook, 10, pc_game)
                win_for_o_or_x = win_and_stop(The_playbook_after)
                test_draw = funtion_test_draw(The_playbook_after)
                prevent_dtep_repeat.append(pc_game)
                return win_for_o_or_x, test_draw
            stop, pc_game = option_game_for_pc_game(The_playbook_after)
            if stop:
                update_playbook(The_playbook, 10, pc_game)
                win_for_o_or_x = win_and_stop(The_playbook_after)
                test_draw = funtion_test_draw(The_playbook_after)
                prevent_dtep_repeat.append(pc_game)
                return win_for_o_or_x, test_draw
        elif game_for_x_or_o == 2:
            # funtion pc game x
            stop, pc_game = test_win_for_x(The_playbook_after)
            if stop:
                update_playbook(The_playbook, pc_game, 10)
                win_for_o_or_x = win_and_stop(The_playbook_after)
                test_draw = funtion_test_draw(The_playbook_after)
                prevent_dtep_repeat.append(pc_game)
                return win_for_o_or_x, test_draw
            stop, pc_game = test_win_for_o(The_playbook_after)
            if stop:
                update_playbook(The_playbook, pc_game, 10)
                win_for_o_or_x = win_and_stop(The_playbook_after)
                test_draw = funtion_test_draw(The_playbook_after)
                prevent_dtep_repeat.append(pc_game)
                return win_for_o_or_x, test_draw
            stop, pc_game = funtion_option_for_pc(The_playbook_after, 2)
            if stop:
                update_playbook(The_playbook, pc_game, 10)
                win_for_o_or_x = win_and_stop(The_playbook_after)
                test_draw = funtion_test_draw(The_playbook_after)
                prevent_dtep_repeat.append(pc_game)
                return win_for_o_or_x, test_draw
            stop, pc_game = option_game_for_pc_game(The_playbook_after)
            if stop:
                update_playbook(The_playbook, pc_game, 10)
                win_for_o_or_x = win_and_stop(The_playbook_after)
                test_draw = funtion_test_draw(The_playbook_after)
                prevent_dtep_repeat.append(pc_game)
                return win_for_o_or_x, test_draw


def test_win_for_o(The_playbook_after):
    # الأنماط الفائزة
    winning_combinations = [
        (0, 1, 2),  # الصف الأول
        (3, 4, 5),  # الصف الثاني
        (6, 7, 8),  # الصف الثالث
        (0, 3, 6),  # العمود الأول
        (1, 4, 7),  # العمود الثاني
        (2, 5, 8),  # العمود الثالث
        (0, 4, 8),  # الخط المائل الأول
        (2, 4, 6),  # الخط المائل الثاني
    ]
    # التحقق من الأنماط
    for combo in winning_combinations:
        x, y, z = combo
        if (The_playbook_after[x] == "o" and The_playbook_after[y] == "o" and The_playbook_after[z] == " "):
            return True, z + 1
        if (The_playbook_after[x] == "o" and The_playbook_after[z] == "o" and The_playbook_after[y] == " "):
            return True, y + 1
        if (The_playbook_after[y] == "o" and The_playbook_after[z] == "o" and The_playbook_after[x] == " "):
            return True, x + 1

    # إذا لم توجد حركة رابحة
    return False, 10


def test_win_for_x(The_playbook_after):
    # الأنماط الفائزة
    winning_combinations = [
        (0, 1, 2),  # الصف الأول
        (3, 4, 5),  # الصف الثاني
        (6, 7, 8),  # الصف الثالث
        (0, 3, 6),  # العمود الأول
        (1, 4, 7),  # العمود الثاني
        (2, 5, 8),  # العمود الثالث
        (0, 4, 8),  # الخط المائل الأول
        (2, 4, 6),  # الخط المائل الثاني
    ]
    # التحقق من الأنماط
    for combo in winning_combinations:
        x, y, z = combo
        if (The_playbook_after[x] == "x" and The_playbook_after[y] == "x" and The_playbook_after[z] == " "):
            return True, z + 1
        if (The_playbook_after[x] == "x" and The_playbook_after[z] == "x" and The_playbook_after[y] == " "):
            return True, y + 1
        if (The_playbook_after[y] == "x" and The_playbook_after[z] == "x" and The_playbook_after[x] == " "):
            return True, x + 1

    # إذا لم توجد حركة رابحة
    return False, 10


def funtion_option_for_pc(The_playbook_after, option_test):
    The_playbook_test = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    pc_game = 10
    option = []
    stop = False
    for i in range(9):
        for e in range(9):
            The_playbook_test[e] = The_playbook_after[e]
        if The_playbook_test[i] == " ":
            test = i + 1
            if option_test == 1:
                if 1 <= test <= 9:
                    The_playbook_test[test - 1] = "o"
                    stop, option1 = test_win_for_o(The_playbook_test)
                    if stop:
                        option.append(option1)
            elif option_test == 2:
                if 1 <= test <= 9:
                    The_playbook_test[test - 1] = "x"
                    stop, option1 = test_win_for_x(The_playbook_test)
                    if stop:
                        option.append(option1)
    if not option == []:
        pc_game = random.choice(option)
        stop = True
        return stop, pc_game
    return stop, pc_game


def option_game_for_pc_game(The_playbook_after):
    random_option = []
    pc_game = 10
    stop = True
    for i in range(9):
        if The_playbook_after[0+i] == " ":
            random_option.append(1+i)
    if not random_option ==[]:
        pc_game = random.choice(random_option)
    return stop, pc_game


print(" 7 | 8 | 9 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 1 | 2 | 3 ")
while True:
    The_playbook = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    prevent_dtep_repeat = []
    player_1 = 10
    player_2 = 10
    try:
        options_1 = int(input("\nair want play \n"
                            "vs player = 1\n"
                            "or vs robbot = 2\n"
                            "or break = 3\n"))
        #vs player
        if options_1 == 1:
            for i in range(5):
                win_for_o_or_x, test_draw = win_or_draw(1, 1)
                if win_for_o_or_x == "x_win":
                    print_xo()
                    print("win for player 1(x):\n")
                    break
                elif test_draw == "yes_draw":
                    print_xo()
                    print("draw")
                    break
                print_xo()

                win_for_o_or_x, test_draw = win_or_draw(2, 1)
                if win_for_o_or_x == "o_win":
                    print_xo()
                    print("win for player 2(o):\n")
                    break
                elif test_draw == "yes_draw":
                    print_xo()
                    print("draw")
                    break
                print_xo()
        #vs robbot
        elif options_1 == 2:
            options_2 = input("play x or o\n"
                              "or random option:\n")
            play_robbot = 3
            if   options_2 == "x":
                play_robbot = 1
            elif options_2 == "o":
                play_robbot = 2
            elif options_2 == "random":
                play_robbot = random.choice([1, 2])

            #the game for user
            if   play_robbot == 1:
                #the frist game for pc
                user_input = win_or_draw(3, 2)
                if not user_input == 10:
                    if user_input == 9 or user_input == 7 or user_input == 3 or user_input == 1:
                        pc_input = 5
                        update_playbook(The_playbook, 10, pc_input)
                    elif user_input == 5:
                        pc_input = random.choice([1, 3, 7, 9])
                        update_playbook(The_playbook, 10, pc_input)
                    elif user_input == 2 or user_input == 6 or user_input == 8 or user_input == 4:
                        pc_input = 5
                        update_playbook(The_playbook, 10, pc_input)
                    else:
                        print("Enter number")
                print_xo()
                for i in range(10):
                    win_for_o_or_x, test_draw =  win_or_draw(3,1)
                    if win_for_o_or_x == "x_win":
                        print_xo()
                        print("win for player 1(x):")
                        break
                    elif test_draw == "yes_draw":
                        print_xo()
                        print("draw")
                        break
                    win_for_o_or_x, test_draw = funtion_pc_game(The_playbook, 1)
                    if win_for_o_or_x == "o_win":
                        print_xo()
                        print("win for pc (o):")
                        break
                    elif test_draw == "yes_draw":
                        print_xo()
                        print("draw")
                        break
                    print_xo()
            #the game for pc
            elif play_robbot == 2:
                pc_input = random.randint(1, 9)
                update_playbook(The_playbook, pc_input, 10)
                prevent_dtep_repeat.append(pc_input)
                print_xo()
                for i in range(10):
                    win_for_o_or_x, test_draw = win_or_draw(4, 1)
                    if win_for_o_or_x == "o_win":
                        print_xo()
                        print("win for player 1(x):")
                        break
                    elif test_draw == "yes_draw":
                        print_xo()
                        print("draw")
                        break
                    win_for_o_or_x, test_draw = funtion_pc_game(The_playbook, 2)
                    if win_for_o_or_x == "x_win":
                        print_xo()
                        print("win for pc (x):")
                        break
                    elif test_draw == "yes_draw":
                        print_xo()
                        print("draw")
                        break
                    print_xo()
            #break
            elif play_robbot == 3:
                print("chooso x, o or random")
        #break
        elif options_1 == 3:
            break
        else:
            print("Enter 1, 2 or 3:\n")
    except ValueError as ex:
        print("ERROR")
        print("Enter number:\n")