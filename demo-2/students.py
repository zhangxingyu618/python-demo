# 主函数
def main():
    student_list = []
    student_list.append({"学号": 1000, "姓名": "홍길동", "学科": "열공학과"})
    student_list.append({"学号": 1001, "姓名": "강감찬", "学科": "체육학과"})
    student_list.append({"学号": 1002, "姓名": "이순신", "学科": "물리학과"})
    student_list.append({"学号": 1003, "姓名": "신사임당", "学科": "열공학과"})
    student_list.append({"学号": 1004, "姓名": "22", "学科": "22"})
    while True:
        print("┌------------------------------------------------┐")
        print("│ 学生管理系统 V 1.0 created by 范逸芊              │")
        print("├------------------------------------------------┤")
        print("│1.整体输出 2.查询 3.新增学生 0.结束                 │")
        print("└------------------------------------------------┘")
        number = int(input("请输入命令 : "))
        # 여기부터 코드 작성
        menus = [1, 2, 3, 0]
        while True:
            if number not in menus:
                number = int(input("输入命令有误，请重新输入 : "))
            else:
                break

        if number == 1:
            show_student_info(student_list)
        elif number == 2:
            search_stduent_info(student_list)
        elif number == 3:
            add_student_info(student_list)
        elif number == 0:
            print("┌------------------------------------------------┐")
            print("│  退出程序                                       │")
            print("└------------------------------------------------┘")
            break
        # ...
        # 코드 작성 종료
        print("==结束==")
        input("계속하려면 엔터키를 누르세요…")
    # 코드 끝


# 显示学生信息
def show_student_info(student_list):
    print("┌------------------------------------------------┐")
    print("│ 学生信息                                        │")
    print("└------------------------------------------------┘")
    for info in student_list:
        print("学号:", info.get("学号"), ", 姓名:", info.get("姓名"), ", 学科:", info.get("学科"))


#  查询
def search_stduent_info(student_list):
    print("┌------------------------------------------------┐")
    print("│ 选择搜索类型                                     │")
    print("├------------------------------------------------┤")
    print("│1.搜索姓名 2.搜索学科                              │")
    print("└------------------------------------------------┘")
    number = int(input("请选择搜索类型 : "))
    menus = [1, 2]
    while True:
        if number not in menus:
            number = int(input("输入命令有误，请重新输入 : "))
        else:
            break
    if number == 1:
        name = str(input("请输入搜索的名字 : "))
        for info in student_list:
            if name == info.get("姓名"):
                print("学号:", info.get("学号"), ", 姓名:", info.get("姓名"), ", 学科:", info.get("学科"))
            else:
                print("抱歉没有此结果")
    elif number == 2:
        subject = str(input("请输入搜索的学科 : "))
        for info in student_list:
            if subject == info.get("学科"):
                print("学号:", info.get("学号"), ", 姓名:", info.get("姓名"), ", 学科:", info.get("学科"))


# 添加学生
def add_student_info(student_list):
    print("注册新的学生信息")
    sid = int(input("请输入学号 : "))
    name = str(input("请输入姓名 : "))
    subject = str(input("请输入学科 : "))
    new_list = {"学号": sid, "姓名": name, "学科": subject}
    student_list.append(new_list)
    print("增加了新的学生")


if __name__ == '__main__':
    main()
