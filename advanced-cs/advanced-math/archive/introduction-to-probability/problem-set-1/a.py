from functools import cache


@cache
def count_ways(n, s):
    if s == 0 and n == 0:
        return 1  
    if s < 0 or n == 0:
        return 0  
    total_ways = 0
    for face in range(1, 7):
        total_ways += count_ways(n - 1, s - face)
    
    return total_ways


ways_to_21 = count_ways(4, 21)
ways_to_22 = count_ways(4, 22)
total_possibilities = 6 ** 4

prob_21 = ways_to_21 / total_possibilities
prob_22 = ways_to_22 / total_possibilities

print(f"Ways to get 21: {ways_to_21}, Probability: {prob_21:.5f}")
print(f"Ways to get 22: {ways_to_22}, Probability: {prob_22:.5f}")