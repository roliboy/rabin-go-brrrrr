from modular_square_root import mod_sqrt
from codec import decode_blocks


# TODO: finish this
""" Decodes an rabin-encoded message, using the private key and the block sizes
('BED_HI', (31, 53), 3, 2) -> 'GAME'
"""
def decode(ciphertext, private_key, ciphertext_block_size, plaintext_block_size):
    decoded_blocks = decode_blocks(ciphertext, ciphertext_block_size)
    # first_block = decoded_blocks[0]
    # print(mod_sqrt(first_block, private_key[0]))
    # print(-mod_sqrt(first_block, private_key[0]))
    # print(mod_sqrt(first_block, private_key[1]))
    # print(-mod_sqrt(first_block, private_key[1]))    
    return decoded_blocks


# TODO: this
""" Encodes a plaintext message using the rabin cypher
"""
def encode():
    pass


# TODO: after implementing the encode and decode functions, we also need to look into padding for disambiguation
