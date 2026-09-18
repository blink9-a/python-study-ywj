print("구매할 상품의 이름과 가격을 알려주세요")
a = input("상품 이름")
b = int(input("상품 가격"))

if b >= 10000:
    print("2000원을 할인합니다.")
    price = b - 2000
elif b >= 5000:
    print("1000원을 할인합니다.")
    price = b - 1000
else:
    print("할인하지 않습니다.")
    price = b


print(a, "의 최종 가격은", price, "원입니다.")