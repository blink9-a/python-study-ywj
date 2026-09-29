def hello():
    print("안녕하세요")


hello()


def attack(damage):
    print("데미지:", damage)


attack(30)



def show_values(a, b):
    print("a:", a)
    print("b:", b)


show_values(a=10, b=20)




def add(a, b):
    result = a + b
    return result


number = add(10, 20)

print(number)