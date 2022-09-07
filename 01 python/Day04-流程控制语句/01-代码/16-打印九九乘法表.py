j = 0
while j < 9:
    j += 1  # j = 3;
    i = 0  # i=0;
    while i < j:
        i += 1  # i=2;
        print(i, '*', j, '=', (i * j), sep="", end="\t")
    print()
