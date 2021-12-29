from modular_square_root import mod_sqrt
from codec import decode_blocks, encode_blocks, double_letters_in_block, string_representation, check_doubling, de_double
from mod_inverse import mod_inverse

# TODO: finish this
""" Decodes an rabin-encoded message, using the private key and the block sizes
('BED_HI', (31, 53), 3, 2) -> 'GAME'
"""
def decode(ciphertext, private_key, ciphertext_block_size, plaintext_block_size):
    decoded_blocks = decode_blocks(ciphertext, ciphertext_block_size)

    result = ""

    for block in decoded_blocks:
        N1, N2 = private_key
        K1 = mod_inverse(N1, N2)
        K2 = mod_inverse(N2, N1)

        N = N1 * N2

        sol2 = mod_sqrt(block, N1)
        sol1 = mod_sqrt(block, N2)

        values = [
            (N1*K1*sol1 + N2*K2*sol2) % N,
            (-N1*K1*sol1 + N2*K2*sol2) % N,
            (N1*K1*sol1 - N2*K2*sol2) % N,
            (-N1*K1*sol1 - N2*K2*sol2) % N]

        for value in values:
            if value > 27**plaintext_block_size:
                continue

            text = string_representation(value, plaintext_block_size)
            if check_doubling(text, plaintext_block_size):
                result += de_double(text, plaintext_block_size)
                break

    return result


# TODO: this
""" Encodes a plaintext message using the rabin cypher
"""
def encode(plaintext, public_key, ciphertext_block_size, plaintext_block_size):
    plaintext = double_letters_in_block(plaintext, plaintext_block_size)

    chunks = decode_blocks(plaintext, plaintext_block_size)
    chipher_chunks = list(map(lambda x: x**2 % public_key, chunks))

    ciphertext = encode_blocks(chipher_chunks, ciphertext_block_size)
    return ciphertext
    