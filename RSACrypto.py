def rsa_encrypt(plain_text, public_key):
    n, e = public_key
    # 将每个字符转换为其ASCII值
    encoded_text = [ord(c) for c in plain_text]
    # 将ASCII列表转换为无符号整数
    number = int.from_bytes(encoded_text, byteorder='big', signed=False)
    return pow(number, e, n)


def rsa_decrypt(cipher, private_key):
    n, d = private_key
    number = pow(cipher, d, n)
    # 将整数转换为字节数组
    print(number)
    encoded = number.to_bytes((number.bit_length() + 7) // 8, byteorder='big')
    # 将每个字节转换为对应的字符
    plaintext = "".join([chr(b) for b in encoded])
    return plaintext
