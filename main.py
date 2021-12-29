#!/usr/bin/env python

from keygen import generate_keys
from codec import get_block_sizes
from rabin import decode

# public_key, private_key = generate_keys(16)
public_key, private_key = 31 * 53, (31, 53)
plaintext_block_size, ciphertext_block_size = get_block_sizes(public_key)

ciphertext = "BED_HI"
plaintext = decode(ciphertext, private_key, ciphertext_block_size, plaintext_block_size)

print(plaintext)
