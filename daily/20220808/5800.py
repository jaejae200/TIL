T = int(input())

for _ in range(1, T+1):
    N = list(map(int, input().split())) 
    del N[0]
    N.sort()
    max_score = max(N)
    min_score = min(N)

    largest_gap = []

    for j in range(len(N)-1):
        largest_gap.append(N[j+1] - N[j])
        
    print(f'Class {_}')
    print(f'Max {max_score}, Min {min_score}, Largest gap {max(largest_gap)}') 


    # for j in range(1, len(N)-1):

    #     if j < len(N)-2:
    #         if largest_gap < N[j+1] - N[j]:
    #             largest_gap = N[j+1] - N[j]