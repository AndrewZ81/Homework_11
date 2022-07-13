from flask import Flask

app = Flask(__name__)


@app.route("/")
def main_page():
    page_content = """
    <h1>Смотри, это - моя страничка</h1>
    <p>Страничек много, но эта - моя!</p>
    <p>Фронтенд - мой лучший друг!</p>
    """
    return page_content

app.run()
