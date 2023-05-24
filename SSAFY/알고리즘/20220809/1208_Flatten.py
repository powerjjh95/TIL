T = 10
for test_case in range(1, T + 1):
    dump = int(input()) # 덤프 수 저장
    box = list(map(int, input().split())) # 숫자 리스트 저장
    # print(type(box)) # <class 'list'>
    # 먼저 순서대로 나열 후 분배
    while True:

        # 버블 정렬 # 최소와 최대를 찾기 위함
        for i in range(len(box)-1, 0, -1): # 모든 칸의 박스에는 무조건 1개 이상의 박스가 있기 때문에 괜춘 # len(box) = 100
            for j in range(i): #
                if box[j] > box[j + 1]:
                    box[j], box[j + 1] = box[j + 1], box[j]

        # 정렬 후, 최대 최소 차이가 1보다 작거나 같으면 Break
        # 아래 조건에서 평탄화가 더 이상 발생하지 않는다.
        if box[len(box)-1] - box[0] <= 1: # box[len(box)-1] : 최대 / len(box) - 1 = 99, 정렬된 상태에서 box[99] : 최대
            break
        elif dump == 0: # dump 횟수를 다 소진하였을 경우
            break

        if box[len(box)-1] - box[0] >= 1:
            dump -= 1
            box[len(box) - 1] -= 1
            box[0] += 1

    print(f'#{test_case} {box[len(box) - 1] - box[0]}')


    # 제일 위에 있는 친구들을 하나씩 내려야한다.

    # print(box)
    #
    # if box[i]
    # # 카운트 정렬 쓰면 안됨...
    # cnt = [0] * 100
    # for cnt_box in box:
    #     cnt[cnt_box] += 1
    # print(cnt)
