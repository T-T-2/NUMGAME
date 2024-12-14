from random import shuffle

# 버전 2 : 라운드 추가 및 플레이어의 카드 선택 기능을 추가했다.
# 무한 루프를 통해 사용자가 메뉴를 반복적으로 선택할 수 있도록 한다.
while True:
    # 사용자에게 선택지를 제시하고 입력을 받는다.
    N = input("1: 숫자 카드 게임 실행 2: 게임 기록 보기 3: 종료\n")

    # 사용자가 "1"을 입력하면 카드 게임 실행한다.
    if N == '1':
        # 플레이어와 컴퓨터의 카드 초기화한다.  (1부터 10까지의 숫자)
        computer_cards = list(range(1, 11))
        player_cards = list(range(1, 11))
        shuffle(computer_cards)  # 컴퓨터의 카드는 무작위로 섞인다.

        # 결과를 저장할 리스트 초기화한다.  (승리, 무승부, 패배 횟수)
        result = [0, 0, 0]  # [승리, 무승부, 패배]

        # 10번의 게임 진행한다.
        for _ in range(10):
            # 플레이어가 직접 카드를 선택한다.
            # 플레이어가 사용할 수 있는 카드 보여준다.
            print(f"현재 플레이어가 가지고 있는 카드: {player_cards}")
            while True:
                try:
                    player_card = int(input("플레이어가 낼 카드를 선택하세요 (1-10): "))
                    if player_card not in range(1, 11):
                        raise ValueError
                    break
                except ValueError:
                    print("잘못된 입력입니다. 1부터 10 사이의 숫자를 입력하세요.")

            # 선택한 카드는 소모된다.
            player_cards.remove(player_card)
            # 컴퓨터는 카드 더미에서 가장 앞의 카드를 선택한다.
            computer_card = computer_cards.pop(0)

            # 현재 플레이어와 컴퓨터가 낸 카드 출력한다.
            print(f"플레이어가 낸 카드: {player_card}")
            print(f"컴퓨터가 낸 카드: {computer_card}")

            # 특별 규칙: 플레이어 카드가 1이고 컴퓨터 카드가 10일 경우 플레이어가 승리한다.
            if player_card == 1 and computer_card == 10:
                result[0] += 1
                print("플레이어 승리! (특별 규칙: 1이 10을 이김)")

            # 특별 규칙: 플레이어 카드가 10이고 컴퓨터 카드가 1일 경우 컴퓨터가 승리한다.
            elif player_card == 10 and computer_card == 1:
                result[2] += 1  # 패배 횟수 증가
                print("컴퓨터 승리! (특별 규칙: 10이 1에게 패배)")

            # 일반 규칙: 플레이어 카드가 컴퓨터 카드보다 클 경우 플레이어 승리한다.
            elif player_card > computer_card:
                result[0] += 1  # 승리 횟수 증가
                print("플레이어 승리!")

            # 일반 규칙: 컴퓨터 카드가 플레이어 카드보다 클 경우 컴퓨터 승리한다.
            elif player_card < computer_card:
                result[2] += 1  # 패배 횟수 증가
                print("컴퓨터 승리!")

            # 카드 숫자가 동일할 경우 무승부로 처리한다.
            else:
                result[1] += 1
                print("무승부!")

        # 10판이 종료된 후 최종 결과를 출력한다.
        print(f"10판 결과: 승리 {result[0]}번, 무승부 {result[1]}번, 패배 {result[2]}번")

    # 사용자가 "2"를 입력하면 기록 보기 기능 실행한다.  (현재는 구현되지 않음)
    elif N == '2':
        print("기록 보기 기능은 이후 버전에서 추가됩니다.")

    # 사용자가 "3"을 입력하면 프로그램을 종료한다.
    elif N == '3':
        print("프로그램을 종료합니다.")
        break

    # 그 외의 입력에 대해서는 올바르지 않은 입력임을 알린다.
    else:
        print("잘못된 값입니다. 1, 2, 3 중에 입력하세요.")

