import json

import mock
import numpy
import networkx


if networkx.__version__ >= '2.0':
    raise RuntimeError("This code requires networkx less than 2.0")
print("Success!")
