from ashu import timer

def is_prime(number,prime_list):
    for prime in prime_list:
        if number % prime == 0:
            return False
    prime_list.append(number)
    return True
@timer    
def euler():
    i = 3
    prime_list = [2]
    while(i < 2000000):
        is_prime(i,prime_list)
        i = i+1
    return sum(prime_list)

if __name__ == '__main__':
    print euler()
