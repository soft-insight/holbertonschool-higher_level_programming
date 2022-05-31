#!/usr/bin/python3
""" Matrix multiplication 
    with numpy module
"""


def lazy_matrix_mul(m_a, m_b):
    """ Multiplication of 
        two conformables matrices
    """
    
    import numpy as np
    
    return np.matmul(m_a, m_b)
