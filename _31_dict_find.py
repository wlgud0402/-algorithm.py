#학생번호 입력하면 번호애 해당하는 이름을 돌려주고 번호 없으면 물음표 돌려줌

d ={
    39:"Justin",
    14:"John",
    67:"Mike",
    105:"Summer"
}

def find_stu(put_list):
    stu_num = int(input("찾으시는 학생의 번호를 입력하세요"))
    if stu_num in put_list:
        return put_list[stu_num]
    else:
        return "찾는 학생이 존재하지 않습니다."

print(find_stu(d))