import pandas as pd
import matplotlib.pyplot as plt

# Les CSV-fil
df = pd.read_csv("Network_med_potensiometer.csv", delimiter=',', decimal='.', comment='#')

# Konverter kolonner
df['Frequency (Hz)'] = df['Frequency (Hz)'].astype(float)
df['Channel 1 Magnitude (dB)'] = df['Channel 1 Magnitude (dB)'].astype(float)
df['Channel 2 Magnitude (dB)'] = df['Channel 2 Magnitude (dB)'].astype(float)

# Filtrer ut kun data fra 1.0 kHz og opp
df = df[df['Frequency (Hz)'] >= 1000]

# Finn punkt nærmest 1.9 kHz
target_freq = 1900
closest_idx = (df['Frequency (Hz)'] - target_freq).abs().idxmin()
peak_freq_kHz = df['Frequency (Hz)'][closest_idx] / 1000
peak_value = df['Channel 2 Magnitude (dB)'][closest_idx]

# Lag plott
plt.figure(figsize=(12, 6))
plt.plot(df['Frequency (Hz)'] / 1000, df['Channel 1 Magnitude (dB)'], label='V₁(t)', color='darkorange')
plt.plot(df['Frequency (Hz)'] / 1000, df['Channel 2 Magnitude (dB)'], label='V₂(t)', color='royalblue')

# Marker 1.9 kHz punkt
plt.plot(peak_freq_kHz, peak_value, 'ko')
plt.axvline(peak_freq_kHz, color='black', linestyle='--')
plt.axhline(peak_value, color='black', linestyle='--')
plt.text(peak_freq_kHz + 0.05, peak_value + 2, f"{peak_value:.1f} dB", color='black')

# Legg til 1.9 som x-tick
xticks = list(plt.xticks()[0])
xticks.append(1.9)
xticks = sorted(set(xticks))
plt.xticks(xticks)

# 👇 Sørg for at grafen bare viser det aktuelle frekvensområdet
plt.xlim(df['Frequency (Hz)'].min() / 1000, df['Frequency (Hz)'].max() / 1000)

# Oppsett
plt.title("Nettverksanalyse")
plt.xlabel("Frekvens [kHz]")
plt.ylabel("Forsterkning [dB]")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
