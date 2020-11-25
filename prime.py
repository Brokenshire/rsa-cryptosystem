# Copyright 2020 Jack Brokenshire

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Third-party import(s)
import random


class Prime():

    def __init__(self, p, q, size):
        self.p = p
        self.q = q
        self.size = size
        self.get_p_and_q(size)


    def is_prime(self, n):
        """ Fermat primality test.

        Args:
            n (int): Value to be tested for primality.
        """
        if n <= 3:
            return n > 1
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i ** 2 <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True


    def generate_small_prime(self):
        self.is_prime()


    def generate_big_prime(self):
        self.is_prime()
        

    def get_p_and_q(self, size):
        """ Gets the values of p and q determined by the size of the prime wanted.

        Args:
            size (int): 0 for small prime and 1 for big prime.
        """
        if size == 0:
            self.p = self.generate_small_prime()
            self.q = self.generate_small_prime()
        else:
            self.p = self.generate_big_prime()
            self.q = self.generate_big_prime()


def main():
    

if __name__ == "__main__":
    main()