
# 🗺️ Google Maps Scraper

A Python project that extracts business information from **Google Maps**, including:

* Name
* Address
* Phone number
* Website
* Coordinates (Latitude, Longitude)
* Ratings & reviews

Results are saved in CSV format inside the `GMaps Data/` folder.

---

## 📌 Versions

### 1️⃣ Old Version – CLI Scraper

* Pure Python project.
* User provides search query & number of results in code.
* Runs in terminal (`python main.py`).
* Outputs results in **CSV** inside `GMaps Data/`.

Folder structure (old):

```
google_maps_scraper/
└─ Googles-Maps-Scraper/
   ├─ GMaps Data/
   ├─ main.py
   ├─ requirements.txt
   └─ venv/
```

---

### 2️⃣ New Version – Flask Web App (Default 🚀)

* Includes a **Flask-based UI**.
* User enters **search query + number of results** directly from a web form.
* Results are displayed in a **styled HTML table** and can be **downloaded as CSV**.
* Uses **Bootstrap + custom CSS** for a clean frontend.

Folder structure (new):

```
google_maps_scraper/
└─ Googles-Maps-Scraper/
   ├─ GMaps Data/          # Saved results
   ├─ static/              # CSS (style.css)
   ├─ templates/           # HTML templates
   │  ├─ base.html
   │  ├─ index.html
   │  └─ results.html
   ├─ main.py              # Scraping logic
   ├─ app.py               # Flask app
   ├─ requirements.txt
   └─ venv/
```

---

## ⚙️ Installation

Clone the repo:

```bash
git clone https://github.com/your-username/Google-Maps-Scraper.git
cd Google-Maps-Scraper
```

Create a virtual environment & install dependencies:

```bash
python -m venv venv
venv\Scripts\activate    # On Windows
source venv/bin/activate # On Linux/Mac

pip install -r requirements.txt
```

---

## ▶️ Run

### 🔹 Flask App (Default)

```bash
python app.py
```

Open in browser → [http://127.0.0.1:5000](http://127.0.0.1:5000)

You can:

* Enter your **query & result count**
* View results in table format
* Download results as CSV

### 🔹 CLI Scraper (Legacy)

```bash
python main.py
```

Edit the `main.py` query and run from terminal.

---

## 📂 Branches

* **main** → Flask Web App (default)
* **cli-version** → Old terminal version

---

## 🚀 Features

✔️ Scrapes businesses from Google Maps
✔️ Saves results as CSV
✔️ Flask web UI with table + download option
✔️ Clean frontend with Bootstrap styling
✔️ Supports both CLI & Flask modes

---

Would you like me to **write it in a way that GitHub shows screenshots/demo GIFs** too (so people instantly see how it looks), or keep it text-only for now?
