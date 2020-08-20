# 고스톱 패 섞기 및 패 분배
# 패의 수 : 48, 게임 인원수 : 3
import random


def init(userNum):
    deck = list(range(1, 49))
    random.shuffle(deck)  # 시퀀스 내용을 랜덤하게 섞음

    # 컴프리핸션 사용
    users = [[] for _ in range(userNum)]  # userNum 의 사용자가 가질 패를 저장할 비어있는 이중리스트 생성
    return deck, users


def assign(deck, users):
    for _ in range(7):  # 7장씩, 이렇게 하면 한장씩 주는 거, 루프문 순서 바꾸면 7장씩 주는 거
        for userCard in users:
            card = deck.pop()  # deck 에 있는 거 제거
            userCard.append(card)  # user 리스트에 추가


def printResult(deck, users):
    print("사용자 패")
    for ix, userCard in enumerate(users, 1):
        print(f"{ix} 번째 사용자 : ", userCard)
    print(f"남은 패({len(deck)}장)")
    print(deck)


def main():
    userNum = int(input("게임 인원수: "))
    deck, users = init(userNum)  # 패 섞기
    assign(deck, users)  # 패 분배
    printResult(deck, users)  # 결과 출력


main()