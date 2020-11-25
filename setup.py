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

# Local imports
from prime import generate_p_and_q


def get_p_and_q(n):
    """ Secretely choose two distinct prime numbers. 

    Args:
        n (int): Max limit of prime range to choose from.

    Returns:
        tuple: The two distinct prime integer values.
    """
    p, q = generate_p_and_q(n)
    return p, q


def calculate_n(p, q):
    """ Calculate the value of n.

    Args:
        p (int): Distinct prime integer.
        q (int): Distinct prime integer.

    Returns:
        int: [description]
    """
    n =  p * q
    return n


def calculate_phi(p, q):
    """ Calculate Euler's phi function.

    Args:
        p (int): Distinct prime integer.
        q (int): Distinct prime integer.

    Returns:
        int: Euler's phi function.
    """
    phi = (p - 1) * (q - 1)
    return phi


def calculate_invertible_element(n):
    """ Calculates an invertible element whithin the natural set of phi.

    Args:
        n (int): Max limit of prime range to choose from.

    Returns:
        int: Invertible element 
    """
    e = 0
    return e


if __name__ == "__main__":
    import doctest
    doctest.testmod()