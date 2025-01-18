import sys
input_data = sys.stdin.read().split()
results = []
 
for i in range(0, len(input_data), 2):
    N = int(input_data[i])
    S = int(input_data[i + 1])
    x = S // (N + 1)
    results.append(x)
    
for result in results:
    print(result)