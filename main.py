import numpy as np
from unitary_signals import unit_step, unit_impulse, ramp_signal
from trigonometric_signals import sine_wave, cosine_wave
from operations import time_shift, signal_addition, signal_multiplication

step = unit_step(np.arange(0, 20))
impulse = unit_impulse(np.arange(0, 20))

t = np.linspace(0, 1, 500)
sine = sine_wave(2, 5, 0, t)

time_shift(sine, t, 5)

ramp = ramp_signal(np.arange(0, 20))
signal_addition(step, ramp, np.arange(0, 20))

cosine = cosine_wave(2, 5, 0, t)
signal_multiplication(sine,cosine,t)