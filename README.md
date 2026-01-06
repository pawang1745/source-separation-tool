# Source Separation Tool

A small Flask-based tool for separating audio sources (vocals, drums, bass, etc.) using local separation models. This repo contains the web UI and helper scripts to run a separation pipeline.

## Quick start

1. Create and activate a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python app.py
```

The web UI is served from `templates/index.html` and static assets in `static/`.

## Notes

- Large model files and outputs are stored in `outputs/` and are excluded from the repo via `.gitignore`.
- For deployment, consider configuring an appropriate production server and model storage.
