def solve_knapsack_dp(weights, values, capacity):
    """
    Solves the 0/1 Knapsack problem using a Dynamic Programming approach.

    Args:
        weights (list): A list of the weights of the items.
        values (list): A list of the values of the items.
        capacity (int): The maximum weight capacity of the knapsack.

    Returns:
        int: The maximum value that can be carried in the knapsack.
    """
    n = len(weights)
    
    # Create a 2D DP table with dimensions (n+1) x (capacity+1).
    # dp[i][w] will store the maximum value achievable with the first i items
    # and a maximum capacity of w.
    # We initialize the table with 0s.
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the table in a bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # Get weight and value of the current item (adjusting for 0-based indexing)
            current_weight = weights[i-1]
            current_value = values[i-1]

            if current_weight <= w:
                # If the item fits, we have two choices:
                # 1. Don't include the item: Value is same as dp[i-1][w]
                # 2. Include the item: Value is current_value + value of remaining capacity
                #    which is dp[i-1][w - current_weight]
                # We take the maximum of these two choices.
                dp[i][w] = max(dp[i-1][w], current_value + dp[i-1][w - current_weight])
            else:
                # If the item is too heavy for the current capacity w, we cannot include it.
                dp[i][w] = dp[i-1][w]

    # The answer is found in the bottom-right cell of the table.
    return dp[n][capacity]

# --- Define the problem data from the image ---
# Item 1: Weight = 1kg, Value = 10 pesos
# Item 2: Weight = 2kg, Value = 15 pesos
# Item 3: Weight = 3kg, Value = 40 pesos

items_weights = [1, 2, 3]
items_values = [10, 15, 40]

# NOTE: The problem in the image does not specify the backpack's capacity.
# We will assume a capacity to run the example. Let's assume it can hold 5kg.
knapsack_capacity = 5

# --- Solve the problem ---
max_value = solve_knapsack_dp(items_weights, items_values, knapsack_capacity)

# --- Print the results ---
print("--- Knapsack Problem Solution (Dynamic Programming) ---\n")
print("Given Items:")
for i in range(len(items_weights)):
    print(f"  Item {i+1}: Weight = {items_weights[i]}kg, Value = {items_values[i]} pesos")

print(f"\nAssumed Knapsack Capacity: {knapsack_capacity} kg")
print(f"Maximum Value Achievable: {max_value} pesos")

# For a capacity of 5kg, the optimal solution is to take Item 2 (2kg, 15 pesos)
# and Item 3 (3kg, 40 pesos) for a total weight of 5kg and a total value of 55 pesos.