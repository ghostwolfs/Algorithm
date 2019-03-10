def max_subarray(array):
    boundry = array[0]
    maxvalue = array[0]
    for i in range(1,len(array)):
        if boundry + array[i] > array[i]:
            boundry += array[i]
        else:
            boundry = array[i]
            
        if boundry > maxvalue:
            maxvalue = boundry
    return maxvalue


a = [1,-2,3,10,-4,7,2,-48]
print(max_subarray(a))