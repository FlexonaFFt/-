results = {}

num_records = int(input())

for _ in range(num_records):
    candidate, votes = input().split()
    votes = int(votes)
    if candidate in results:
        results[candidate] += votes
    else:
        results[candidate] = votes
    
for candidate in sorted(results.keys()):
    print(f'{candidate}' + ' ' + f'{results[candidate]}')
