from pyseq import Sequence
import json
from datetime import datetime
import py_framels
import matplotlib.pyplot as plt


def benchmark_pyseq(x: list[int]):
    name = f"bench_{str(x[-1])}"
    y1 = list()
    y2 = list()
    for i in x:
        data_set: list[str] = list()
        for aov in ["Beauty", "Specular", "IndirectDiffuse", "SSS"]:
            for i in range(0, i):
                data_set.append(f"{aov}_left.{str(i).zfill(6)}.exr")
        now = datetime.now()
        py_framels.py_basic_listing(data_set, False)
        y1.append((datetime.now() - now).total_seconds())

        now = datetime.now()
        s = Sequence(data_set)
        y2.append((datetime.now() - now).total_seconds())
    print("py_framels", y1)
    print("pyseq", y2)
    plt.plot(x, y1, label="py_framels")
    plt.plot(x, y2, label="pyseq")
    plt.xlabel("Number of string")
    plt.ylabel("Time in seconds")
    plt.title(f"Benchmark {name} between pyseq and py_framels")
    plt.savefig(f"./benchmark/{name}.png")
    plt.show()
    plt.close()


if __name__ == "__main__":
    x = [1, 2, 5, 10, 50, 100]
    benchmark_pyseq(x)
    x = [100, 1000, 20000, 25000]
    benchmark_pyseq(x)
