# 1)

def safe_call(f, *args):
    anot = f.__annotations__
    vars = args
    i = 0
    for v in anot:
        if type(vars[i]) is not anot[v]:
            raise Exception("Invalid parameters type: " + v)
        i += 1
    return f(*args)


def f(x: int, y: float, z):
    return x + y + z

# 2)
# the function to sort list type objects
# the objects are sorted bottom up
# each call create a new copy as to not the change the original x
def real_sort(x, tag1, tag2):
    if type(x) is type({'a': 1}):
        for i in x:
            x[i] = real_sort(x[i], tag1, tag2)   # sort inner elements
        tmp = {}
        for i in sorted(x):  # sort the dictionary
            tmp[i] = x[i]
        x = tmp
    elif type(x) is type([]):
        x = x.copy()
        for i in range(len(x)):
            x[i] = real_sort(x[i], tag1, tag2)
        x.sort()
    elif type(x) is type({'a'}):
        sorted_list = sorted(x)
        res = tag1 + str(sorted_list)[1:-1] + tag2 # list to string of set
        res = res.replace('\\\\', '\\')   # str() in sets creates escapes that print does not show
        res = res.replace('\\\'', '\'')   # so i removed them
        return res
    elif type(x) is type(()):
        for i in x:
            real_sort(i,tag1,tag2)
        x = tuple(sorted(x))
    return x


def print_sorted(x):
    size = len(str(x))
    tag1 = '!' * size  # tags to replace {} of the set string
    tag2 = '?' * size  # it is used to distinguish between the delimiters from string elements
    if type(x) in [type({'a': 1}), type([])]:
        obj = x.copy()
        res = str(real_sort(obj, tag1, tag2))
        res = res.replace("\""+tag1,'{')   # converts tags to delimiters
        res = res.replace(tag2+"\"", '}')
        res = res.replace("\'" + tag1, '{')
        res = res.replace(tag2 + "\'", '}')   # str() in sets creates escapes that print does not show
        res = res.replace('\\\'', '\'')       # so i removed them
        print(res)
        return res
    elif type(x) is type(()):
        tup = tuple(x)
        res = real_sort(tup, tag1, tag2)
        print(res)
        return str(res)
    elif type(x) is type({'a'}):  # sets can only hold primitives
        res = str(sorted(x))
        res = '{' + res[1:-1] + '}'
        print(res)
        return res
    else:
        print(x)
        return str(x)


# 3)

from scipy.misc import derivative


def find_root(f,a,b):
    if a > b:     # check for the upper limit
        max = a
        min = b
    elif a == b:
        raise Exception("root space must be greater than 0")
    else:
        max = b
        min = a
    res = max - f(max) / derivative(f,max) # calculate the root
    i = 0
    while res < min or res > max: # try until you find a fitting root
        i += 1
        res = res - f(res) / derivative(f,res)
        if i > 10000:
            raise Exception("could not find root")
    return res

# 4)
# https://www.codingame.com/training/medium/shadows-of-the-knight-episode-1
