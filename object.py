from fontTools.misc.cython import returns

if __name__ == '__main__':
    #dictionary 이용 해서 메뉴 리스트 생성

    cola={
        "price":2000,
        }

    alcol_drink={
        "price":3000,
        "taste":"good"
        }


    hamburger={
    "price":5000,
    "taste":"spicy",
    "bread":"flatbread",
    "vegetable":"cabbage"

    }
    ramen={
        "price":2000,
        "taste":"good"
    }

    #자판기 알고리즘 구동

    menu= ["0.cola", "1.alcol_drink", "2.hamburger", "3.ramen"]
    print("메뉴 출력:cola, alcol_drink, hamburger, ramen",)
    a = input("메뉴를 선택하세요(메뉴 앞에 있는 숫자 입력 가능): ")





    if a=='cola':
        print("🥤가 선택되었습니다")
        print("🥤의 가격",cola["price"],"원")
        c = int(input("돈을 투입해주세요: "))
        money=(c-int(cola["price"]))
        print(f'잔돈은 {money}원 입니다')
        if money > 0:
            print("다른 메뉴를 선택하시겠습니까?")
            choice = int(input("yse(1) or no(2): "))
            if choice == 2:
                print("자판기 프로그램을 종료하겠습니다")

            elif choice == 1:
              a=input("메뉴를 선택해주세요: ")


    elif a=='alcol_drink':
        print("🍺가 선택 되었습니다")
        print("🍺의 가격",alcol_drink["price"],"원")
        t=(int(input("돈을 투입해주세요: ")))
        m=(t-int(alcol_drink["price"]))
        print(f'잔돈은 {m}원 입니다')
        if m > 0:
            print("다른 메뉴를 선택하시겠습니까?")
            choice = int(input("yse(1) or no(2): "))
            if choice == 2:
                print("자판기 프로그램을 종료하겠습니다")

            elif choice == 1:
              a=input("메뉴를 선택해주세요: ")


    elif a=='hamburger':
        print("🍔가 선택되었습니다")
        print("🍔의 가격",hamburger["price"],"원")
        h = (int(input("돈을 투입해주세요: ")))
        ham = (h-int(hamburger["price"]))
        print(f'잔돈은{ham}원 입니다')
        if ham > 0:
            print("다른 메뉴를 선택하시겠습니까?")
            choice = int(input("yse(1) or no(2): "))
            if choice == 2:
                print("자판기 프로그램을 종료하겠습니다")

            elif choice == 1:
              a=input("메뉴를 선택해주세요: ")

    elif a=='ramen':
        print("🍜이 선택되었습니다")
        print("🍜의 가격", ramen["price"], "원")
        r = (int(input("돈을 투입해주세요: ")))
        r1 = (r - int(ramen["price"]))
        print(f'잔돈은 {r1}원 입니다')
        if r1 > 0:
            print("다른 메뉴를 선택하시겠습니까?")
            choice = int(input("yse(1) or no(2): "))
            if choice == 2:
                print("자판기 프로그램을 종료하겠습니다")

            elif choice == 1:
              a=input("메뉴를 선택해주세요: ")

