import time
import math

from test_solution import test_solution

def is_prime(n):
    return len([i for i in range(2 , round(n/2)) if n%i == 0]) == 0

class PrimeCalculator():
    def __init__(self, upper_max):
        self.upper_max = upper_max

    def sieve(self):
        n_list = [n for n in range(2, self.upper_max)]
        primes = []
        for n in n_list:
            if len(n_list) == 0:
                return primes
            primes.append(n_list[0])
            n_list = [x for x in n_list[1:] if x % n != 0]
        return primes

    def sieve_not_append(self):
        n_list = [n for n in range(2, self.upper_max)]
        primes = []
        for ii in range(len(n_list)):
            if n_list[ii] == 0:
                continue
            if len(n_list) == 0:
                return primes
            primes.append(n_list[ii])
            for i in range(ii+1, len(n_list)):
                if n_list[ii] != 0 and n_list[i] % n_list[ii] == 0:
                    n_list[i] = 0
        return primes
        

    def sieve_hop(self):
        n_list = [n for n in range(2, self.upper_max)]
        primes = []
        for ii in range(len(n_list)):
            if n_list[ii] == 0:
                continue
            if len(n_list) == 0:
                return primes
            primes.append(n_list[ii])
            for i in range(ii, len(n_list), n_list[ii]):
                n_list[i] = 0
        return primes

    def get_primes_acc(self):
        primes = []
        for n in range(2, self.upper_max):
            div = False
            for p in primes: 
                if n % p == 0:
                    div = True
                    break
            if not div:
                primes.append(n)
        return primes


if __name__ == "__main__":
    upper_max = 1000 * 1000
    s = PrimeCalculator(upper_max)
    print(f"[+] Looking into {upper_max} ")

    
    print(f"[+] sieve solution")
    start_time = time.perf_counter()
    primes = s.sieve()
    end_time = time.perf_counter ()
    test_solution(primes, upper_max)
    print(f"[+] Took {end_time - start_time} seconds")

    print(f"[+] sieve solution hop")
    start_time = time.perf_counter()
    primes = s.sieve_hop()
    end_time = time.perf_counter ()
    test_solution(primes, upper_max)
    print(f"[+] Took {end_time - start_time} seconds")

    print(f"[+] accumulator solution")
    start_time = time.perf_counter()
    primes = s.get_primes_acc()
    end_time = time.perf_counter ()
    test_solution(primes, upper_max)
    print(f"[+] Took {end_time - start_time} seconds")