import random

# 出拳
win = 0
ping = 0
lose = 0
while True:
    computer = str(random.randint(1, 3))
    # print(computer)
    user = input('请出拳：（1=剪刀，2=石头，3=布）')  # 请用户输入选择
    while user not in ["1", "2", "3"]:  # 当用户输入错误，提示错误，重新输入
        user = input('输入有误，请重新出拳')  # 请用户输入选择

    if computer == "1":
        com = "剪刀"
    elif computer == "2":
        com = "石头"
    else:
        com = "布"

    if user == "1":
        us = "剪刀"
    elif user == "2":
        us = "石头"
    else:
        us = "布"

    print('-----------过程-------------')
    print('电脑出了：%s' % com)
    print('你出了：%s' % us)
    # 胜负
    if user == computer:  # 使用if进行条件判断
        print('平局！当前比分 %d 胜, %d 败' % (win, lose))
        ping = ping+1
    elif (user == "1" and computer == "3") or (user == "2" and computer == "1") or (
            user == "3" and computer == "2"):
        win = win + 1
        print('你赢了！当前比分 %d 胜, %d 败' % (win, lose))
        if (win == 3):
            break
    else:
        lose = lose + 1
        print('你输了！当前比分 %d 胜, %d 败' % (win, lose))
        if (lose == 3):
            break
