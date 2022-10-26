# Overview
py_lets_be_quickly_rational is an updated version of py_lets_be_rational. It currently speeds up calculations as much as <b>80%</b> while still passing the test suite. This repo also exists as a place of continued development since py_lets_be_rational seems to not be actively maintained.


The below table provides some comparisons in the various libraries
| Feature                                     | `py_lets_be_quickly_rational` | `py_lets_be_rational` | `lets_be_rational`         |
| ------------------------------------------- |:---------------------:|:---------------------:|:--------------------------:|
| Python Version Compatibility                | 2.7 and 3.x           | 2.7 and 3.x           |           2.7 only         |
| Source Language                             | Python + All Numba    | Python + Some Numba   | C with Python SWIG Wrapper |
| Optional Dependencies                       | Numba                 | Numba                  |          None             |

## Execution Speed
`py_lets_be_quickly_rational` uses numba to speedup calculations on every function. `py_lets_be_rational` also does this, but on a smaller scale. Therefore, `py_lets_be_quickly_rational` is several times faster at calculating implied volatility than `py_lets_be_rational` or `lets_be_rational`. The below results were done on my macbook pro, and the script can be found in tests. The script calls each function with a thousand fake values, and averages the time over 100 runs.

| Feature                                     | `py_lets_be_rational` | `py_lets_be_quickly_rational` | Improvement 
| ------------------------------------------- |:---------------------:|:---------------------:|:---------------------:|
| Normalised IV Transformed Rational Guess                              | 16.2s    |  2.6s  | <b>~83%</b>
| Normalised IV Transformed Rational Guess Limited Iterations | 13.7s                   |  2.7s               | <b>~78%</b>


## Installation
  Can be installed with pip 
  ```
    pip3 install py-lets-be-quickly-rational
   ```
## Roadmap
Right now the code takes advantage of numba JIT compiling, but that can only get us so far. Several common stats functions are implemented in a custom way, orignially done in the C++ implementation since they were faster than the C++ versions. However, even optimized python code is slower than native code, and numpy provides several of those functions natively. This, combined with taking advantage of numpys vectorization support, could lead to performance impacts.  

## Numba Dependency
Numba is an optional dependency. Because Numba installation can be tricky and OS-dependent, 
we decided to leave it up to each user to decide how and whether to install Numba. If Numba is present, execution speed  will be faster. If not, the code will still run -- just much slower.




## Installing numba
`py_lets_be_quickly_rational` optionally depends on `numba` which in turn depends on `llvm-lite`. `llvm-lite` wants LLVM 3.9 
```
pip install numba
```

For other operating systems, please refer to the `llvm-lite` and `numba` documentation.

## Development

Fork our repository, and make the changes on your local copy:

```
git clone git@github.com/your_username/py_lets_be_quickly_rational
cd py_lets_be_quickly_rational
pip install -e .
pip install -r dev-requirements.txt
```

When you are done, push the changes, and create a pull request on your repo.


## About "Let's be Rational"

["Let's Be Rational"](http://www.jaeckel.org/LetsBeRational.pdf) is a paper by [Peter Jäckel](http://jaeckel.org) showing *"how Black's volatility can be implied from option prices with as little as two iterations to maximum attainable precision on standard (64 bit floating point) hardware for all possible inputs."*

The paper is accompanied by the full C source code, which resides at [www.jaeckel.org/LetsBeRational.7z](www.jaeckel.org/LetsBeRational.7z).

```
    Copyright © 2013-2014 Peter Jäckel.

    Permission to use, copy, modify, and distribute this software is freely granted,
    provided that this notice is preserved.

    WARRANTY DISCLAIMER
    The Software is provided "as is" without warranty of any kind, either express or implied,
    including without limitation any implied warranties of condition, uninterrupted use,
    merchantability, fitness for a particular purpose, or non-infringement.
```


## License
MIT 
