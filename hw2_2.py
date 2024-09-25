girls = ["Kate", "Anna", "Elena"]
boys = ["John", "Mark"]

if len(girls) == len(boys):
    sorted_girs = sorted(girls)
    sorted_boys = sorted(boys)
    result = list(zip(sorted_boys, sorted_girs))
    for i in range(len(girls)):
        print(f"{result[i][0]} и {result[i][1]}")
else:
    print("Внимание, кто-то может остаться без пары.")