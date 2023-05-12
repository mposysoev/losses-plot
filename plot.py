import sys
import os
import matplotlib.pyplot as plt


def read_file(file_path):
    with open(file_path, "r") as file:
        values = []
        lines = file.readlines()

        for line in lines:
            value = float(line.split()[-1])
            values.append(value)

    return values


def main():
    print("Start")
    file_paths = os.listdir()
    x = list(range(1, 26))
    for path in file_paths:
        if ".loss" in path:
            data = read_file(path)
            plt.scatter(x, data, label=f"{path}")

    plt.legend()
    plt.savefig("losses.pdf")
    # plt.show()


if __name__ == "__main__":
    # file_paths = os.listdir()
    # print(file_paths)
    main()
