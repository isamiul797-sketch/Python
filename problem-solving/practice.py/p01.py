while True:

    try:
        M,N=map(int,input().split())

        if M<=0 or N<=0:
            break

        if M>N:
            M,N=N,M

        total=0
        output=''

        for i in range(M,N+1):
            output+=f"{i} "
            total+=i

        print(f"{output}Sum={total}")


    except EOFError:
        break


