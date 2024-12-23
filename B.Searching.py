def Searching(size,array,X):
    for i in range(0,size):
        if array[i]==X:
            print(i)
            return
    print(-1)
    return
            
array_size = int(input(""))
array_input = input("")
array_split = array_input.split()
array = [int(num) for num in array_split]
X_number = int(input(""))
Searching(array_size,array,X_number)