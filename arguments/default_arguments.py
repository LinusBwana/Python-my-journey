# default arguments = a default value for certain parameters
# used when the argument is omitted
# makes the function more flexible, reduces # of arguments
# 1. positional
# 2. DEFAULT
# 3. keyword
# 4. arbitrary

# function(positional_args, *args, keyword_args, **kwargs)


# example1
def net_price(list_price, discount=0, tax=0.05):
    print(list_price, discount, tax)
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 0.1, 0))