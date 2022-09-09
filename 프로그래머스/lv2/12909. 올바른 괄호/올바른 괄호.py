def solution(s):
    if s[0] == ')':
        return False
    
    st = []
    
    for char in s:
        if char == '(':
            st.append(')')
            
        elif len(st) > 0 and st[-1] == char:
            st.pop()
            
            
    return len(st) == 0