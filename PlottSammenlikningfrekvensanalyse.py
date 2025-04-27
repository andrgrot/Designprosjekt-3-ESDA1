import pandas as pd
import matplotlib.pyplot as plt

# Les CSV-data
df = pd.read_csv(
    "Spekteranalyse_sammelikning.csv", 
    delimiter=',', 
    decimal='.', 
    comment='#', 
    header=None,
    names=['Frequency_Hz', 'Channel_1_dB', 'Channel_1_Phase', 'Channel_2_dB', 'Channel_2_Phase']
)

# Konverter frekvens til kHz
df['Frequency_kHz'] = df['Frequency_Hz'] / 1000

# Finn nærmeste punkt til 1.9 kHz
target_freq = 1.9
closest_idx = (df['Frequency_kHz'] - target_freq).abs().idxmin()
amp1 = df['Channel_1_dB'][closest_idx]
amp2 = df['Channel_2_dB'][closest_idx]

# Plot
plt.figure(figsize=(12, 6))
plt.plot(df['Frequency_kHz'], df['Channel_1_dB'], label='V₁(t)', color='darkorange')
plt.plot(df['Frequency_kHz'], df['Channel_2_dB'], label='V₂(t)', color='royalblue')

# Horisontale striplete linjer ved amplitudetopper
plt.axhline(amp1, color='darkorange', linestyle='--', linewidth=1)
plt.axhline(amp2, color='royalblue', linestyle='--', linewidth=1)

# Marker punktene
plt.plot(1.9, amp1, 'o', color='darkorange')
plt.plot(1.9, amp2, 'o', color='royalblue')

# Legg til tekst ved siden av y-verdiene
plt.text(df['Frequency_kHz'].max() + 0.05, amp1, f"{amp1:.1f} dB", color='darkorange', va='center')
plt.text(df['Frequency_kHz'].max() + 0.05, amp2, f"{amp2:.1f} dB", color='royalblue', va='center')

# Legg 1.9 som x-tick
xticks = list(plt.xticks()[0])
xticks.append(1.9)
xticks = sorted(set(xticks))
plt.xticks(xticks)

# Stil og layout
plt.title("Sammenlikning av originalt signal (V₁(t)) og filtrert signal (V₂(t))")
plt.xlabel("Frekvens [kHz]")
plt.ylabel("Amplitude [dB]")
plt.grid(True)
plt.legend()
plt.xlim(df['Frequency_kHz'].min(), df['Frequency_kHz'].max())  # ekstra plass for tekst
plt.ylim(min(df['Channel_1_dB'].min(), df['Channel_2_dB'].min()) - 5,
         max(df['Channel_1_dB'].max(), df['Channel_2_dB'].max()) + 5)
plt.tight_layout()
plt.show()
