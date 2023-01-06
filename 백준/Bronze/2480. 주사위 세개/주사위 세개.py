a, b, c = map(int, input('').split(' '))

list_variable = [a, b, c]
dict_variable = {}

for num in list_variable:
    if num in dict_variable:
        dict_variable[num] += 1
    else:
        dict_variable[num] = 1

sort_dict = sorted(dict_variable)

reverse_key_value = {v:k for k, v in dict_variable.items()}

if len(dict_variable) == 1:
    price = 10000 + reverse_key_value.get(3) * 1000
elif len(dict_variable) == 2:
    price = 1000 + reverse_key_value.get(2) * 100
else:
    price = sort_dict.pop() * 100

print(price)