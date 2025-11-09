from typing import List, Tuple
import heapq

#!/usr/bin/env python3
"""
0-1 Knapsack solver with two methods:
- Dynamic Programming (exact)
- Branch and Bound (best-first, exact with bounding)
Usage: import functions or run this file to see a simple example.
"""



def knapsack_dp(values: List[int], weights: List[int], capacity: int) -> Tuple[int, List[int]]:
    n = len(values)
    if n == 0 or capacity <= 0:
        return 0, []
    # DP table: (n+1) x (capacity+1)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        v = values[i - 1]
        w = weights[i - 1]
        for c in range(capacity + 1):
            if w <= c:
                dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - w] + v)
            else:
                dp[i][c] = dp[i - 1][c]
    # reconstruct chosen items
    res_value = dp[n][capacity]
    c = capacity
    chosen = []
    for i in range(n, 0, -1):
        if dp[i][c] != dp[i - 1][c]:
            chosen.append(i - 1)
            c -= weights[i - 1]
    chosen.reverse()
    return res_value, chosen


def _bound_for_sorted(values: List[float], weights: List[int], capacity: int, level: int, profit: float, weight: int) -> float:
    # fractional knapsack upper bound starting from 'level+1' in sorted arrays
    if weight >= capacity:
        return 0
    bound = profit
    totweight = weight
    n = len(values)
    j = level + 1
    while j < n and totweight + weights[j] <= capacity:
        totweight += weights[j]
        bound += values[j]
        j += 1
    if j < n:
        # take fraction
        bound += values[j] * (capacity - totweight) / weights[j]
    return bound


def knapsack_branch_and_bound(values: List[int], weights: List[int], capacity: int) -> Tuple[int, List[int]]:
    n = len(values)
    if n == 0 or capacity <= 0:
        return 0, []
    # sort by value/weight ratio descending and keep index mapping
    idx = list(range(n))
    idx.sort(key=lambda i: values[i] / weights[i], reverse=True)
    sv = [values[i] for i in idx]
    sw = [weights[i] for i in idx]

    # max-heap by bound (use negative for heapq)
    # heap entries: (-bound, level, profit, weight, taken_tuple)
    best_profit = 0
    best_taken = tuple([False] * n)
    heap = []
    root_bound = _bound_for_sorted(sv, sw, capacity, -1, 0, 0)
    heapq.heappush(heap, (-root_bound, -1, 0, 0, tuple([False] * n)))

    while heap:
        neg_bound, level, profit, weight, taken = heapq.heappop(heap)
        bound = -neg_bound
        if bound <= best_profit:
            continue
        next_level = level + 1
        if next_level >= n:
            continue
        # Branch: include next item
        w_in = weight + sw[next_level]
        p_in = profit + sv[next_level]
        taken_in = list(taken)
        taken_in[next_level] = True
        if w_in <= capacity and p_in > best_profit:
            best_profit = p_in
            best_taken = tuple(taken_in)
        bound_in = _bound_for_sorted(sv, sw, capacity, next_level, p_in, w_in)
        if bound_in > best_profit:
            heapq.heappush(heap, (-bound_in, next_level, p_in, w_in, tuple(taken_in)))
        # Branch: exclude next item
        bound_ex = _bound_for_sorted(sv, sw, capacity, next_level, profit, weight)
        if bound_ex > best_profit:
            taken_ex = tuple(taken)  # next remains False
            heapq.heappush(heap, (-bound_ex, next_level, profit, weight, taken_ex))

    # map taken from sorted order back to original indices
    chosen_sorted_indices = [i for i, taken_flag in enumerate(best_taken) if taken_flag]
    chosen_original = [idx[i] for i in chosen_sorted_indices]
    chosen_original.sort()
    return int(best_profit), chosen_original


if __name__ == "__main__":
    # Example
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50

    print("Items (value, weight):")
    for i, (v, w) in enumerate(zip(values, weights)):
        print(f" {i}: ({v}, {w})")
    print("Capacity:", capacity)

    dp_value, dp_items = knapsack_dp(values, weights, capacity)
    print("\nDynamic Programming result:")
    print(" Max value =", dp_value)
    print(" Items chosen =", dp_items)

    bnb_value, bnb_items = knapsack_branch_and_bound(values, weights, capacity)
    print("\nBranch and Bound result:")
    print(" Max value =", bnb_value)
    print(" Items chosen =", bnb_items)