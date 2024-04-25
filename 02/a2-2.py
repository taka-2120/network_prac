import datetime

from flask import Flask, render_template

# flaskモジュールからFlaskクラスとrender_templateメソッドをインポートする

app = Flask(__name__)
# Flaskインスタンスを生成する．


@app.route("/")
def template():
    time = datetime.datetime.now()
    return render_template(
        "a2-2.html", title="現在時刻", h=time.hour, min=time.minute, sec=time.second
    )


if __name__ == "__main__":
    # このプログラムが直接起動されたものであれば以下を実行する．
    app.debug = True
    # デバッグ機能をONにする．
    app.run(host="localhost", port=8000)
    # ホスト名をlocalhostにして，Webアプリケーションを起動する．
