def Reversing(size,array):
    reverse_array = array[::-1]
    for value in reverse_array:
        print(value,end=" ")


size = int(input(""))
array_input = input("")
split_input = array_input.split()
new_array = [int(num) for num in split_input]
Reversing(size,new_array)