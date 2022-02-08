# knapsack algorithm
def knapsack(capacity, n, weight, values):
    if capacity == 0 or n == 0:
        return 0

    elif weight[n - 1] > capacity:
        return knapsack(capacity, n-1, weight, values)

    else:
        return max(values[n-1] + knapsack(capacity-weight[n-1], n-1, weight, values), knapsack(capacity, n-1, weight, values))


print(knapsack(20, 8, [5, 3, 1, 6, 8, 4, 11, 12], [2500, 1700, 1200, 3000, 4100, 2000, 7000, 7500]))

# def knapsack(capacity, n, weight, values):
#     m= {}
#
#     for c in range(capacity + 1):
#         m[(0, c)] = 0
#
#     for i in range(1, n + 1):
#         for c in range(capacity + 1):
#             if weight[i - 1] <= c:
#                 m[(i, c)] = max(m[(i-1, c)], values[i-1] + m[(i-1, c-weight[i-1])])
#             else:
#                 m[(i,c)] = m[(i-1, c)]
#
#     return m[(n, capacity)]
#
#
# print(knapsack(20,8,[5, 3, 1, 6, 8, 4, 11, 12], [2500, 1700, 1200, 3000, 4100, 2000, 7000, 7500]))