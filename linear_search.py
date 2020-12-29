#Searching algorithm:
#Linear Search


#Function for linear search nd it returns Index of element if it is in data.
def linear_search(data,search):
	if search in data:
		for i in range(len(data)):
			if data[i] == search:
				return i;
	else:
		print("Sorry. Element not available")

	
#Execution start from here.
if __name__ == "__main__":
	data = []
	size = int(input("How many elements you want to enter : "))
	
	print("\n---------- INITIALIZING ------------")
	for i in range(size):
		temp = int(input(f"Enter element { i+1 } : "))
		data.append(temp)
		
	search=int(input(f"\nEnter element for Search : "))
	answer = linear_search(data,search)
	print(f"Successfully Find element at the index of : { answer }")
		
	
