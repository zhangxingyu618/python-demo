import random


def roll(sides=6):
    num_rolled = None
    num_rolled = random.randint(1, sides)
    return num_rolled


def main():
    sides = 6
    stop = False
    while not stop:
        user_in = input('试试手气？ 回车=掷骰子， Q=退出')
        if user_in.lower() == 'q':
            stop = True
        else:
            num_rolled = None
        num_rolled = roll(sides)
        print('你掷出了 %d 点' % num_rolled)
        print('欢迎下次再来')


main()
