def solution(arr):
    st = []
    
    for num in arr:
        if len(st) == 0:
            st.append(num)
            
        elif st[-1] != num:
            st.append(num)
            
    return st
