import numpy as np
import matplotlib.pyplot as plt

def time_shift(signal, n, k):
    shifted_n = n + k
    plt.stem(shifted_n, signal)
    plt.title(f"Time-Shifted Signal (k={k})")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return shifted_n, signal

def time_scale(signal, n, k):
    scaled_n = n * k
    plt.stem(scaled_n, signal)
    plt.title(f"Time-Scaled Signal (k={k})")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return scaled_n, signal

def signal_addition(signal1, signal2, n):
    result = signal1 + signal2
    plt.stem(n, result)
    plt.title("Signal Addition")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return result

def signal_multiplication(signal1, signal2, n):
    result = signal1 * signal2
    plt.stem(n, result)
    plt.title("Signal Multiplication")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return result


n = np.arange(-5, 6)
x1 = np.where(n >= 0, 1, 0) 
x2 = np.where(n == 0, 1, 0)  

time_shift(x1, n, 2)
time_scale(x1, n, 2)
signal_addition(x1, x2, n)
signal_multiplication(x1,x2,n)