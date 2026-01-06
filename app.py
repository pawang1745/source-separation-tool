import os
import subprocess
from flask import Flask, render_template, request, send_from_directory

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs/demucs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def index():
    output_files = []

    if request.method == "POST":
        audio = request.files["audio"]
        audio_path = os.path.join(UPLOAD_FOLDER, audio.filename)
        audio.save(audio_path)

        # Run Demucs
        subprocess.run([
            "demucs",
            "-n", "htdemucs",
            audio_path,
            "-o", OUTPUT_FOLDER
        ])

        song_name = os.path.splitext(audio.filename)[0]
        stem_dir = os.path.join(OUTPUT_FOLDER, "htdemucs", song_name)

        for stem in os.listdir(stem_dir):
            output_files.append(f"htdemucs/{song_name}/{stem}")

    return render_template("index.html", files=output_files)


@app.route("/download/<path:filename>")
def download(filename):
    return send_from_directory(OUTPUT_FOLDER, filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
