print("Half Pyramid Pattern of starts(*): ")
n=int(input("Please enter number of rows: "))
for i in range(n):
    for j in range(i+1):
        print("*", end="$5")
    print()