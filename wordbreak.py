if len(word) < 34:
    if len(word) > 16:
        midpoint = 8
        while len(word[midpoint:]) > 16:
            midpoint = midpoint+1
        space = word.find(' ', midpoint)
        last = word[space+1:]
        first = word[:space]
        print(first); print(last)
    else:
       print(word)
else:
    print(len(word))
