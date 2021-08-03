def fizz_buzz(num: int) -> str:
    if num % 15 == 0:
        return "FizzBuzz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "Fiz"
    else:
        return str(num)

if __name__ == '__main__':
    for i in range(1, 31):
        print(fizz_buzz(i))