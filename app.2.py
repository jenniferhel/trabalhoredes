from flask import Flask, render_template

app = Flask(_name_)

@app.route("/")
def index():
    connections = [
        [1, "Porta 1", "Painel 1", "Recepção 1"],
        [2, "Porta 2", "Painel 2", "Recepção 2"],
        [3, "Porta 3", "Painel 3", "Admin 1"],
        [4, "Porta 4", "Painel 4", "Admin 2"],
        [5, "Porta 5", "Painel 5", "Sala Clínica 1"],
        [6, "Porta 6", "Painel 6", "Sala Clínica 2"],
        [7, "Porta 7", "Painel 7", "Sala Clínica 3"],
        [8, "Porta 8", "Painel 8", "Sala Clínica 4"],
        [9, "Porta 9", "Painel 9", "Sala Clínica 5"],
        [10, "Porta 10", "Painel 10", "Sala Clínica 6"]
    ]
    return render_template("index.html", connections=connections)

if _name_ == "_main_":
    app.run(debug=True)