"""
## Password Policies, and why I do not like them.

**Password restrictions, or password policies, are a way to ensure that passwords are "secure".
Many websties have password policies, to ensure that passwords are not too easy to guess.
However, these policies are not always more secure than letting the user choose their own password.
Password policies were initally created to ensure that passwords are not too easy to crack against a dictionary attack.
Now-a-days, dictionary attacks can be carried out against passwords and finished in a matter of seconds.**

### Here is an example senario:

Mary is a bank teller who is using a password that is too easy to guess: _"password"_. 
Assuming the bank stores their passwords with a hashing algoritm, if an attacker were to access the bank's database, the attacker would be able to guess the password using a basic brute-force attack against the hashed passwords using software like Hashcat. Generally, because of the incomplexity of Mary's password, the attacker would be able to guess the password instantly.

The bank then updates their password policies. Mary now needs a password that is at least: 
- 8 characters in length
- contains three numbers

She can not use the password "password" anymore because it does not adheer to the policy, so she uses "password111" instead. The problem with this is that obviously, the password is still quite easy to guess. Humans by nature take the path of least resistance, hence the subtle change in the password.

An attacker now wants to hack the bank again, and this time, the attacker sees the new password policy. Instead of the attacker trying to brute force a password with all combinations of characters, less than the length of 8, the attacker can try to brute force the password with all combinations of characters, more than the length of 8, and also contains three numbers. To put it simply, the attacker has just narrowed the amount of passwords that they have to check, making it easier for the attacker to crack the password.

To calculate the number of total unique passwords that can be created, we can use the following equation:

	Possible Characters ^ Password Length

The equation above calculates the total number of unique passwords that can be created, given the number of possible characters, and the length of the password.

8 RTX-3090's can crack an MD5 hash at 471.7 GH/s. (see https://www.onlinehashcrack.com/tools-benchmark-hashcat-nvidia-rtx-3090.php) which means, that if the password **length is 8**, the number of **possible characters is 94** and **total combination of passwords** for the given password length **is 6095689385410816**, the time it would take to crack the password, is roughly around **1 hour and 45 minutes**.
"""

import datetime

def possible_characters(password):
    L = len(password)
    S = 94
    return S**L

def password_time(password, max):
    pwd = []
    for i in range(1, max):
        pwd.append(chr(i))
        e = possible_characters(pwd)
        # 471.7 GH/s > 47170000000
        # we devide by 2 because in a brute force attack,
        # if the attacker gets to 50% of the total possible passwords,
        # and it has not yet cracked the password, they will have an
        # increasing chance of cracking the password after each guess.
        time = e/471700000000/2
        res = datetime.timedelta(seconds =time)
        print(f"{i}: {e}   :::   {res}")

if __name__ == '__main__':
    pwd = input("Enter a password: ")
    password_time(input, 94)
