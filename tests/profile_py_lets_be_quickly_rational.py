from __future__ import division
import py_lets_be_quickly_rational
from timeit import timeit

import numpy as np
from math import log, sqrt
import random

import time

NumTestCases = 10000

_F = [random.randint(10, 2000) for _ in range(NumTestCases)]
_K = [random.randint(10, 2000) for _ in range(NumTestCases)]
_sigma = [random.uniform(0, 1) for _ in range(NumTestCases)]
_T = [round(random.uniform(0.2, 1), 2) for _ in range(NumTestCases)]
_N = [random.randint(0, 3) for _ in range(NumTestCases)]
_z = [random.uniform(0, 1) for _ in range(NumTestCases)]
_x = [random.uniform(0, 1) for _ in range(NumTestCases)]

def run_black():
    q = 1  # CALL = 1 PUT = -1
    for i in range(NumTestCases):
        F = _F[i]
        K = _K[i]
        sigma = _sigma[i]
        T = _T[i]

        py_lets_be_quickly_rational.black(F, K, sigma, T, q)

    q = -1  # CALL = 1 PUT = -1
    for i in range(NumTestCases):
        F = _F[i]
        K = _K[i]
        sigma = _sigma[i]
        T = _T[i]
        py_lets_be_quickly_rational.black(F, K, sigma, T, q)


def run_implied_volatility_from_a_transformed_rational_guess():
    binary_flag = [-1, 1]
    _q = [
        binary_flag[random.randint(0, 1)] for _ in range(NumTestCases)
    ]  # CALL = 1 PUT = -1
    _price = [random.randint(200, 1000) for _ in range(NumTestCases)]
    for i in range(NumTestCases):
        F = _F[i]
        K = _K[i]
        T = _T[i]
        q = _q[i]
        price = _price[i]
        try:
            py_lets_be_quickly_rational.implied_volatility_from_a_transformed_rational_guess(
                price, F, K, T, q
            )
        except:
            pass

def run_implied_volatility_from_a_transformed_rational_guess_with_limited_iterations():
    price = 100.0
    q = 1  # CALL = 1 PUT = -1
    for i in range(NumTestCases):
        F = _F[i]
        K = _K[i]
        sigma = _sigma[i]
        T = _T[i]
        N = _N[i]
        try:
            py_lets_be_quickly_rational.implied_volatility_from_a_transformed_rational_guess_with_limited_iterations(
                price, F, K, T, q, N
            )
        except:
            pass

    q = -1  # CALL = 1 PUT = -1
    for i in range(NumTestCases):
        F = _F[i]
        K = _K[i]
        sigma = _sigma[i]
        T = _T[i]
        N = _N[i]

        try:
            py_lets_be_quickly_rational.implied_volatility_from_a_transformed_rational_guess_with_limited_iterations(
                price, F, K, T, q, N
            )
        except:
            pass

def run_normalised_black():
    q = 1  # CALL = 1 PUT = -1
    for i in range(NumTestCases):
        F = _F[i]
        K = _K[i]
        sigma = _sigma[i]
        T = _T[i]

        x = log(F / K)
        s = sigma * sqrt(T)

        py_lets_be_quickly_rational.normalised_black(x, s, q)

    q = -1  # CALL = 1 PUT = -1
    for i in range(NumTestCases):
        F = _F[i]
        K = _K[i]
        sigma = _sigma[i]
        T = _T[i]

        x = log(F / K)
        s = sigma * sqrt(T)

        py_lets_be_quickly_rational.normalised_black(x, s, q)


def run_normalised_black_call():
    for i in range(NumTestCases):
        F = _F[i]
        K = _K[i]
        sigma = _sigma[i]
        T = _T[i]

        x = log(F / K)
        s = sigma * sqrt(T)

        py_lets_be_quickly_rational.normalised_black_call(x, s)

def run_normalised_vega():
    for i in range(NumTestCases):
        F = _F[i]
        K = _K[i]
        sigma = _sigma[i]
        T = _T[i]

        x = log(F / K)
        s = sigma * sqrt(T)

        py_lets_be_quickly_rational.lets_be_rational.normalised_vega(x, s)


