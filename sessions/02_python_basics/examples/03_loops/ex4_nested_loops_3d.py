x_size = 10
y_size = 6
z_size = 5

list_x = list(range(x_size))
list_y = list(range(y_size))
list_z = list(range(z_size))

new_list = []

# add code for 3rd dimension
for i in list_x:
    for j in list_y:
        for k in list_z:
            if i == 0:
                pass
            elif j == 5:
                pass
            else:
                new_list.append(i)
                new_list.append(j)
                new_list.append(k)

print(new_list)