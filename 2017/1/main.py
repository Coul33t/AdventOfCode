def captcha(digits):
    cumsum = 0
    for i, _ in enumerate(digits):
        if i < len(digits) - 1:
            if digits[i] == digits[i+1]:
                cumsum += int(digits[i])
        else:
            if digits[0] == digits[-1]:
                cumsum += int(digits[0])

    return cumsum

def captcha2(digits):
    cumsum = 0
    n = int(len(digits)/2)

    for i, _ in enumerate(digits):
        if i < len(digits) - n - 1:
            if digits[i] == digits[i+n]:
                cumsum += int(digits[i])

        else:
            if digits[i] == digits[i-n]:
                cumsum += int(digits[i])
    
    return cumsum

if __name__ == '__main__':
    with open('input.txt', 'r') as input_file:
        digits = input_file.read()
        print(captcha(digits))
        print(captcha2(digits))