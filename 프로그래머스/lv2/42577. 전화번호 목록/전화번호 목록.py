def solution(phone_book):
    # 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
    # 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false,
    # 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.
    
    phone_num = {} 
    for num in phone_book:
        phone_num[num] = 1
        
    for num in phone_book:
        tmp = ''
        
        for n in num:
            tmp += n
            
            if tmp in phone_num and tmp != num:
                return False
            
    return True
    