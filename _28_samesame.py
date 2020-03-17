#회문찾기 >>> 기러기 ==기러기 

def same_same(put_str):

    qu = []
    st = []

    for i in put_str:
        if i.isalpha():
            qu.append(i.lower())
            st.append(i.lower())
    
    while qu:
        if qu.pop(0) != st.pop():
            return False
    
    return True

print(same_same("Wow"))
print(same_same("Hello"))