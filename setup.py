from distutils.core import setup


setup(
    name='py_lets_be_quickly_rational',
    version='1.0.0',
    packages=['py_lets_be_quickly_rational'],
    url="https://github.com/tmcnitt/py_lets_be_quickly_rational",
    license='MIT',
    maintainer='Troy McNitt',
    maintainer_email='troy.mcnitt@gmail.com',
    description='Pure python implementation of Peter Jaeckel\'s LetsBeRational.',
    install_requires=[
        'numpy'
    ]
)
