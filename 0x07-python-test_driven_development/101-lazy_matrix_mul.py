#!/usr/bin/python3
""" Matrix multiplication
    with numpy module
"""


import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """ Multiplication of
        two conformables matrices
    """

    return np.dot(m_a, m_b)
