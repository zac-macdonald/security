"""
Password restrictions, or password policies, are a way to ensure that passwords are "secure".
Many websties have password policies, to ensure that passwords are not too easy to guess.
However, these policies are not always more secure than letting the user choose their own password.
Password policies were initally created to ensure that passwords are not too easy to crack against a dictionary attack.
Now-a-days, dictionary attacks can be carried out against passwords and finished in a matter of seconds.

Here's an example senario:

    Mary is a bank teller who is using a password that is too easy to guess (like "password").
    She uses this password to log into her bank account. Assuming the bank stores their passwords encrypted,
    if an attacker were to access the bank's database, the attacker would be able to guess the password using
    a brute-force attack against the encrypted passwords using software like Hashcat.
    Generally, because of the complexity of Mary's password, the attacker would be able to guess the password in a very short amount of time.

    Enter the bank. The bank updates their password policies. Mary now needs a password that is at least
    8 characters in length, and contains three numbers. She can't use the password "carrot11" anymore,
    so she uses "p@s$w04d" instead.

    The problem here, is that even though she was forced to use a password that adheres to the bank's password policies,
    the attacker would still be able to guess the password using a brute-force attack because the password is still easy to guess.
    The password policy has also now made it easier, by narrowing the range of characters that can be used in cracking the password.
    You might be wondering to yourself, "But what if I just make a password that is harder to guess that adheres to the bank's password policies?"
    The majority of people would change their original password to meet the requirements of the new password policies, and in that case,
    It would increase password entropy, however, by assigning these rules, the password time to crack has been lowered, by removing
    the need to check for passwords without numbers, and that are under 8 characters long.
    Since password cracking is exponential, it saves a lot of time and effort by not having to check for passwords that are
    outside of the range of the password policies.

    To calculate the number of total unique passwords that can be created, we can use the following formula:

    Possible_Characters = 24
    Password_Length = 8
    Total_Passwords = Possible_Characters^Password_Length

    The formula above calculates the total number of unique passwords that can be created, given the number of possible characters,
    and the length of the password. 8 RTX-3090's can crack at 471.7 GH/s. (see https://www.onlinehashcrack.com/tools-benchmark-hashcat-nvidia-rtx-3090.php) 
    Which means, that if the password length is 8, and the number of possible characters is 24,
    The total combination of passwords for the given password length is 128063081718016.


"""
import numpy

def possible_characters(password):
    """
    Calculates the total number of possible characters that can be used in a password.
    """
    # Get the total number of possible characters
    L = len(password)
    # Get the total number of possible symbols (alphabet lower, and upper, and numbers)
    S = 94
    # Calculate the total number of possible characters
    possible_characters = S**L
    return possible_characters

pwd = []
for i in range(1, 13):
    pwd.append(chr(i))
    e = possible_characters(pwd)
    time = e/471700000000/2
    import datetime

    res = datetime.timedelta(seconds =time)

    print(f"{i}: {e}   :::   {res}")

d = 24986644000165537792/471700000000
print(datetime.timedelta(seconds =d))