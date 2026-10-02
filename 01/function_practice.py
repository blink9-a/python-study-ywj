def get_score(score, bonus):

    result = score + bonus
    return result


score_result = get_score(30, 20)

print("최종 점수:", score_result)


print("--------------------")


def get_price(price, count):
    print("한 개 가격:", price)
    print("주문 개수:", count)

    result = price * count
    return result


price_result = get_price(price=2000, count=3)

print("전체 가격:", price_result)