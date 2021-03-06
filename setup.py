from setuptools import setup


requires = ["requests>=2.14.2"]


setup(
    name='bitmex_simple_websocket',
    version='0.1.1',
    description='BitMEX simple websocket client',
    url='https://github.com/qLethon/bitmex_simple_websocket',
    author='qLethon',
    author_email='qLethon@gmail.com',
    license='MIT',
    py_modules=['bitmex_simple_websocket'],
    install_requires=[
        'websocket-client==0.46.0',
    ],
)