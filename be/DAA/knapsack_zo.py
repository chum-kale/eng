def knapsack_01(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n+1)]

    for i in range(n+1):
        for w in range(capacity + 1):
            if i ==0 or w == 0:
                dp[i][w] = 0
            elif weights[i -1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]

n = int(input("Enter the number of items: "))
values = []
weights = []
for i in range(n):
    value, weight = map(int, input(f"Enter value and weight for item {i + 1} (e.g., 60 10): ").split())
    values.append(value)
    weights.append(weight)
capacity = int(input("Enter the capacity of the knapsack: "))

print("Maximum value:", knapsack_01(values, weights, capacity))