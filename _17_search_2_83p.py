#학생번호를 입력하면 학생번호에 해당하는 이름을 순차탐색으로 찾아 돌려줌, 없으면?출력


stu_num = [39, 14, 67, 105]
stu_name = ["JUSTIN", "JOHN", "MIKE", "SUMMER"]

def search_stu():
    input_num = int(input("학생의 번호를 입력하세요>"))  
    #input으로 받은것은 문자이므로 int를 사용해서 숫자로 변환해주어야한다
    for i in range(0, len(stu_num)):
        if input_num == stu_num[i]:
            return stu_name[i]
            
    return "?"

print(search_stu())

