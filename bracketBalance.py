
# Question 1
# function to check if brackets are balanced
def is_balanced(expression):
	stack = []

    # Pushing and checking if elements are in the stack 
	for element in expression:
		if element in ["(", "{", "["]:

			stack.append(element)
		else:
            # checking the corresponding element
			if not stack:
				return False
			current_element = stack.pop()
			if current_element == '(':
				if element != ")":
					return False
			if current_element == '{':
				if element != "}":
					return False
			if current_element == '[':
				if element != "]":
					return False

	# Check Empty Stack
	if stack:
		return False
	return True



if __name__ == "__main__":
	expression = "{()}[]"

	# calling the function
	if is_balanced(expression):
		print("True")
	else:
		print("False")


