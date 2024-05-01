def add_comma(alist):
    res = ''
    
    for elems in alist:
        if elems == alist[-1]:
            res += 'and ' + elems
        else:
            res += elems + ', '
    return res

spam = ['apples', 'bananas', 'tofu', 'cats']
print(add_comma(spam))
