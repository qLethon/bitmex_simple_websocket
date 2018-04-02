from setuptools import setup


requires = ["requests>=2.14.2"]


setup(
    name='bitmex_simple_ws',
    version='0.1',
    description='BitMEX simple websocket client',
    url='https://github.com/whatever/whatever',
    author='qLethon',
    author_email='qLethon@gmail.com',
    license='MIT',
    packages=[
        "bitmex_ws",
    ],
    install_requires=[
        'websocket-client==0.46.0',
    ],
)