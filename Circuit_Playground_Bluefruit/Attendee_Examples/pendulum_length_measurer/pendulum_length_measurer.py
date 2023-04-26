import time
from adafruit_circuitplayground import cp

# Utilities used to compute frequency components
from ulab.numpy.fft import fft
from ulab.numpy import zeros, argmax, pi


def compute_magnitude(vector):
    """Use pythagoras to compute the magnitude of a vector."""
    return sum(xi ** 2 for xi in vector) ** 0.5


# Setup parameters
sampling_period = 0.1
sampling_freq = 1 / sampling_period

num_data_points = 128
data = zeros(num_data_points)

total_time = sampling_period * num_data_points

print("""
This application computes the swinging frequency and length of a pendulum, \
with the hanging at the end. To do this, we first gather acceleration \
magnitude data. Then, we use the FFT to compute the frequency components \
of this signal. This allows us to compute the swinging frequency of the \
pendulum.

Finally, since the swinging frequency of a pendulum is dependent only on the \
distance to the center of mass and the strength of gravity, we can also compute \
the length of the pendulum.

To test the length measurements, you can hang the Bluefruit after the micro USB \
cable and swing it. This should give approximately the correct length. It will \
likely be a few cm shorter than the full length of the pendulum since it is the \
distance to the center of mass that matters.
""")
print(("frequency [Hz]", "length [cm]"))
while True:
    # Gather acceleration measurements
    for i in range(num_data_points):
        t0 = time.time()
        data[i] = compute_magnitude(cp.acceleration)

        # Sleep sufficiently
        elapsed_time = time.time() - t0
        if elapsed_time > sampling_period:
            print(
                "WARNING: Sampling is slower than expected, the accuracy might be affected by this."
            )
            print(f"Expected: {sampling_period}, actual: {elapsed_time}, iteration: {i}")
        time_to_sleep = max(0, sampling_period - elapsed_time)
        time.sleep(time_to_sleep)

    # Use FFT to compute frequency components of the acceleration signal
    real, imag = fft(data)
    # Use Pythagoras to compute the frequency magnitude
    magnitude = (real ** 2 + imag ** 2) ** 0.5

    # Since we are only interested in the magnitude, we can ommit the second half
    # of the FFT, which contains phase information.
    magnitude = magnitude[1: len(magnitude) // 2]

    # Find the most prevalent frequency in the signal
    freq = (1 + argmax(magnitude)) / total_time  # Hz
    freq /= 2  # Since we are using the absolute value, the frequency is doubled

    # Use the formula for the fundamental frequency as a function of length
    # "in reverse" to compute the length of the pendulum
    if freq > 0:
        T = 1 / freq  # s
    else:
        T = float("inf")  # s
    g = 1000  # cm / s^2
    length = g * (T / (2 * pi)) ** 2  # cm

    # Write the output
    print((freq, length))
