#BOJ-5543
burger=list()
drink=list()

for _ in range(3) :
    burger.append(int(input()))
for _ in range(2) :
    drink.append(int(input()))

    burger_min=min(burger)
    drink_min=min(drink)

hap = (burger_min+drink_min)-50
print(hap)