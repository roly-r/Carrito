from flask import Flask, render_template,request, session, redirect, url_for

app = Flask(__name__)

app.secret_key = 'unaclavesecreta'

@app.route("/")
def carrito():
    if 'lista' not in session:
        session['lista'] = []
    return render_template('index.html', lista = session['lista'])

@app.route("/proceso", methods=['GET', 'POST'])
def procesa():
    producto = request.form.get("producto")
    if 'lista' in session and producto:
        session['lista'].append(producto)
        session.modified = True
    return redirect(url_for("carrito"))

@app.route("/vaciar", methods=["GET"])
def vaciar():
    session.pop("lista", None)
    return redirect(url_for("carrito"))


if __name__ == "__main__":
    app.run(debug=True)