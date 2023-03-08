def solution(bin1, bin2):
    answer = ''
    bin1 = int('0b' + bin1, 2)
    bin2 = int('0b' + bin2, 2)
    result = str(bin(bin1 + bin2))
    answer = result[2:]
    return answer