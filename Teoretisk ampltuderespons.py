import numpy as np
import matplotlib.pyplot as plt


R = 1000      
L = 10e-3     
C = 100e-9     

frequencies = np.logspace(1, 6, 1000)  
omega = 2 * np.pi * frequencies

LCserie = 1 - (omega**2) * L * C
LCRserie = np.sqrt((1 - (omega**2) * L * C)**2 + (omega * C * R)**2)
amplituderespons = np.abs(LCserie / LCRserie)

plt.figure(figsize=(8, 5))
plt.semilogx(frequencies, 20 * np.log10(amplituderespons), color='orange', label='Amplituderespons')
plt.title("Teoretisk Amplituderespons for Båndstoppfilter")
plt.xlabel("Frekvens (Hz)")
plt.ylabel("Amplitude (dB)")
plt.grid(True, which="both", ls="--")
plt.legend()
plt.show()
