def summation(size,arr):
    total=0
    for num in arr:
        total+=num
    if total<0:
        total=total*-1
    print(total)

array_size_input = int(input(""))
array_items_input = input("")
input_split = array_items_input.split()
input_array = [int(num) for num in input_split]
summation(array_size_input,input_array)
