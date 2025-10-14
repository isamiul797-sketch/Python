while True:

    valid_score=0
    total=0.0

    while valid_score <2:
        score=float(input())

        if 0<= score <=10:
            total +=score
            valid_score+=1
        else:
            print("nota invalida")

    average=total/2
    print(f"media = {average:.2f}")

    while True:
        print(f"novo calculo (1-sim 2-nao)")
        option=int(input())

        if option == 1:
            break
        elif option == 2:
            exit()
        else:
            continue

