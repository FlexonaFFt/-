country_list = {}
for _ in range(int(input())):
    data = input().split()
    country = data[0]
    cities = data[1:]
    for city in cities:
        country_list[city] = country
'''for _ in range(int(input())):
    country, city = input().split()
    country_list[country] = set(city)'''   
for _ in range(int(input())):
    trigger_city = input()
    if trigger_city in country_list:
        print(country_list[trigger_city])