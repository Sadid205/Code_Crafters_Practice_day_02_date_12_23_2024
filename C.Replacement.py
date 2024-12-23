def Replacement(size,array):
    for i in range(0,size):
        if(array[i]>0):
            array[i]=1
        if(array[i]<0):
            array[i]=2
    for value in array:
        print(value, end=' ')



size = int(input(""))
array_input = input("")
split_input = array_input.split()
new_array = [int(num) for num in split_input]
Replacement(size,new_array)