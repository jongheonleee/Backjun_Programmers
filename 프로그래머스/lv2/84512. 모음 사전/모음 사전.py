from itertools import product
def solution(word):
    words = []
    
    # 중복 순열활용하기
    # words의 길이가 5이하
    for i in range(1, 6):
        for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            # 이때, c 같은 경우는 중복조합(튜플형태임)
            # 문자열로 전환해서 리스트에 담기
            words.append(''.join(list(c)))
    
    # 정렬
    words.sort()
    return words.index(word) + 1
