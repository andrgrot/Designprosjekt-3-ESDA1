import pandas as pd
import matplotlib.pyplot as plt

# Last inn og klargjør data
df = pd.read_csv("spectrum_V1(t).csv", skiprows=30)
df.columns = ['Frequency_Hz', 'Amplitude_dBV', 'Phase_deg']
df.dropna(inplace=True)

# Finn punkt nærmest 1900 Hz
freq_target = 1900
closest_idx = (df['Frequency_Hz'] - freq_target).abs().idxmin()
peak_freq = df['Frequency_Hz'][closest_idx] / 1000  # i kHz
peak_value = df['Amplitude_dBV'][closest_idx]

# Plot
plt.figure(figsize=(10, 5))
plt.plot(df['Frequency_Hz'] / 1000, df['Amplitude_dBV'], color='firebrick')

# Marker punkt, linjer og verdi
plt.plot(peak_freq, peak_value, 'ko')
plt.axhline(peak_value, color='black', linestyle='--', linewidth=1)
plt.axvline(peak_freq, color='black', linestyle='--', linewidth=1)
plt.text(peak_freq + 0.05, peak_value + 2, f"{peak_value:.1f} dBV", color='black')

# ➕ Legg til 1.9 som tick på x-aksen
xticks = list(plt.xticks()[0])         # hent eksisterende xticks
xticks.append(1.9)                     # legg til 1.9
xticks = sorted(set(xticks))          # sorter og fjern duplikater
plt.xticks(xticks)                    # sett de nye tickene

# Oppsett
plt.title("Frekvensspekter")
plt.xlabel("Frekvens [kHz]")
plt.ylabel("Amplitude [dBV]")
plt.grid(True)
plt.xlim(0, df['Frequency_Hz'].max() / 1000)
plt.ylim(df['Amplitude_dBV'].min() - 5, df['Amplitude_dBV'].max() + 5)
plt.tight_layout()
plt.show()
