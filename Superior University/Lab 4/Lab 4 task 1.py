def luhn_check(card_number):
    total = 0
    digits = [int(d) for d in str(card_number)][::-1]

    for i in range(len(digits)):
        if i % 2 == 1:  
            digits[i] *= 2
            if digits[i] > 9:  
                digits[i] -= 9
        total += digits[i]

    return total % 10 == 0

card_number = input("Enter a credit card number: ")
if luhn_check(card_number):
    print("Valid card number.")
else:
    print("Invalid card number.")
