"""
hash functions are designed to be one-way functions,
meaning that they are not meant to be reversed or decoded.
The purpose of a hash function is to take input data and produce
a fixed-size "digest" or "hash value" that is unique to that specific input.
It is computationally infeasible to reverse the process and obtain the
original input from the hash value.
"""
import hashlib


def generate_card_hash(
    number,
    expire_date,
    provider_type,
):
    """
    generate a new card hash.
    """
    data = str(number + expire_date + provider_type)

    sha256_hash = hashlib.sha256()

    sha256_hash.update(data.encode('utf-8'))

    static_hash = sha256_hash.hexdigest()

    return static_hash


generate_card_hash(
    number=8600120438395413,
    expire_date=1226,
    provider_type=1
)
