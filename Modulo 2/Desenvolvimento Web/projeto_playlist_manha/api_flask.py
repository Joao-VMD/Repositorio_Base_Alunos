from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

playlist = [
    {"id":1, "titulo":"Always On Time", "artista":"Ja Rule", "link":"https://youtu.be/0tcDXJfAFVw?si=MI9fxqbS1o94CD-V"},
    {"id":2, "titulo":" Mesmerize", "artista":"Ja Rule", "link":"https://youtu.be/VcP96KbFIIU?si=wqy9iIRYhHHiuNqB"},
    {"id":3, "titulo":"baile inolvidable", "artista":"Bad Bunny", "link":"https://youtu.be/a1Femq4NPxs?si=Hs8e7oxuMxHwBkdC"}
    ]

@app.route("/musicas", methods=['GET'])
def get_musicas():
    return jsonify({"playlist":playlist, "total":len(playlist)})

@app.route("/musicas/<int:id>", methods=["GET"])
def get_musica(id):
    for musica in playlist:
        if musica["id"] == id:
            return jsonify(musica), 200
    return "",204    


@app.route("/musicas", methods=['POST'])
def add_musica():
    nova_musica = request.json
    nova_musica["id"] = len(playlist) + 1

    playlist.append(nova_musica)
    return jsonify({"mensagem": "Nova música adicionada!", "musica":nova_musica}), 201

app.run(host="0.0.0.0", debug=True)