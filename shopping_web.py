from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTMLテンプレート（超シンプル版）
HTML_TEMPLATE = """
<!doctype html>
<html>
  <head>
    <title>買い物リスト</title>
    <meta charset="utf-8">
  </head>
  <body>
    <h1>🛒 買い物リスト</h1>
    <form method="POST">
      <input type="text" name="item" placeholder="商品を入力" required>
      <button type="submit">追加</button>
    </form>
    <ul>
      {% for item in items %}
        <li>{{ item }}</li>
      {% endfor %}
    </ul>
  </body>
</html>
"""

# 買い物リストをメモリ上で管理
shopping_items = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        item = request.form.get("item")
        if item:
            shopping_items.append(item)
    return render_template_string(HTML_TEMPLATE, items=shopping_items)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
