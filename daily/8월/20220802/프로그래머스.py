def solution(s):
    word =['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(word)):
        s = s.replace(word[i], str(i)) # s.replace (word의 index값과 i(0,1,2,3,4,...) 문자열로 바꾼 값을 바꾼다)
    
    return int(s)       # replace 마친


    