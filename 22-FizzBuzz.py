# https://www.coderbyte.com/editor/FizzBuzz:Python#
# Difficulty Easy 
# Took care of my exceptions first
# Feb 1

def FizzBuzz(num):
    result = ''
    for x in range(1, num+1):
        if x % 3 == 0 and x % 5 == 0:
            result += 'FizzBuzz' + ' '
        elif x % 3 == 0:
            result += 'Fizz' + ' '
        elif x % 5 == 0:
            result += 'Buzz' + ' '
        else:
            result += str(x) + ' '

    return result

# keep this function call here  
print FizzBuzz(raw_input())
