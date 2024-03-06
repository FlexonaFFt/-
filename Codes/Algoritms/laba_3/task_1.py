"""n = int(input("Введите количество температур: "))
temperatures = list(map(int, input("Введите температуры через пробел: ").split()))
chaotic_days = 0

for i in range(1, n - 1):
    if temperatures[i] > temperatures[i - 1] and temperatures[i] > temperatures[i + 1]:
        chaotic_days += 1

print(chaotic_days)"""

t = list(map(int, input("Введите температуры через пробел: ").split()))
ends = (t[0] > t[1]) + (t[-1] > t[-2])
su   = sum( [ t[i] > max( t[i-1], t[i+1] ) for i in range( 1, len(t)-1 ) ] )
print( ends + su )