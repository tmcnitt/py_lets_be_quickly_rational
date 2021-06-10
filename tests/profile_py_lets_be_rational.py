from __future__ import division

try:
    import py_lets_be_rational
except:
    print('This file is used to compare py_lets_be_quickly_rational with py_lets_be_rational. The code can not find py_lets_be_rational installed, and will exit.')
    exit(-1)

from timeit import timeit


from math import log, sqrt
import random
import time

TestCases = 10000

_F = [random.randint(10, 2000) for _ in range(TestCases)]
_K = [random.randint(10, 2000) for _ in range(TestCases)]
_sigma = [random.uniform(0, 1) for _ in range(TestCases)]
_T = [round(random.uniform(0.2, 1), 2) for _ in range(TestCases)]
_N = [random.randint(0, 3) for _ in range(TestCases)]
_z = [random.uniform(0, 1) for _ in range(TestCases)]
_x = [random.uniform(0, 1) for _ in range(TestCases)]


def run_black():
    q = 1  # CALL = 1 PUT = -1
    for i in range(TestCases):
        F = _F[i]
        K = _K[i]
        sigma = _sigma[i]
        T = _T[i]
        actual = py_lets_be_rational.black(F, K, sigma, T, q)
    #        print(F, K, sigma, T, " CALL = ", actual)
    q = -1  # CALL = 1 PUT = -1
    for i in range(TestCases):
        F = _F[i]
        K = _K[i]
        sigma = _sigma[i]
        T = _T[i]
        actual = py_lets_be_rational.black(F, K, sigma, T, q)


#        print(F, K, sigma, T, " PUT = ", actual)


def run_implied_volatility_from_a_transformed_rational_guess():
    binary_flag = [-1, 1]
    _q = [
        binary_flag[random.randint(0, 1)] for _ in range(TestCases)
    ]  # CALL = 1 PUT = -1
    _price = [random.randint(200, 1000) for _ in range(TestCases)]
    for i in range(TestCases):
        F = _F[i]
        K = _K[i]
        sigma = _sigma[i]
        T = _T[i]
        q = _q[i]
        # price = lets_be_rational_version.black(F, K, sigma, T, q)
        price = _price[i]
        try:
            actual = py_lets_be_rational.implied_volatility_from_a_transformed_rational_guess(
                price, F, K, T, q
            )
        except:
            pass


#        print(F, K, sigma, T, " CALL implied_volatility_from_a_transformed_rational_guess = ", actual)


def run_implied_volatility_from_a_transformed_rational_guess_with_limited_iterations():
    price = 100.0
    q = 1  # CALL = 1 PUT = -1
    for i in range(TestCases):
        F = _F[i]
        K = _K[i]
        sigma = _sigma[i]
        T = _T[i]
        N = _N[i]
        # price = lets_be_rational_version.black(F, K, sigma, T, q)
        try:
            actual = py_lets_be_rational.implied_volatility_from_a_transformed_rational_guess_with_limited_iterations(
                price, F, K, T, q, N
            )
        except:
            pass

    #        print(F, K, sigma, T, N, " CALL test_implied_volatility_from_a_transformed_rational_guess_with_limited_iterations = ", actual)
    q = -1  # CALL = 1 PUT = -1
    for i in range(TestCases):
        F = _F[i]
        K = _K[i]
        sigma = _sigma[i]
        T = _T[i]
        N = _N[i]
        # price = lets_be_rational_version.black(F, K, sigma, T, q)

        try:
            actual = py_lets_be_rational.implied_volatility_from_a_transformed_rational_guess_with_limited_iterations(
                price, F, K, T, q, N
            )
        except:
            pass


#        print(F, K, sigma, T, N, " PUT test_implied_volatility_from_a_transformed_rational_guess_with_limited_iterations = ", actual)


def run_normalised_black():
    q = 1  # CALL = 1 PUT = -1
    for i in range(TestCases):
        F = _F[i]
        K = _K[i]
        sigma = _sigma[i]
        T = _T[i]

        x = log(F / K)
        s = sigma * sqrt(T)

        actual = py_lets_be_rational.normalised_black(x, s, q)
    #        print(F, K, sigma, T, " CALL normalised_black = ", actual)
    q = -1  # CALL = 1 PUT = -1
    for i in range(TestCases):
        F = _F[i]
        K = _K[i]
        sigma = _sigma[i]
        T = _T[i]

        x = log(F / K)
        s = sigma * sqrt(T)

        actual = py_lets_be_rational.normalised_black(x, s, q)


