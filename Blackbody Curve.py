import numpy as np
import matplotlib.pyplot as plt

h = 6.62607015*10e-34  # Planck's constant (2019), (J*s).
c = 299792458  # Speed of light (m/s).
k = 1.380649*10e-23  # Boltzmann constant (J/K).
b = 2.897772917e-3  # Wien's displacement constant (K*m).

size = 2000  # Array size.

w = np.arange(size)  # Wavelength array (nm).
sr = np.zeros(size)  # Spectral radiance array.
csr = np.zeros(size)  # Classical spectral radiance array.

T = 6001  # Temperature limit (K).
i = 3000  # Iterator.

np.seterr(all='ignore')  # Ignoring the RuntimeWarning.


def pl(x, y):  # Planck's law.
    return (2*h*c**2)/(x**5) * 1/(np.e**((h*c)/(x*k*y))-1)


def rjl(x, y):  # Rayleigh-Jeans law.
    return (2*c*k*y)/x**4


def wdl(x):  # Wien's displacement law.
    return b/x


fig = plt.figure('Blackbody Curve')
while i < T:
    j = 0
    while j < len(w):
        sr[j] = pl(np.float64(j*1e-9), i)
        csr[j] = rjl(np.float64(j), i)
        j += 1
    plt.plot(w, sr)
    i += 1000

# plt.plot(w, csr)
# plt.axis((0, 2000, 0, 3.3e-13))
plt.grid()
plt.xlabel('Wavelength (nm)')
plt.ylabel("Spectral Radiance")
plt.show()




