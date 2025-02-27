def can_make_hamburgers(count, recipe, have, prices, money):
    need = {'B': recipe.count('B'), 'S': recipe.count('S'), 'C': recipe.count('C')}
    
    total_money_needed = 0
    for ing in ['B', 'S', 'C']:
        total_needed = need[ing] * count
        if total_needed > have[ing]:
            to_buy = total_needed - have[ing]
            cost = to_buy * prices[ing]
            if cost > money:
                return False
            total_money_needed += cost
            if total_money_needed > money:
                return False
    return True

def max_hamburgers(recipe, pantry, prices, money):
    ing_map = {'B': 0, 'S': 1, 'C': 2}
    have = {ing: pantry[ing_map[ing]] for ing in ['B', 'S', 'C']}
    
    left = 0
    max_possible = 0
    for ing in ['B', 'S', 'C']:
        count_needed = recipe.count(ing)
        if count_needed > 0:
            have_amount = pantry[ing_map[ing]]
            can_buy = money // prices[ing_map[ing]]
            possible = (have_amount + can_buy) // count_needed
            if max_possible == 0 or possible < max_possible:
                max_possible = possible
    
    right = max_possible + 1  # Fixed indentation
    
    while left < right:
        mid = (left + right) // 2
        if can_make_hamburgers(mid, recipe, have, prices, money):
            left = mid + 1
        else:
            right = mid
    
    return left - 1  # Fixed indentation

# Input handling
recipe = input().strip()
pantry = list(map(int, input().split()))
prices = list(map(int, input().split()))
money = int(input())
result = max_hamburgers(recipe, pantry, prices, money)
print(result)