"""Wrapper around the Linux /dev/random stream.

Option to fallback to os.urandom.

In general, either fllows the Python standard library ```random``` or
``os.urandom`` interface.
"""

import os
import math

LOG_OF_2_TIMES_8 = math.log(2)*8

def random(n, allow_pseudo=False, path=None):
    """Return a string of `n` random bytes suitable for cryptographic use.

    Block if there is not enough entropy. If `allow_pseudo` is True, fallback to
    ``os.urandom``, otherwise raise NotImplementedError.
    """

    path = path or '/dev/random'
    try:
        f = open(path, 'r', buffering=0)
    except IOError:
        if allow_pseudo:
            return urandom(n)
        else:
            raise NotImplementedError
    return f.read(n)

def urandom(n):
    """Return `n` bytes from ``os.urandom``."""
    return os.urandom(n)

def randint(a, b, allow_pseudo=False, use_pseudo=False, path=None):
    """Return a random integer N such that a <= N <= b.
    """

    assert(a <= b)
    span = b - a + 1
    if span == 1:
        return a
    num_bytes = int(math.ceil(math.log(span)/LOG_OF_2_TIMES_8))
    if not use_pseudo:
        rand_str = random(num_bytes, allow_pseudo=allow_pseudo, path=path)
    else:
        rand_str = urandom(num_bytes)
    rand_int = 0
    for c in rand_str:
        rand_int <<= 8
        rand_int += ord(c)

    rand_int = rand_int % span
    return a + rand_int

def choice(seq):
    """Return a random element from the non-empty sequence seq. If seq is
    empty, raises IndexError."""

    if len(seq) == 0:
        raise IndexError
    return seq[randint(0, len(seq)-1)]
