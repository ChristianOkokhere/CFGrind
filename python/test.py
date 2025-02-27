def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_good(n):
    s = str(n)
    for i in range(len(s) - 2):
        window = int(s[i:i+3])
        if is_prime(window):
            return False
    return True

def solve_full_range():
    MOD = int(1e9 + 7)
    total = 0
    count = 0
    
    # Calculate for 4-digit numbers
    for num in range(1000, 10000):
        if is_good(num):
            total = (total + num) % MOD
            count += 1
    
    print(f"Found {count} good numbers")
    return total

result = solve_full_range()
print(f"Final sum mod 1e9+7: {result}")