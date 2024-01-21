from pyseq import Sequence
import json
from datetime import datetime
import py_framels
import matplotlib.pyplot as plt

x = [100, 1000, 10000, 50000, 100000]
y1 = list()
y2 = list()
for i in x:
    data_set: list[str] = list()
    for i in range(0, i):
        data_set.append(f"beauty_left.{str(i).zfill(6)}.exr")

    now = datetime.now()
    py_framels.py_basic_listing(data_set)
    y1.append((datetime.now() - now).total_seconds())

    now = datetime.now()
    s = Sequence(data_set)
    y2.append((datetime.now() - now).total_seconds())
plt.plot(x, y1, label="py_framels")
plt.plot(x, y2, label="pyseq")
plt.xlabel("Number of string")
plt.ylabel("Time in seconds")
plt.title("Benchmark between pyseq and py_framels")
plt.savefig("./benchmark/bench.png")
