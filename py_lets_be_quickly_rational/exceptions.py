# -*- coding: utf-8 -*-

from py_lets_be_quickly_rational import constants


class VolatilityValueException(Exception):
    def __init__(self):
        Exception.__init__(self, "Volatility value out of range.")
        self.value = None

    def __init__(self, message, value):
        Exception.__init__(self, message)
        self.value = value


class BelowIntrinsicException(VolatilityValueException):
    def __init__(self):
        VolatilityValueException.__init__(self, "The volatility is below the intrinsic value.",
                                                       constants.VOLATILITY_VALUE_TO_SIGNAL_PRICE_IS_BELOW_INTRINSIC)


class AboveMaximumException(VolatilityValueException):
    def __init__(self):
        VolatilityValueException.__init__(self, "The volatility is above the maximum value.",
                                                       constants.VOLATILITY_VALUE_TO_SIGNAL_PRICE_IS_ABOVE_MAXIMUM)


if __name__ == "__main__":
    try:
        raise BelowIntrinsicException
    except VolatilityValueException as e:
        if not isinstance(e, BelowIntrinsicException):
            raise Exception("Should be BelowIntrinsicException")

    try:
        raise AboveMaximumException
    except VolatilityValueException as e:
        if not isinstance(e, AboveMaximumException):
            raise Exception("Should be AboveMaximumException")
