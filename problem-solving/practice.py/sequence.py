I=1
while I <=9:
    J=I+6
    for _ in range(3):
        print(f"I={I} J={J}")
        J-=1

    I+=2

    #sequence02

I = 0.0
EPS = 1e-9

while I <= 2.0 + EPS:
    for j in range(1, 4):
        J = I + j
        
        # Format I
        if abs(I - round(I)) < EPS:
            I_str = str(int(round(I)))
        else:
            I_str = f"{I:.1f}"
        
        # Format J
        if abs(J - round(J)) < EPS:
            J_str = str(int(round(J)))
        else:
            J_str = f"{J:.1f}"
        
        print(f"\nI={I_str} J={J_str}")
    I += 0.2
