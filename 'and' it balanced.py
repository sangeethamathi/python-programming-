t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_balanced(expression) == True:
        print("YES")
    else:
        print("NO")
