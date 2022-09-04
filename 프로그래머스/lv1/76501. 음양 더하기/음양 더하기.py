def solution1(absolutes, signs):
    return sum(absolute if sign else -absolute for absolute, sign in zip(absolutes, signs))

def solution(absolutes, signs):
    return sum(absolute if signs[idx] else -absolute for idx, absolute in enumerate(absolutes))