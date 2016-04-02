from setuptools import setup, find_packages
from tcp_handshake_rst import __version__


setup(
    name='tcp-handshake-rst',
    version=__version__,
    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'tcp-handshake-rst = tcp_handshake_rst.tcp_handshake_rst:main',
        ],
    },

    install_requires=[
        'scapy==2.3.2',
    ],

    license='Apache 2',
    description='TCP Handshake RST',
    url='https://github.com/2m/tcp-handshake-rst',
)
