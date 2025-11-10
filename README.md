# 🎨 Met Museum Collections Search API

An interactive Museum Collections API built with **Streamlit** and **Python**, using the **Metropolitan Museum of Art Public API**.  
Search and explore artworks dynamically with real museum data.

---

## 🌍 Features
- Search The Met Museum collections by keyword
- Display image, title, artist, date, and museum link
- Limit results to 20 items for performance
- Fully dynamic using The Met API

---

## 🚀 How to Run Locally
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/museum-collections-api-met.git
   cd museum-collections-api-met
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run Streamlit:
   ```bash
   streamlit run app.py
   ```

---

## ☁️ Deploy on Streamlit Cloud
1. Push your repository to GitHub  
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)  
3. Select your repo and deploy — done!

---

## 🧠 Customization
- Change the number of results returned by modifying the slice `objectIDs[:20]` in `app.py`.
- UI is fully customizable in `app.py`.

---

## 📄 License
MIT License © 2025
