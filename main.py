from RSAGenerator import miller_rabin
from RSAGenerator import generate_prime
from RSAGenerator import generate_key
from RSACrypto import rsa_encrypt, rsa_decrypt, rsa_optimize_decrypt
import time
import threading

# start_time = time.perf_counter()
# for i in range(10):
#     generate_prime(3072)

plain_text = "I love crypto!"
public_key, private_key, optimized_private_key = generate_key(1024)
cipher = rsa_encrypt(plain_text, public_key)
start_time = time.perf_counter()
answer = rsa_decrypt(cipher, private_key)
# answer = rsa_optimize_decrypt(cipher, optimized_private_key)
end_time = time.perf_counter()
print("代码执行时间为:", end_time - start_time, "秒")
print(cipher)
print(answer)