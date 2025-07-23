# 🌍🚀 ExoHabit: Discover Earth 2.0 with AI 🪐

![space telescope](https://media.tenor.com/0pEZ6_oKBIEAAAAC/nasa-james-webb.gif)

> **"Somewhere, something incredible is waiting to be known." – Carl Sagan**

**ExoHabit** is an AI-powered space research project using real and simulated spectrogram data from exoplanets to detect habitability. It compares light signatures from distant worlds with Earth’s biosignature to find our next potential home in the stars.

---

## 🌠 What Is ExoHabit?

ExoHabit uses the **James Webb Space Telescope (JWST)**'s spectrograms to:

- 🔬 Detect key molecules like O₂, CH₄, CO₂ in planetary atmospheres
- 🧠 Compare with Earth’s light signature
- 🧪 Calculate a **habitability compatibility score**
- 📈 Visualize side-by-side spectrograms

> ✨ This is your AI companion for exploring habitable worlds across galaxies.

---

## 🚀 Live from the Universe

![planet scan](https://media.giphy.com/media/WFZvB7VIXBgiz3oDXE/giphy.gif)

JWST beams data from far-off exoplanets.  
ExoHabit reads the **infrared spectrum**, identifies chemical markers, and evaluates if the planet could host Earth-like life.

---

## 🛠️ Tech Stack

- Python 3.11+
- `numpy`, `scipy`, `pandas`
- `scikit-learn`, `matplotlib`, `seaborn`
- `astropy`, `specutils`

---

## 🧪 Sample Output

![spectral analysis](https://upload.wikimedia.org/wikipedia/commons/c/cb/Exoplanet_Spectra_-_NASA.gif)

```text
🪐 Planet: Kepler-1649c
✔️ O₂ Detected
✔️ CH₄ Detected
❌ H₂O Missing

✅ Habitability Score: 86.7%



## 📁 Project Structure

```bash
ExoHabit/
├── data/                     # Sample spectra (Earth, exoplanets)
├── notebooks/                # Jupyter exploration and EDA
├── src/
│   ├── preprocessing.py      # Clean and normalize spectral data
│   ├── feature_extraction.py # Detect molecules & features
│   ├── model.py              # ML model for scoring
│   └── evaluate.py           # Compatibility score logic
├── main.py                   # Run everything in one go!
├── requirements.txt
└── README.md
# ExoHabit-A-Spectrogram-Based-Habitability-Analysis-Model

Sample Output

🧪 Habitability Score: 88.3%
✅ "This planet contains strong O₂ and CH₄ signatures, within the habitable zone. Compatible with Earth-like life."

 Future Possibilities
🌐 Use real JWST data from MAST

🧬 Deep learning on high-res spectra

🛰️ Dashboard to explore planets interactively (Streamlit/Gradio)

🌎 Terraforming suggestions for low-score planets

 Contributing
Pull requests are welcome! Found a better way to model alien life? Let’s explore together!

git clone https://github.com/yourusername/ExoHabit.git
cd ExoHabit
pip install -r requirements.txt
python main.py

📖 License
This project is licensed under the MIT License — free to use, explore, and extend.

✨ Final Thought

🌌 “ExoHabit is not just about planets — it's about possibilities.”

💫 Made with love, science, and stars.

