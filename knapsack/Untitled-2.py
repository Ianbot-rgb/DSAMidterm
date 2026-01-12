# 0/1 Knapsack using Dynamic Programming

# Items from the problem
weights = [1, 2, 3]      # kg
values = [10, 15, 40]   # pesos
capacity = 5            # bag capacity (kg)

n = len(values)

# Create DP table
dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

# Fill the DP table
for i in range(1, n + 1):
    for w in range(capacity + 1):
        if weights[i - 1] <= w:
            dp[i][w] = max(
                dp[i - 1][w],
                dp[i - 1][w - weights[i - 1]] + values[i - 1]
            )
        else:
            dp[i][w] = dp[i - 1][w]

# Backtrack to find selected items
w = capacity
selected_items = []

for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        selected_items.append(i)
        w -= weights[i - 1]

# Results
print("Maximum value:", dp[n][capacity], "pesos")
print("Selected items:", selected_items)
