import copy

def pascal_triangle(n):
    list = [[1]]
    line_list = [[1]]

    while len(list) <= n:
        temp_list = []

        for i in range(len(line_list)+1):
            if i == 0 or i == (len(line_list)):
                elem = 1
                temp_list.append(elem)
                    
            else:
                elem = line_list[i-1] + line_list[i]
                temp_list.append(elem)

        list.append(temp_list)
        line_list = copy.copy(temp_list)
    
    return list


pascal_list = (pascal_triangle(4))

print(pascal_list)
n = len(pascal_list) 

for i in range(n):
    print(' ' * (n - 1 - i), end='')

    for j in range(len(pascal_list[i])):
        print(pascal_list[i][j], end=' ')
    
    print()