from RSAGenerator import miller_rabin
from RSAGenerator import generate_prime
from RSAGenerator import generate_key
from RSACrypto import rsa_encrypt, rsa_decrypt
import time

# start_time = time.perf_counter()
# for i in range(10):
#     generate_prime(3072)
# end_time = time.perf_counter()

# print("代码执行时间为:", end_time - start_time, "秒")

plain_text = "I love crypto!"
public_key, private_key = (222349984549928269711208533854767328313, 11601824759722370529),(222349984549928269711208533854767328313, 146282193007944228814703292109633864481)
cipher = rsa_encrypt(plain_text, public_key)
answer = rsa_decrypt(cipher, private_key)
print(cipher)
print(answer)