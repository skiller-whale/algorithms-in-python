import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


UTILS_PATH = Path(__file__).parent


def plot_list_timing(times):
    """A helper function to plot the time of list operations.

    Args:
        times (list): A list of times (in seconds).
    """

    # ensure skillerwhale style is used
    plt.style.use(UTILS_PATH / 'skiller-whale.mplstyle')
    times = np.array(times)

    fig, ax = plt.subplots(1, 1, figsize=(5, 4))

    ax.scatter(range(len(times)), times, s=10)
    ax.vlines(
        range(len(times)),
        ymin=np.zeros_like(times),
        ymax=times
    )
    ax.xaxis.grid(True, which='minor')
    ax.yaxis.grid(True, which='minor')
    ax.set_ylabel('Time (s.)')
    ax.set_xlabel('Length of list')

    # Prevent scientific notation
    ax.ticklabel_format(style='plain')

    plt.tight_layout()
    plt.show()

def plot_cubic_polyfit(Ns, times, ax=None, label=''):
    """Plots a list of times and a cubic approximation.

    Args:
        Ns (list): A list of input sizes.
        times (list): A list of times (in seconds).
    """
    if ax is None:
        fig, ax = plt.subplots()
    plt.scatter(Ns, times, label=label)

    coefs = np.polyfit(Ns, times, deg=3)
    Ns = np.array(Ns)

    plt.plot(
        Ns,
        coefs[0] * Ns ** 3 + coefs[1] * Ns ** 2 +
        coefs[2] * Ns + coefs[3]
    )

    plt.ylabel('Time (s.)')
    plt.xlabel('Input size (N)')

    # Prevent scientific notation
    ax.ticklabel_format(style='plain')
    plt.legend()
    return ax
