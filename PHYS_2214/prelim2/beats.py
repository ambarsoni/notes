from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

def main():
    A = 1

    T1 = 2.0 
    T2 = 2.3
    
    w1 = 2 * np.pi / T1
    w2 = 2 * np.pi / T2
    
    wbeat = w1 - w2
    Tbeat = 2 * np.pi / wbeat
    
    start = 0
    stop  = 2.5 * Tbeat
    step  = (stop - start) / 1000
    t = np.arange(start, stop, step)

    y1 = A * np.cos(-w1 * t) 
    y2 = A * np.cos(-w2 * t) 
    y  = y1 + y2

    envelope = 2 * A * np.cos(wbeat / 2 * t)

    plt.figure()
    plt.plot(t, envelope, linewidth=3, label="envelope")
    plt.plot(t, y, label="beat")
    plt.xlabel("time")
    plt.ylabel("amplitude")
    plt.legend()
    plt.savefig("beats.pgf")

    plt.figure()
    plt.plot(t, envelope, linewidth=3, label="envelope")
    plt.plot(t, y1, label="$y_1$")
    plt.plot(t, y2, label="$y_2$")
    plt.xlabel("time")
    plt.ylabel("amplitude")
    plt.legend()
    plt.savefig("beats-interference.pgf")

main()
