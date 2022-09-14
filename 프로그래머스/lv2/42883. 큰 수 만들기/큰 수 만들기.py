def solution(number, k):
    st = []
    
    for n in number:
        while st and st[-1] < n and k > 0:
            st.pop()
            k -= 1
            
        st.append(n)
        
    return ''.join(st[:len(st)-k])