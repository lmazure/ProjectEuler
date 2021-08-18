max = 999
found = 1
for i in range(1, max+1):
    for j in range(1, i+1):
        product = i * j
        strg = str(product)
        if (strg == strg[::-1]) and (product > found):
            found = product
print(found)