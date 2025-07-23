import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from scipy.interpolate import interp1d


def load_spectrogram_from_csv(filepath):
    """
    Loads spectrogram data from a CSV file with 'wavelength' and 'intensity' columns.
    Returns: numpy arrays of wavelength and normalized intensity.
    """
    df = pd.read_csv(filepath)
    wavelength = df['wavelength'].values
    intensity = df['intensity'].values
    intensity = intensity / np.linalg.norm(intensity)  # Normalize
    return wavelength, intensity


def interpolate_spectrogram(w1, i1, w2):
    """
    Interpolates the intensity values of spectrum 1 to match the wavelength range of spectrum 2.
    """
    f_interp = interp1d(w1, i1, bounds_error=False, fill_value=0)
    return f_interp(w2)


def calculate_similarity(intensity1, intensity2):
    return cosine_similarity([intensity1], [intensity2])[0][0]


def assess_habitability(similarity_score):
    """Returns habitability interpretation based on similarity."""
    if similarity_score > 0.9:
        return "🌍 Very High Compatibility - Earth-like"
    elif similarity_score > 0.75:
        return "🪐 High Compatibility"
    elif similarity_score > 0.5:
        return "🌗 Moderate Compatibility"
    else:
        return "🛸 Low Compatibility"


def visualize_spectrograms(w_earth, i_earth, w_exo, i_exo):
    plt.figure(figsize=(10, 5))
    plt.plot(w_earth, i_earth, label="Earth", color='blue')
    plt.plot(w_exo, i_exo, label="Exoplanet", color='orange')
    plt.title("Spectrogram Comparison")
    plt.xlabel("Wavelength")
    plt.ylabel("Normalized Intensity")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # Load CSV data
    earth_path = "earth_spectrogram.csv"
    exoplanet_path = "exo_spectrogram.csv"

    w_earth, i_earth = load_spectrogram_from_csv(earth_path)
    w_exo, i_exo_raw = load_spectrogram_from_csv(exoplanet_path)

    # Interpolate Earth data to match Exo wavelengths
    i_earth_interp = interpolate_spectrogram(w_earth, i_earth, w_exo)

    # Calculate similarity and assess habitability
    similarity = calculate_similarity(i_earth_interp, i_exo_raw)
    status = assess_habitability(similarity)

    # Output results
    print(f"\n🔭 Spectral Similarity Score: {similarity:.4f}")
    print(f"🏁 Habitability Estimate: {status}\n")

    # Visualize
    visualize_spectrograms(w_exo, i_earth_interp, w_exo, i_exo_raw)
