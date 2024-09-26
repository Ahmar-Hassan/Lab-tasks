def fizz_buzz_with_stack(n):
    stack = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            stack.append("Fizz Buzz")
        elif i % 3 == 0:
            stack.append("Fizz")
        elif i % 5 == 0:
            stack.append("Buzz")
        else:
            stack.append(str(i))
    
    while stack:
        print(stack.pop())

while True:
    n = int(input("Enter a number to play Fizz Buzz up to: "))
    fizz_buzz_with_stack(n)

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
