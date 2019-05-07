from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")

def page():
	return render_template('elliotdev.html')

# @app.route("/")
# def style():
# 	return url_for('static', filename="style.css")



if __name__ == "__main__":
	app.run()
