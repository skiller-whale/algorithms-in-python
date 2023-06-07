from utils.plotting import plot_cubic_polyfit
import numpy as np
import time
import matplotlib.pyplot as plt


def time_plot_count_occurrences(count_occurrences, count_occurrences_optimized):
    """Time and plot `count_occurrences` and `count_occurrences_optimized`
        on input of different size.
    """
    rng = np.random.default_rng(seed=42)
    Ns = range(0, 1_500, 75)
    times, times_optimized = [], []

    for n in Ns:
        random_list = list(rng.integers(-n, n, n))
        numbers_to_count = list(set(rng.integers(-n // 2, n // 2, n // 2)))

        start_time = time.perf_counter()
        occurrences = count_occurrences(random_list, numbers_to_count)
        times.append(time.perf_counter() - start_time)

        start_time_fast = time.perf_counter()
        occurrences_optimized = count_occurrences_optimized(random_list, numbers_to_count)

        if occurrences_optimized is not None:
            times_optimized.append(time.perf_counter() - start_time_fast)
            assert occurrences == occurrences_optimized, (
                'count_occurrences and count_occurrences_optimized return '
                'different results!'
            )

    ax = plot_cubic_polyfit(Ns, times, label='count_occurrences')
    if times_optimized:
        plot_cubic_polyfit(Ns, times_optimized, ax, label='count_occurrences_optimized')

    plt.show()
