def work(s):
    #note that the ds that you are working with is last in first out

    #first we are going to need some sort of ds that will allow for me to seperate the left from the right side into two elements
    brackets = {")":"(", "}":"{", "]":"["}

    