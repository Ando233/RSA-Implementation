# Miller-Rabin Test
import random
from preprocess import low_primes
from RSAMath import gcd, get_mod_inverse


def miller_rabin(n, trials=5):
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # 解出s,d
    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    for _ in range(trials):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def is_prime(n):
    for prime in low_primes:
        if n % prime == 0:
            return False
    return miller_rabin(n)


def generate_prime(key_size=1024):
    num = random.randrange(1 << (key_size - 1), 1 << key_size)
    if num % 2 == 0:
        num = num + 1
    while not is_prime(num):
        num = num + 2
    return num


def generate_key(key_size):
    # Step 1: Create two prime numbers, p and q. Calculate n = p * q.
    # print('Generating p prime...')
    p = generate_prime(key_size)
    # print('Generating q prime...')
    q = generate_prime(key_size)
    n = p * q
    # Step 2: Create a number e that is relatively prime to (p-1)*(q-1).
    # print('Generating e that is relatively prime to (p-1)*(q-1)...')
    while True:
        e = random.randrange(1 << (key_size - 1), 1 << key_size)
        if gcd(e, (p - 1) * (q - 1)) == 1:
            break

    # Step 3: Calculate d, the mod inverse of e.
    # print('Calculating d that is mod inverse of e...')
    d = get_mod_inverse(e, (p - 1) * (q - 1))
    publicKey = (n, e)
    privateKey = (n, d)
    # print('Public key:', publicKey)
    # print('Private key:', privateKey)
    # Step 4: Optimize
    d_p = get_mod_inverse(e, p - 1)
    d_q = get_mod_inverse(e, q - 1)
    q_Inv = get_mod_inverse(q, p)
    optimizedPrivateKey = (d_p, d_q, q_Inv, p, q)
    return publicKey, privateKey, optimizedPrivateKey
