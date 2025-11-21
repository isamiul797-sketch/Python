class phone:
    def __init__(self):
        print("you can call")


class samsung(phone):
    def __init__(self):
        super().__init__()
        print("you can take photo")

s= samsung()