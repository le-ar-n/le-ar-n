anything = []
x_size = 10
y_size = 6

for i in range(x_size):
    for j in range(y_size):
        anything.append((i, j))
        print(anything)
else:
    print(x_size * y_size, "points have been generated")
    print(points)