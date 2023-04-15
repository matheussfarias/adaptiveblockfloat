from goldeneye.src.num_sys_class import *
from goldeneye.src.num_sys_class import _number_sys, _ieee754
import torch
import math

# Adaptive Float
def test_adaptive():
    # test tensors to use on different systems
    test1 = torch.tensor([[-1.17,  2.71, -1.60,  0.43],
                          [-1.14,  2.05,  1.01,  0.07],
                          [ 0.16, -0.03, -0.89, -0.87],
                          [-0.04, -0.39,  0.64, -2.89]])

    test2 = torch.tensor([[ 997.481,  188.034, -147.376, -277.766],
                          [-617.844, -755.696,   18.283,  670.539],
                          [-709.682, -841.260,  300.587,  837.047],
                          [ 347.082,   98.871, -775.379,  709.284]])

    # bitwidth of 4, 1 sign bit, 2 exponent bits, 1 mantissa bit
    adaptive4 = adaptive_float(
        bit_width=4,
        exp_len=2,
        mant_len=1,
        exp_bias=None
    )

    # # expected tensors for tests
    # expected1 = torch.tensor([[-1.0,  3.0, -1.5,  0.0],
    #                           [-1.0,  2.0,  1.0,  0.0],
    #                           [ 0.0, -0.0, -0.0, -0.0],
    #                           [-0.0, -0.0,  0.0, -3.0]])

    # assert(torch.equal(adaptive4.real_to_format_tensor(test1), expected1))

    expected2 = torch.tensor([[ 768.0,    0.0,   -0.0, -256.0],
                              [-512.0, -768.0,    0.0,  768.0],
                              [-768.0, -768.0,  256.0,  768.0],
                              [ 384.0,    0.0, -768.0,  768.0]])

    assert(torch.equal(adaptive4.real_to_format_tensor(test2), expected2))

#     # bitwidth of 6, 1 sign bit, 2 exponent bits, 3 mantissa bits
#     adaptive6 = adaptive_float(
#         bit_width=6,
#         exp_len=2,
#         mant_len=3,
#         exp_bias=None
#     )

#     # expected tensors for tests
#     expected1 = torch.tensor([[-1.125, 2.750, -1.625,  0.0],
#                               [-1.125,   2.0,    1.0,  0.0],
#                               [   0.0,  -0.0,   -0.0, -0.0],
#                               [  -0.0,  -0.0,    0.0, -3.0]])

#     assert(torch.equal(adaptive6.real_to_format_tensor(test1), expected1))

#     expected2 = torch.tensor([[ 960.0,    0.0,   -0.0, -288.0],
#                               [-640.0, -768.0,    0.0,  640.0],
#                               [-704.0, -832.0,  288.0,  832.0],
#                               [ 352.0,    0.0, -768.0,  704.0]])

#     assert(torch.equal(adaptive6.real_to_format_tensor(test2), expected2))

#     # bitwidth of 11, 1 sign bit, 4 exponent bits, 6 mantissa bits
#     adaptive11 = adaptive_float(
#         bit_width=11,
#         exp_len=4,
#         mant_len=6,
#         exp_bias=None
#     )

#     # expected tensors for tests
#     expected1 = \
#         torch.tensor([[    -1.171875,         2.71875,  -1.59375,  0.4296875],
#                       [    -1.140625,          2.0625,  1.015625,  0.0703125],
#                       [   0.16015625, -0.030029296875, -0.890625, -0.8671875],
#                       [-0.0400390625,       -0.390625,  0.640625,     -2.875]])

#     assert(torch.equal(adaptive11.real_to_format_tensor(test1), expected1))

#     expected2 = torch.tensor([[1000.0,  188.0, -148.0, -276.0],
#                               [-616.0, -752.0,  18.25,  672.0],
#                               [-712.0, -840.0,  300.0,  840.0],
#                               [ 348.0,   99.0, -776.0,  712.0]])

#     assert(torch.equal(adaptive11.real_to_format_tensor(test2), expected2))

#     # bitwidth of 11, 1 sign bit, 2 exponent bits, 8 mantissa bits
#     adaptive11 = adaptive_float(
#         bit_width=11,
#         exp_len=2,
#         mant_len=8,
#         exp_bias=None
#     )

#     # expected tensors for tests
#     expected1 = torch.tensor([[-1.171875, 2.7109375, -1.6015625,       0.0],
#                               [-1.140625,  2.046875, 1.01171875,       0.0],
#                               [      0.0,      -0.0,       -0.0,      -0.0],
#                               [     -0.0,      -0.0,        0.0, -2.890625]])

#     assert(torch.equal(adaptive11.real_to_format_tensor(test1), expected1))

#     expected2 = torch.tensor([[ 998.0,    0.0,   -0.0, -278.0],
#                               [-618.0, -756.0,    0.0,  670.0],
#                               [-710.0, -842.0,  301.0,  838.0],
#                               [ 347.0,    0.0, -776.0,  710.0]])

#     assert(torch.equal(adaptive11.real_to_format_tensor(test2), expected2))

def test_block_adaptive():
    # test tensors to use on different systems
    test1 = torch.tensor([[-1.17,  2.71, -1.60,  0.43],
                          [-1.14,  2.05,  1.01,  0.07],
                          [ 0.16, -0.03, -0.89, -0.87],
                          [-0.04, -0.39,  0.64, -2.89]])

    test2 = torch.tensor([[ 997.481,  188.034, -147.376, -277.766],
                          [-617.844, -755.696,   18.283,  670.539],
                          [-709.682, -841.260,  300.587,  837.047],
                          [ 347.082,   98.871, -775.379,  709.284]])
    
    bladapt4 = block_adapt_fp(
        bit_width=4,
        exp_len=2,
        mant_len=1,
        exp_bias=None
    )

    result_b_adapt = bladapt4.real_to_format_tensor(test2)
    print(result_b_adapt)