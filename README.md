[Tox](https://tox.readthedocs.org/en/latest/) is used to manage virtual python environments.

To send 3-way tcp handshake ending with RST with source port of 12500 and destination IP 192.168.1.100 run

    tox sudo tcp-handshake-rst 192.168.1.100 12500

To start python interpreter with all dependant modules loaded to python path run:

    tox python
