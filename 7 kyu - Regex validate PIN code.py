'''
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

Examples:
validate_pin("1234") == True
validate_pin("12345") == False
validate_pin("a234") == False
'''

numbers = '0123456789'

def validate_pin(pin):
    pin = list(pin)
    for i in pin:
        if not i in numbers:
            return False
    if len(pin) == 4 or len(pin) == 6:
        return True
    return False