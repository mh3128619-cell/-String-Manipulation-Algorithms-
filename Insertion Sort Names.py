names = ["Moustafa", "Ahmed", "Ziad", "Hany"]

for i in range(1, len(names)):
    key = names[i]
    j = i - 1
    while j >= 0 and names[j] > key:
        names[j + 1] = names[j]
        j -= 1
    names[j + 1] = key

print(f"Sorted names: {names}")
