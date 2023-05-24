T = int(input())

for _ in range(T):
    card_cnt = [0] * 10
    cards = input()

    for card in cards:
        card_cnt[int(card)] += 1

    baby_gin = 0
    i = 0
    while i <= 9:
        if card_cnt[i] >= 3:
            card_cnt[i] -= 3
            baby_gin += 1
            continue

        if i <= 7:
            if card_cnt[i] and card_cnt[i+1] and card_cnt[i+2]:
                card_cnt[i], card_cnt[i + 1], card_cnt[i + 2] = card_cnt[i]-1, card_cnt[i+1]-1, card_cnt[i+2]-1
                baby_gin += 1
        i += 1

    print('True') if baby_gin == 2 else print('False')