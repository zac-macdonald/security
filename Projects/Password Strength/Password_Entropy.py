import numpy
"""
Entropy is the foundation upon which all cryptographic functions operate.
They are a measure of the randomness or diversity of a data-generating function.

Password Entropy can be crudely calculated by calulating with the following expressions, L, S, and C:

L = length of password
S = The total pool of unique possible symbols, or sets of characters, for example:
    - Lower English alphabet (abcdefghijklmnopqrstuvwxyz): 26
    - Upper English alphabet (ABCDEFGHIJKLMNOPQRSTUVWXYZ): 26
    - Special characters (!@#$%^&*()_+-=[]{}|;':",.<>/?`~ ): 32
    - Numbers (0123456789): 10
    - All of the above combined: 94
Note: Most websites/apps do not allow for non-english characters, so we won't include them.

To get the total number of possible symbols, we get S to the power of L (S^L).

We can then calculate the password entropy by:
log(S^L)

It's important to understand that most of the time, when passwords are being brute-forced,
the attacker will not (generally) statistically require all of the possible symbols to be used, 
to get the password. To combat this, and give a more accurate measure of the password entropy,
we can divide the password entropy by 2, so the new function is:

log(S^L)/2) 

=========================================================================================

"""
def BasicEntropy(password):
    """
    Calculates the basic entropy of a password.
    """
    # Get the length of the password
    L = len(password)
    # Get the total number of possible symbols
    S = 94
    # Calculate the password entropy given the length and total number of possible symbols
    entropy = numpy.log(numpy.power(S,L))/2

    return entropy