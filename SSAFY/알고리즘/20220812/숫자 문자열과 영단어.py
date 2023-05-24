def solution(s):
    answer = 0
    dict_num = {'zero': '0',
                'one': '1',
                'two': '2',
                'three': '3',
                'four': '4',
                'five': '5',
                'six': '6',
                'seven': '7',
                'eight': '8',
                'nine': '9'}
    for key in dict_num:
        # print(dict_num[key])
        # print(type(dict_num[key]))
        s = s.replace(key, dict_num[key])
        # answer = int(s) # 제발 들여쓰기...
    answer = int(s)
    return answer

solution('one4seveneight')