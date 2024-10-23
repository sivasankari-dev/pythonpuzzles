def check_evenorodd(pile1):
    return (pile1 % 2 == 0)


n = 17
check_evenorodd(n)

piles = [n]

if check_evenorodd:
   for _ in range(n-1):
    piles.append(piles[-1]+2)
else:
   for _ in range(n-1):
    piles.append(piles[-1]+1)

print (piles)
