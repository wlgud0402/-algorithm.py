#큐와 스택을 쓰지 않고 회문판단 >>> 문장의 아뒤를 차례로 비교

def same_same(put_str):

    i = 0
    j = len(put_str) -1
    while i < j:
        if put_str[i].isalpha() == False:
            i += 1

        elif put_str[j].isalpha() == False:
            j -= 1

        elif put_str[i].lower() != put_str[j].lower():
            return False

        else:
            i += 1
            j -= 1

    return True

print(same_same("Wow"))
print(same_same("Madam, I'm Adam."))    
print(same_same("Heollo"))