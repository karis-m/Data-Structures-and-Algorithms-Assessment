def remove_duplicates(input_sequence):
    print("The original list is as follows:" + str(input_sequence))
    #removing duplicates 
    result = list(set(input_sequence)) 
    # 
    print("The list after the duplicates have been removed:" + str(result))

if __name__ == "__main__":
	input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
	# calling the function
	remove_duplicates(input_sequence)