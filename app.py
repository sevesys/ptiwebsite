from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        form_data = request.form
        for item in form_data:
            print(form_data[item])
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)