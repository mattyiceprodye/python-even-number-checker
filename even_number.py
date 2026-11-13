def count_up(numbers: list[int])-> tuple[int, list[int]]:
    count = 0
    even_numbers = []
    for num in numbers:
        if num % 2 ==0:
            count += 1
            even_numbers.append(num)
    return count, even_numbers

choice = "yes"
while choice == "yes":
    numbers = []
    for i in range (6):
        num = int(input("Enter a  number: "))
        numbers.append(num)
    total, evens = count_up(numbers)
    print(f"There are {total} even numbers.")
    print(f"The even numbers are {evens}!")
    choice = input("Would you like to keep goin?: ")
print("Goodbye, Thanks for checking the code out!")

            
