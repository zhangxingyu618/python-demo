import re


# 보안성 검사 함수
def check_security(pwd):
    if len(pwd) >= 8:
        re_str = re.compile(r'[A-Za-z]', re.S)
        re_num = re.compile(r'\d+', re.S)
        re_char = re.compile(r'[!@#$%^&*()]')
        res_str = re.findall(re_str, pwd)
        res_num = re.findall(re_num, pwd)
        res_char = re.findall(re_char, pwd)

        if res_str and res_num and res_char:
            return "安全"
        elif res_str and res_num or res_str and res_char:
            return "一般"
        else:
            return "脆弱"
    else:
        return "不可以"


# 보안성 검사 알고리즘 작성
# 비밀번호 보안성을 검사하고 적절한 값을 return 함
# return 값은 안전, 보통, 취약, 사용불가 중 택 1 #비밀번호 보안성 검사하기
pwd = input("비밀번호를 입력하세요: ")
print("보안상태는 %s 입니다." % check_security(pwd))
