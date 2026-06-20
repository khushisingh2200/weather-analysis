# Weather CLI Tool

A Python command line tool that fetches real-time weather data 
using REST APIs and JSON parsing.

---

## What This Project Does

1. Takes a city name as input
2. Calls the Open-Meteo geocoding API to get coordinates
3. Uses coordinates to fetch current weather data
4. Displays temperature, wind speed, wind direction, and daytime status
5. Handles errors — connection errors, timeouts, and invalid city names

---

## Project Structure

    weather-cli/
    ├── main.py
    ├── requirements.txt
    └── readme.md

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| requests | REST API calls |
| JSON | Parsing API response |

---

## APIs Used

- Open-Meteo Geocoding API
- Open-Meteo Forecast API
- Both free, no API key required

---

## How to Run

**Step 1 — Install dependencies:**
```bash
pip install -r requirements.txt
```

**Step 2 — Run:**
```bash
python main.py
```

---

## Error Handling

- Connection Error — no internet connection
- Timeout Error — API not responding
- Invalid city name — spelling error detected