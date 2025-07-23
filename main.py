# ExoHabit - main.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cosine


def generate_earth_spectrogram():
    """
    Simulated Earth spectrum with peak absorption features for O2, CO2, CH4
    """
    wavelengths = np.linspace(0.5, 2.5, 500)
    spectrum = (
        np.exp(-((wavelengths - 0.76) ** 2) / 0.01) +  # O2 peak
        np.exp(-((wavelengths - 1.5) ** 2) / 0.03) +    # CO2 peak
        np.exp(-((wavelengths - 2.3) ** 2) / 0.01)      # CH4 peak
    )
    return wavelengths, spectrum


def generate_exoplanet_spectrogram():
    """
    Simulated exoplanet spectrum with partially matching features
    """
    wavelengths = np.linspace(0.5, 2.5, 500)
    spectrum = (
        0.8 * np.exp(-((wavelengths - 0.76) ** 2) / 0.01) +  # weak O2
        np.exp(-((wavelengths - 1.5) ** 2) / 0.03) +          # CO2
        0.1 * np.random.rand(500)                            # noise
    )
    return wavelengths, spectrum


def compute_similarity(earth_spectrum, planet_spectrum):
    """
    Calculate cosine similarity between Earth and exoplanet spectra
    """
    return 1 - cosine(earth_spectrum, planet_spectrum)


if __name__ == "__main__":
    # Generate spectra
    wl, earth = generate_earth_spectrogram()
    _, exo = generate_exoplanet_spectrogram()

    # Compute habitability score
    score = compute_similarity(earth, exo) * 100
    print(f"\n🌍 Habitability Compatibility Score: {score:.2f}%\n")

    # Plot the spectrograms
    plt.figure(figsize=(10, 5))
    plt.plot(wl, earth, label='🌍 Earth Spectrum', color='blue')
    plt.plot(wl, exo, label='🪐 Exoplanet Spectrum', color='orange')
    plt.title('Spectrogram Comparison - Earth vs Exoplanet')
    plt.xlabel('Wavelength (micron)')
    plt.ylabel('Intensity')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
