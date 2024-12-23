def Position(size,array):
    for i in range(0,size):
        if(array[i]<=10):
            print(f"A[{i}] = {array[i]}")

size = int(input(""))
array_input = input("")
split_input = array_input.split()
new_array = [int(num) for num in split_input]
Position(size,new_array)