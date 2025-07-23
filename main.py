import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from scipy.interpolate import interp1d


def load_spectrogram_from_csv(filepath):
    """
    Loads spectrogram and environmental data from a CSV file.
    Returns: wavelength, normalized intensity, and a dictionary of environmental features.
    """
    df = pd.read_csv(filepath)
    wavelength = df['wavelength'].values
    intensity = df['intensity'].values
    intensity = intensity / np.linalg.norm(intensity)  # Normalize

    # Extract environmental parameters
    env_features = {
        'temperature': df['temperature'].iloc[0],
        'pressure': df['pressure'].iloc[0],
        'water_presence': df['water_presence'].iloc[0],
        'oxygen_level': df['oxygen_level'].iloc[0],
    }

    return wavelength, intensity, env_features


def interpolate_spectrogram(w1, i1, w2):
    """
    Interpolates the intensity values of spectrum 1 to match the wavelength range of spectrum 2.
    """
    f_interp = interp1d(w1, i1, bounds_error=False, fill_value=0)
    return f_interp(w2)


def calculate_similarity(intensity1, intensity2):
    return cosine_similarity([intensity1], [intensity2])[0][0]


def calculate_environmental_score(env_earth, env_exo):
    """
    Calculates similarity score between Earth and Exoplanet environmental conditions.
    """
    score = 0
    total = 4

    # Temperature similarity (allow +/- 20K window)
    if abs(env_earth['temperature'] - env_exo['temperature']) <= 20:
        score += 1

    # Pressure similarity (within 0.2 atm)
    if abs(env_earth['pressure'] - env_exo['pressure']) <= 0.2:
        score += 1

    # Water presence match
    if env_earth['water_presence'] == env_exo['water_presence']:
        score += 1

    # Oxygen level within ±5%
    if abs(env_earth['oxygen_level'] - env_exo['oxygen_level']) <= 5:
        score += 1

    return score / total  # Normalize to 0-1


def final_habitability_score(spec_score, env_score):
    """
    Combines spectral and environmental similarity into a single habitability score.
    """
    return 0.6 * spec_score + 0.4 * env_score


def assess_habitability(final_score):
    if final_score > 0.9:
        return "🌍 Very High Compatibility - Earth-like"
    elif final_score > 0.75:
        return "🪐 High Compatibility"
    elif final_score > 0.5:
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

    w_earth, i_earth, env_earth = load_spectrogram_from_csv(earth_path)
    w_exo, i_exo_raw, env_exo = load_spectrogram_from_csv(exoplanet_path)

    # Interpolate Earth data to match Exo wavelengths
    i_earth_interp = interpolate_spectrogram(w_earth, i_earth, w_exo)

    # Calculate spectral and environmental similarity
    spectral_score = calculate_similarity(i_earth_interp, i_exo_raw)
    environmental_score = calculate_environmental_score(env_earth, env_exo)

    # Final score
    final_score = final_habitability_score(spectral_score, environmental_score)
    status = assess_habitability(final_score)

    # Output results
    print(f"\n🔭 Spectral Similarity Score: {spectral_score:.4f}")
    print(f"🌡️ Environmental Score: {environmental_score:.4f}")
    print(f"✨ Final Habitability Score: {final_score:.4f}")
    print(f"🏁 Habitability Estimate: {status}\n")

    # Visualize
    visualize_spectrograms(w_exo, i_earth_interp, w_exo, i_exo_raw)
