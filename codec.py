from itertools import count


charset = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"


""" Returns the numeric equivalent of a character
('A') -> 1
charset = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
"""
def decode(char):
    return charset.find(char.upper())


""" Returns the character corresponding to a numeric value
(1) -> 'A'
charset = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
"""
def encode(val):
    return charset[val]


""" Returns the block sizes for plaintext and ciphertext, given a key,
such that 27^k < n < 27^l, assuming a 27 character charset
(31 * 53) -> 2, 3
"""
def get_block_sizes(key):
    plaintext_block_size = next(
        x for x in count() if
            len(charset) ** x < key <= len(charset) ** (x + 1))
    ciphertext_block_size = next(
        x for x in count() if
            len(charset) ** x > key >= len(charset) ** (x - 1))
    return plaintext_block_size, ciphertext_block_size


""" Splits a sequence into chunks of a given size
('ayylmao', 2) -> ['ay', 'yl', 'ma', 'o']
"""
def split_into_chunks(sequence, chunk_size):
    return [sequence[i:i+chunk_size] for i in range(0, len(sequence), chunk_size)]


""" Returns the string representation of a given value
(12076, 4) -> '_POG'
assuming charset = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
"""
def string_representation(value, block_size):
    l = len(charset)
    extract_coefficient = lambda n: value % l**(n+1) // l**(n)
    powers = reversed(range(block_size))
    block_values = map(extract_coefficient, powers)
    return "".join(map(encode, block_values))


""" Transforms the input text into its numeric representation
('pog') -> (16 * 27 ** 2) + (15 * 27 ** 1) + (7 * 27 ** 0)
assuming charset = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
"""
def numeric_representation(text):
    index_and_character_pairs = enumerate(reversed(text))
    value_times_charset_size_to_index = lambda x: decode(x[1]) * len(charset) ** x[0]
    return sum(map(value_times_charset_size_to_index, index_and_character_pairs))


""" Encodes a list of numbers into string representation
with a given block size
([52, 687, 352, 15], 2) -> "AYYLMA_O"
"""
def encode_blocks(values, block_size):
    return "".join(map(lambda x: string_representation(x, block_size), values))


""" Splits a string into blocks of a given size and
decodes the blocks to their numeric equivalents
('ayylmao', 2) -> [52, 687, 352, 15]
"""
def decode_blocks(text, block_size):
    chunks = split_into_chunks(text, block_size)
    return list(map(numeric_representation, chunks))

