from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <title>سجل معنا وفوز!</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: url('/static/donuts.jpg') no-repeat center center fixed;
            background-size: cover;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background-color: rgba(255, 255, 255, 0.9);
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        }
        input[type="email"] {
            padding: 10px;
            width: 250px;
            border-radius: 5px;
            border: 1px solid #ccc;
            margin-bottom: 10px;
        }
        button {
            padding: 10px 20px;
            border: none;
            background-color: #ff4d4d;
            color: white;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            transition: transform 0.2s;
        }
        button:hover {
            transform: scale(1.05);
        }
        h1 {
            color: #ff4d4d;
        }
        p {
            font-size: 18px;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>سجل معنا وفوز بالقهوة والدونات!</h1>
        {% if email %}
            <p>شكراً لتسجيلك: {{ email }}</p>
        {% else %}
            <form method="post">
                <input type="email" name="email" placeholder="اكتب إيميلك هنا" required><br>
                <button type="submit">سجل الآن</button>
            </form>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    email = None
    if request.method == 'POST':
        email = request.form['email']
    return render_template_string(HTML, email=email)

if __name__ == '__main__':
    app.run(debug=True)
