
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
        background: rgba(255,255,255,0.94);
        width: 420px;               /* عرض المستطيل */
        max-width: 92%;
        padding: 26px 28px;         /* حشوة داخلية */
        border-radius: 12px;        /* أقل تقويس -> مستطيل أقل مدور */
        text-align: center;
        box-shadow: 0 8px 30px rgba(0,0,0,0.18);
    }
    h1 {
        margin: 0 0 14px 0;
        font-size: 22px;
        color: #222;
    }
    input[type=email] {
        padding: 10px 12px;
        width: calc(100% - 24px);
        margin-bottom: 14px;
        border-radius: 6px;
        border: 1px solid #ddd;
        font-size: 15px;
        box-sizing: border-box;
    }
    input[type=submit] {
        padding: 10px 20px;
        border: none;
        border-radius: 8px;
        background-color: #1e88e5;   /* زر أزرق */
        color: white;
        cursor: pointer;
        font-size: 16px;
        box-shadow: 0 6px 14px rgba(30,136,229,0.18);
        transition: transform .12s ease, box-shadow .12s ease;
    }
    input[type=submit]:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 22px rgba(30,136,229,0.25);
    }
    /* للهواتف */
    @media (max-width:480px){
      .container { width: 95%; padding:18px; }
      h1 { font-size:18px; }
    }
</style>

<script>
    function showPopup(email) {
        if (email) {
            // استخدام template literal مع إسكات هروب علامات الاقتباس
            const msg = `حي عينك اخوي نينجا!\n\n⚠️ قلنا مليون مرة: لا تضغط على أي رابط غريب أو مشبوه — موب منطقي انك صدقت!!\n\nاليوم كان مقلب بسيط، لكن في الواقع ممكن تكون هجمة حقيقة 🚨\n⚠️ جدياً — لا تفتح أي رابط مشبوه قبل تتأكد من العنوان: ${email}`;
            alert(msg);
        }
    }
</script>
</head>
<body>
<div class="container">
{% if email %}
    <script>showPopup("{{ email|e }}");</script>
    <h1>شكراً لتسجيلك!</h1>
    <p>تم استلام الايميل: <strong>{{ email|e }}</strong></p>
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
