head = int(input("enter heads: "))
legs = int(input("enter legs: "))
x = (legs - 2 * head) // 2
y = head - x
print("Chicheks: ", y)
print("Rabbits: ", x)