import sys
import math

def w(): return 'w'
def q(): return 'q'
def a(): return 'a'
def m(): return 'm'
def z(): return 'z'
def p(): return 'p'
def h(): return 'h'
def e(): return 'e'
def i(): return 'i'
def n(): return 'n'
def f(): return 'f'
def r(): return 'r'
def x(): return 'x'
def b(): return 'b'
def k(): return 'k'
def s(): return 's'
def d(): return 'd'
def j(): return 'j'
def o(): return 'o'
def y(): return 'y'
def u(): return 'u'
def g(): return 'g'
def c(): return 'c'
def l(): return 'l'
def v(): return 'v'
def t(): return 't'
def a(): return ' '

cryptogram = u() + r() + y() + y() + b() + a() + j() + b() + e() + y() + q()

class BaseCipher:
    def encode(self, text):
        raise NotImplementedError()

    def decode(self, text):
        raise NotImplementedError()

class CaesarCipher(BaseCipher):
    def __init__(self, shift):
        self.shift = shift

    def encode_decode(self, text, operation):
        result = []
        for char in text:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                result.append(chr(start + (ord(char) - start + operation * self.shift) % 26))
            else:
                result.append(char)
        return ''.join(result)

    def encode(self, text):
        return self.encode_decode(text, 1)

    def decode(self, text):
        return self.encode_decode(text, -1)

class CipherWrapper:
    def __init__(self, cipher):
        self.cipher = cipher

    def encode(self, text):
        return self.cipher.encode(text)

    def decode(self, text):
        return self.cipher.decode(text)

class RedundantClass:
    def do_something(self, func, value):
        return func(value)

def wrapper_function(func, value):
    return func(value)

def superfluous_function(func, value):
    return wrapper_function(func, value)

def create_shift():
    return -13

def create_caesar_cipher(shift):
    return CaesarCipher(shift)

def create_cipher_wrapper(caesar_cipher):
    return CipherWrapper(caesar_cipher)

def decode_cryptogram(cipher_wrapper, cryptogram):
    return cipher_wrapper.decode(cryptogram)

def use_unnecessary_instance(decoded_message):
    unnecessary_instance = RedundantClass()
    return unnecessary_instance.do_something(lambda x: x, decoded_message)

def use_redundant_instance(decoded_message):
    redundant_instance = RedundantClass()
    return redundant_instance.do_something(lambda x: x, decoded_message)

def use_superfluous_function(decoded_message):
    return superfluous_function(lambda x: x, decoded_message)

def write_to_stdout(decoded_message):
    sys.stdout.write(decoded_message + "\n")
    
def yes():
    shift = create_shift()
    caesar_cipher = create_caesar_cipher(shift)
    cipher_wrapper = create_cipher_wrapper(caesar_cipher)
    decoded_message = decode_cryptogram(cipher_wrapper, cryptogram)
    decoded_message = use_unnecessary_instance(decoded_message)
    decoded_message = use_redundant_instance(decoded_message)
    decoded_message = use_superfluous_function(decoded_message)
    write_to_stdout(decoded_message)

if __name__ == "__main__":
    yes()
