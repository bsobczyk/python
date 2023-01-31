from itertools import  zip_longest

liczby=["1","2","3","4"]
litery=["a","b","c","d","e"]

for liczby,litery in zip(liczby,litery):
     print(liczby,litery)

# for liczby,litery in zip_longest(liczby,litery):
#     print(liczby,litery)

# for liczby,liter in zip(liczby,litery, strict=True):
#     print(liczby,litery)