#        print(F, K, sigma, T, " PUT normalised_black = ", actual)


def run_normalised_black_call():
    for i in range(TestCases):
        F = _F[i]
        K = _K[i]
        sigma = _sigma[i]
        T = _T[i]

        x = log(F / K)
        s = sigma * sqrt(T)

        actual = py_lets_be_rational.normalised_black_call(x, s)


#        print(F, K, sigma, T, " normalised_black_call = ", actual)


def run_normalised_vega():
    for i in range(TestCases):
        F = _F[i]
        K = _K[i]
        sigma = _sigma[i]
        T = _T[i]

        x = log(F / K)
        s = sigma * sqrt(T)

        actual = py_lets_be_rational.lets_be_rational.normalised_vega(x, s)


#        print(F, K, sigma, T, " normalised_vega = ", actual)


def run_normalised_implied_volatility_from_a_transformed_rational_guess():
    q = 1  # CALL = 1 PUT = -1
    for i in range(TestCases):
        F = _F[i]
        K = _K[i]
        sigma = _sigma[i]
        T = _T[i]

        x = _x[i]
        s = sigma * sqrt(T)
        beta = py_lets_be_rational.normalised_black(x, s, q)
        actual = py_lets_be_rational.normalised_implied_volatility_from_a_transformed_rational_guess(
            beta, x, q
        )
    #        print(F, K, sigma, T, " CALL normalised_implied_volatility_from_a_transformed_rational_guess = ", actual)
    q = -1  # CALL = 1 PUT = -1
    for i in range(TestCases):
        F = _F[i]
        K = _K[i]
        sigma = _sigma[i]
        T = _T[i]

        x = _x[i]
        s = sigma * sqrt(T)
        beta = py_lets_be_rational.normalised_black(x, s, q)
        actual = py_lets_be_rational.normalised_implied_volatility_from_a_transformed_rational_guess(
            beta, x, q
        )


#        print(F, K, sigma, T, " PUT normalised_implied_volatility_from_a_transformed_rational_guess = ", actual)


def run_normalised_implied_volatility_from_a_transformed_rational_guess_with_limited_iterations():
    q = 1  # CALL = 1 PUT = -1
    for i in range(TestCases):
        F = _F[i]
        K = _K[i]
        sigma = _sigma[i]
        T = _T[i]
        N = _N[i]

        x = _x[i]
        s = sigma * sqrt(T)
        beta = py_lets_be_rational.normalised_black(x, s, q)
        actual = py_lets_be_rational.normalised_implied_volatility_from_a_transformed_rational_guess_with_limited_iterations(
            beta, x, q, N
        )
    #        print(F, K, sigma, T, " CALL normalised_implied_volatility_from_a_transformed_rational_guess_with_limited_iterations = ", actual)
    q = -1  # CALL = 1 PUT = -1
    for i in range(TestCases):
        F = _F[i]
        K = _K[i]
        sigma = _sigma[i]
        T = _T[i]
        N = _N[i]

        x = _x[i]
        s = sigma * sqrt(T)
        beta = py_lets_be_rational.normalised_black(x, s, q)
        actual = py_lets_be_rational.normalised_implied_volatility_from_a_transformed_rational_guess_with_limited_iterations(
            beta, x, q, N
        )


#        print(F, K, sigma, T, " PUT normalised_implied_volatility_from_a_transformed_rational_guess_with_limited_iterations = ", actual)


def run_norm_cdf():
    for i in range(TestCases):
        z = _z[i]
        actual = py_lets_be_rational.norm_cdf(z)


#        print(z, " norm_cdf = ", actual)


# TODO: make this dynamic
funcs = [
    "run_black()",
    "run_implied_volatility_from_a_transformed_rational_guess()",
    "run_implied_volatility_from_a_transformed_rational_guess_with_limited_iterations()",
    "run_normalised_black()",
    "run_normalised_black_call()",
    "run_normalised_vega()",
    "run_normalised_implied_volatility_from_a_transformed_rational_guess()",
    "run_normalised_implied_volatility_from_a_transformed_rational_guess_with_limited_iterations()",
    "run_norm_cdf()",
]
for func in funcs:
    # Call once to compile numba
    try:
        eval(func)
    except Exception as e:
        print("Exception in testcase {}, {} ".format(func, e))
    # Run the bench
    print("py_lets_be_rational:", func, timeit(func, globals=globals(), number=100))
