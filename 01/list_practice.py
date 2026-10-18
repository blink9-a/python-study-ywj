
items = ["검", "방패", "물약"]

print(items)

print(items[0])
print(items[1])
print(items[2])

items[0] = "마법 지팡이"
print(items)

for item in items:
    print(item)

if "물약" in items:
    print("물약을 가지고 있습니다!")
else:
    print("물약이 없습니다!")
