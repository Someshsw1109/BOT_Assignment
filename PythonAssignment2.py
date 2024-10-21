from functools import lru_cache

class PrimeFactorizer:
    def __init__(self):
        self.factors = []

    @lru_cache(maxsize=None)
    def factorize(self, n):
        if n <= 1:
            return []
        
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return [(i, 1)] + self.factorize(n // i)
        
        return [(n, 1)]

    def prime_factorization(self, n):
        self.factors = self.factorize(n)
        return self.combine_factors()

    def combine_factors(self):
        combined = {}
        for factor, exponent in self.factors:
            combined[factor] = combined.get(factor, 0) + exponent
        return [(factor, exponent) for factor, exponent in combined.items()]

    @staticmethod
    def get_number_input(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a positive integer.")

    def run(self):
        while True:
            number = self.get_number_input("Enter a number to factorize (or 0 to exit): ")
            if number == 0:
                print("Exiting the program. Goodbye!")
                break
            if number < 0:
                print("Please enter a positive integer.")
                continue
            
            factors = self.prime_factorization(number)
            print(f"Prime factorization of {number}: {factors}")


if __name__ == "__main__":
    factorizer = PrimeFactorizer()
    factorizer.run()