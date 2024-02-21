#14/02/24

#for loop
words = ["today","is","Valentine's","day"]

for word in words:
    print("The Word is:", word)
    print("The length of the word is:", len(word))

newWords = print(words.sort())
print(words)



# write a script using for loop to print a fibonacci series

def fibonacci_series (length):
    fibonacci_series = [0]
    if length <= 0:
        return fibonacci_series
    elif length == 1:
        fibonacci_series.append(0)
        return fibonacci_series
    else:
        fibonacci_series = [0,1]
        for i in range(2,length):
            next_num = fibonacci_series[-1] + fibonacci_series[-2]
            fibonacci_series.append(next_num)
        return fibonacci_series
    
def main():
    print("Welcome to the Fibonacci series generator!")
    length = int(input("Enter the length of the Fibonacci series: "))

    series = fibonacci_series(length)

    if len(series) > 0:
        print("The Fibonacci series of length {}:".format(length))
        for num in series:
            print(num, end=" ")
        print()
    else:
        print("Please enter a positive integer for the length of the Fibonacci series.")

if __name__ == "__main__":
    main()  


# To check wether the number is even or odd.
    
n = int(input("Enter the number"))

if (n == 9):
    print("Exception")
elif(n%2 == 0):
    print("Even")
else:
    print("Odd")
#14/02/24

#for loop
words = ["today","is","Valentine's","day"]

for word in words:
    print("The Word is:", word)
    print("The length of the word is:", len(word))

newWords = print(words.sort())
print(words)



# write a script using for loop to print a fibonacci series

def fibonacci_series (length):
    fibonacci_series = [0]
    if length <= 0:
        return fibonacci_series
    elif length == 1:
        fibonacci_series.append(0)
        return fibonacci_series
    else:
        fibonacci_series = [0,1]
        for i in range(2,length):
            next_num = fibonacci_series[-1] + fibonacci_series[-2]
            fibonacci_series.append(next_num)
        return fibonacci_series
    
def main():
    print("Welcome to the Fibonacci series generator!")
    length = int(input("Enter the length of the Fibonacci series: "))

    series = fibonacci_series(length)

    if len(series) > 0:
        print("The Fibonacci series of length {}:".format(length))
        for num in series:
            print(num, end=" ")
        print()
    else:
        print("Please enter a positive integer for the length of the Fibonacci series.")

if __name__ == "__main__":
    main()  


# To check wether the number is even or odd.
    
n = int(input("Enter the number"))

if (n == 9):
    print("Exception")
elif(n%2 == 0):
    print("Even")
else:
    print("Odd")