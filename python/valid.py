def work(s):
    #note that the ds that you are working with is last in first out
    stack = []
    #first we are going to need some sort of ds that will allow for me to seperate the left from the right side into two elements
    brackets = {")":"(", "}":"{", "]":"["}

    for char in s:
        if char in "({[":
            #this is looking to see if we have run into an opening bracket
            stack.append(char)

        elif char in "]})":
            if not stack or stack.pop() != brackets[char]:
                return False
            
    return len(stack) == 0
            
    