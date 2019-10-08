
def convert(number):
    l = list(number)
    len_l = len(l)
    n = len_l

    while(n):
        if n%3 == 0:
            l.insert(n-1,",") 
        n -=1
    print('#'.join(l))


convert("12345324")