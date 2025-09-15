from flask import Flask, request, send_file, render_template_string, abort
import pandas as pd
from datetime import datetime
import os

app = Flask(__name__)

LOG_FILE = "phish_log.xlsx"

# إنشاء الملف لو لم يكن موجود
if not os.path.exists(LOG_FILE):
    df = pd.DataFrame(columns=["Timestamp", "Email"])
    df.to_excel(LOG_FILE, index=False)

# صفحة التسجيل
HTML = '''
<!DOCTYPE html>
<html lang="ar">
<head>
<meta charset="UTF-8">
<title>سجل معنا وفوز!</title>
</head>
<body>
<h1>سجل معنا وفوز بالقهوة والدونات!</h1>
{% if email %}
    <p>شكراً لتسجيلك: {{ email }}</p>
{% else %}
    <form method="post">
        Email: <input type="email" name="email" required><br>
        <input type="submit" value="سجل الآن">
    </form>
{% endif %}
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def home():
    email = None
    if request.method == "POST":
        email = request.form.get("email")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # اقرأ الملف، أضف الصف، واحفظ
        try:
            df = pd.read_excel(LOG_FILE)
        except Exception:
            df = pd.DataFrame(columns=["Timestamp", "Email"])
        df = pd.concat([df, pd.DataFrame([[timestamp, email]], columns=df.columns)], ignore_index=True)
        df.to_excel(LOG_FILE, index=False)
    return render_template_string(HTML, email=email)

# صفحة لتحميل سجل الإيميلات
@app.route("/download-log")
def download_log():
    if os.path.exists(LOG_FILE):
        return send_file(LOG_FILE, as_attachment=True)
    else:
        return "File not found!", 404

# صفحة مخفية لعرض التسجيلات مع حماية بكلمة سر
@app.route("/submissions")
def show_submissions():
    secret = os.environ.get("SUBMISSIONS_PASS", "changeme")
    provided = request.args.get("pass", "")
    if provided != secret:
        abort(403)

    if not os.path.exists(LOG_FILE):
        return "<h3>لا يوجد سجلات حالياً.</h3>"
    try:
        df = pd.read_excel(LOG_FILE)
    except Exception:
        return "<h3>حدث خطأ أثناء قراءة الملف.</h3>"

    page = "<h2>📋 قائمة المسجلين</h2><table border='1' cellpadding='6'><tr><th>Timestamp</th><th>Email</th></tr>"
    for _, row in df.iterrows():
        page += f"<tr><td>{row.get('Timestamp','')}</td><td>{row.get('Email','')}</td></tr>"
    page += "</table>"
    return page

# تشغيل التطبيق على المنفذ الصحيح للـ Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
