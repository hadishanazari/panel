from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = "data.json"

# --- توابع کمکی ---
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {"boxText": "", "boxColor": "blanchedalmond"}

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# --- سایت اصلی ---
@app.route("/")
def index():
    data = load_data()
    return render_template("index.html", boxText=data["boxText"], boxColor=data["boxColor"])

# --- پنل مدیریت ---
@app.route("/admin", methods=["GET", "POST"])
def admin():
    data = load_data()
    if request.method == "POST":
        # گرفتن داده‌ها از فرم
        boxText = request.form.get("boxText", "")
        boxColor = request.form.get("boxColor", "blanchedalmond")
        data["boxText"] = boxText
        data["boxColor"] = boxColor
        save_data(data)
        return redirect(url_for("admin"))
    return render_template("admin.html", boxText=data["boxText"], boxColor=data["boxColor"])

# --- API برای تغییر سریع باکس (اختیاری) ---
@app.route("/api/box", methods=["GET"])
def api_box():
    data = load_data()
    return jsonify(data)

# --- اجرا ---
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