def run_normalised_implied_volatility_from_a_transformed_rational_guess():
    q = 1  # CALL = 1 PUT = -1
    for i in range(NumTestCases):
        F = _F[i]
        K = _K[i]
        sigma = _sigma[i]
        T = _T[i]

        x = _x[i]
        s = sigma * sqrt(T)
        beta = py_lets_be_quickly_rational.normalised_black(x, s, q)
        py_lets_be_quickly_rational.normalised_implied_volatility_from_a_transformed_rational_guess(
            beta, x, q
        )
    #        print(F, K, sigma, T, " CALL normalised_implied_volatility_from_a_transformed_rational_guess = ", actual)
    q = -1  # CALL = 1 PUT = -1
    for i in range(NumTestCases):
        F = _F[i]
        K = _K[i]
        sigma = _sigma[i]
        T = _T[i]

        x = _x[i]
        s = sigma * sqrt(T)
        beta = py_lets_be_quickly_rational.normalised_black(x, s, q)
        py_lets_be_quickly_rational.normalised_implied_volatility_from_a_transformed_rational_guess(
            beta, x, q
        )


def run_normalised_implied_volatility_from_a_transformed_rational_guess_with_limited_iterations():
    q = 1  # CALL = 1 PUT = -1
    for i in range(NumTestCases):
        F = _F[i]
        K = _K[i]
        sigma = _sigma[i]
        T = _T[i]
        N = _N[i]

        x = _x[i]
        s = sigma * sqrt(T)
        beta = py_lets_be_quickly_rational.normalised_black(x, s, q)
        py_lets_be_quickly_rational.normalised_implied_volatility_from_a_transformed_rational_guess_with_limited_iterations(
            beta, x, q, N
        )

    q = -1  # CALL = 1 PUT = -1
    for i in range(NumTestCases):
        F = _F[i]
        K = _K[i]
        sigma = _sigma[i]
        T = _T[i]
        N = _N[i]

        x = _x[i]
        s = sigma * sqrt(T)
        beta = py_lets_be_quickly_rational.normalised_black(x, s, q)
        py_lets_be_quickly_rational.normalised_implied_volatility_from_a_transformed_rational_guess_with_limited_iterations(
            beta, x, q, N
        )


def benchmark_custom_cdf():
    for i in range(NumTestCases):
        z = _z[i]
        py_lets_be_quickly_rational.norm_cdf(z)

def benchmark_custom_erfcx():
    for val in erfxTestValues:
        py_lets_be_quickly_rational.erf_cody.erfcx_cody(val)


funcs = [
    # "run_black()",
    # "run_implied_volatility_from_a_transformed_rational_guess()",
    # "run_implied_volatility_from_a_transformed_rational_guess_with_limited_iterations()",
    # "run_normalised_black()",
    # "run_normalised_black_call()",
    # "run_normalised_vega()",
    # "run_normalised_implied_volatility_from_a_transformed_rational_guess()",
    # "run_normalised_implied_volatility_from_a_transformed_rational_guess_with_limited_iterations()",
    "benchmark_custom_cdf()",
    "benchmark_custom_erfcx()"
]

# Optional scipy benchmarks
try:
    import scipy
    @py_lets_be_quickly_rational.numba_helper.maybe_jit(nogil=False)
    def special_cdf(x):
        return scipy.special.ndtr(x)

    def benchmark_scipy_cdf():
        for i in range(NumTestCases):
            z = _z[i]
            special_cdf(z)

    @py_lets_be_quickly_rational.numba_helper.maybe_jit(nogil=False)
    def special_erfcx(x):
        return scipy.special.erfcx(x)

    erfxTestValues = np.linspace(-3, 3)
    def benchmark_scipy_erfcx():
        for val in erfxTestValues:
            special_erfcx(val)

    funcs += [
        "benchmark_scipy_cdf()",
        "benchmark_scipy_erfcx()",
    ]
except:
    pass

if __name__ == "__main__":
    # TODO: make this dynamic

    for func in funcs:
        # Call once to compile numba
        try:
            eval(func)
        except Exception as e:
            print("Exception in testcase {}, {} ".format(func, e))
        # Run the bench
        print("py_lets_be_quickly_rational:", func, timeit(func, globals=globals(), number=100))
