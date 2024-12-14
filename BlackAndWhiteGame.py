# 버전 1 : 승리 로직과 랜덤카드 매커니즘을 추가했다.
# random 모듈에서 shuffle 함수를 가져온다.
from random import shuffle

# 플레이어와 컴퓨터의 카드 생성과 승리 로직에 대한 함수를 구현했다.
while True:
    N = input("1: 숫자 카드 게임 실행 2: 게임 기록 보기 3: 종료\n")

    if N == '1':
        # 카드 배치에 랜덤성을 더해 매번 다른 게임 결과를 가져오게 한다.
        player_cards = list(range(1, 11))
        computer_cards = list(range(1, 11))
        shuffle(player_cards)
        shuffle(computer_cards)
        
        player_card = player_cards.pop(0)
        computer_card = computer_cards.pop(0)

        print(f"플레이어가 낸 카드: {player_card}")
        print(f"컴퓨터가 낸 카드: {computer_card}")
        
        # 승리 로직을 구현, 1은 10을 이기는 특수 룰을 구현했다.
        if player_card == 1 and computer_card == 10:
            print("플레이어 승리! (특별 규칙: 1이 10을 이김)")
        elif player_card == 10 and computer_card == 1:
            print("컴퓨터 승리! (특별 규칙: 10이 1에게 패배)")
        elif player_card > computer_card:
            print("플레이어 승리!")
        elif player_card < computer_card:
            print("컴퓨터 승리!")
        else:
            print("무승부!")
    
    elif N == '2':
        print("기록 보기 기능은 이후 버전에서 추가됩니다.")
    elif N == '3':
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 값입니다. 1, 2, 3 중에 입력하세요.")

