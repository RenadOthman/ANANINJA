from flask import Flask, request, send_file, render_template_string
import pandas as pd
from datetime import datetime
import os

app = Flask(__name__)

LOG_FILE = "phish_log.xlsx"

# إنشاء الملف لو لم يكن موجود
if not os.path.exists(LOG_FILE):
    df = pd.DataFrame(columns=["Timestamp", "Email"])
    df.to_excel(LOG_FILE, index=False)

HTML = '''
<!DOCTYPE html>
<html lang="ar">
<head>
<meta charset="UTF-8">
<title>سجل معنا وفوز!</title>
<style>
    body {
        background-image: url('https://www2.0zz0.com/2025/09/16/11/929822793.png');
        background-size: cover;
        font-family: Arial, sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
    }
    .container {
        background: rgba(255,255,255,0.9);
        padding: 40px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 0 20px rgba(0,0,0,0.3);
    }
    input[type=email] {
        padding: 10px;
        width: 80%;
        margin-bottom: 15px;
        border-radius: 5px;
        border: 1px solid #ccc;
    }
    input[type=submit] {
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        background-color: #ff5722;
        color: white;
        cursor: pointer;
        font-size: 16px;
    }
</style>
<script>
    function showPopup(email) {
        if(email) {
            alert("حي عينك اخوي نينجا 
⚠️  قلنا مليون مرة: لا تضغط على أي رابط غريب أو مشبوه؟ موب منطقي انك صدقت!! 
اليوم كان مقلب بسيط، لكن في الواقع ممكن تكون هجمة حقيقة 🚨
⚠️ جدياً — لا تفتح أي رابط مشبوه قبل تتأكد من العنوان " + email);
        }
    }
</script>
</head>
<body>
<div class="container">
{% if email %}
    <script>showPopup("{{ email }}");</script>
{% else %}
    <h1>سجل معنا وفوز!</h1>
    <form method="post">
        <input type="email" name="email" placeholder="أدخل بريدك الإلكتروني" required><br>
        <input type="submit" value="سجل الآن">
    </form>
{% endif %}
</div>
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def home():
    email = None
    if request.method == "POST":
        email = request.form.get("email")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            df = pd.read_excel(LOG_FILE)
        except Exception:
            df = pd.DataFrame(columns=["Timestamp", "Email"])
        df = pd.concat([df, pd.DataFrame([[timestamp, email]], columns=df.columns)], ignore_index=True)
        df.to_excel(LOG_FILE, index=False)
    return render_template_string(HTML, email=email)

# صفحة عرض الإيميلات المحمية بكلمة مرور
@app.route("/submissions")
def submissions():
    password = request.args.get("pass")
    if password != "mysecret123":
        return "Unauthorized", 403
    if os.path.exists(LOG_FILE):
        df = pd.read_excel(LOG_FILE)
        return df.to_html(index=False)
    else:
        return "No submissions yet!"

@app.route("/download-log")
def download_log():
    if os.path.exists(LOG_FILE):
        return send_file(LOG_FILE, as_attachment=True)
    else:
        return "File not found!", 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
