def print_table_of_5():
    # Display the header
    print("Multiplication Table of 5:")
    
    # Display the table
    for i in range(1, 11):
        result = 5 * i
        print(f"5 x {i} = {result}")

# Call the function to print the table
print_table_of_5()