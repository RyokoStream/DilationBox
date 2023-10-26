from flask import Flask, render_template
import random

app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
    # αの目をサイコロでシミュレーション
    alpha_result = random.randint(1, 6)

    # αの目が奇数の場合、10面体サイコロβを振る
    if alpha_result % 2 == 1:
        beta_result = random.randint(0, 9)
        gamma_result = 0  # gamma_resultを初期化
    else:
        # αの目が偶数の場合、8面体サイコロγを振る
        gamma_result = random.randint(1, 8)
        beta_result = 0  # beta_resultを初期化

    # 新しい10面体サイコロδを振ってbを計算
    delta_result = random.randint(0, 9)
    b = beta_result * alpha_result if alpha_result % 2 == 1 else gamma_result * alpha_result

    # Cを計算
    C = b  # 仮の値。実際の計算方法に合わせて変更してください。

    # Cが40を超えた場合の処理
    if C > 40:
        d = C - (C % 40)
    else:
        d = C

    # εの目をサイコロでシミュレーション
    epsilon_result = random.randint(1, 6)

    # εの目が奇数の場合、dを"赤"に設定
    if epsilon_result % 2 == 1:
        d_color = "赤"
    else:
        d_color = "黄色"

    # HTMLテンプレートに結果を渡す
    return render_template('result.html', alpha_result=alpha_result, beta_result=beta_result, gamma_result=gamma_result, delta_result=delta_result, b=b, C=C, d=d, epsilon_result=epsilon_result, d_color=d_color)

if __name__ == '__main__':
    app.run()
