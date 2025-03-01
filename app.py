import os
from flask import Flask, jsonify, send_from_directory, render_template, redirect 

app = Flask(__name__)

@app.route("/")
def home():
    return redirect("/calls")
    

@app.route("/calls")
def calls_page():
    return render_template("index.html")


turkey_calls = [
    {"name": "Cluck and Purr", "description": "A mix of clucks and purrs for soft turkey communication.", "audio": "Cluck_and_Purr.mp3"},
    {"name": "Clucks", "description": "Short, soft notes to reassure turkeys.", "audio": "Clucks.mp3"},
    {"name": "Cutting", "description": "Excited and aggressive yelps to attract attention.", "audio": "Cutting.mp3"},
    {"name": "Excited Hen Yelps", "description": "A loud series of yelps to call in turkeys.", "audio": "Excited_Hen_Yelps.mp3"},
    {"name": "Fly Down Cackles", "description": "Used when turkeys fly down from the roost.", "audio": "Fly_Down_Cackles.mp3"},
    {"name": "Gobbling", "description": "The dominant gobble of a tom turkey.", "audio": "Gobbling.mp3"},
    {"name": "Kee Kee Run", "description": "A young turkey's lost call.", "audio": "Kee_Kee_Run.mp3"},
    {"name": "Old Hen Assembly Yelp", "description": "A long series of yelps to gather turkeys.", "audio": "Old_Hen_Assembly_Yelp.mp3"},
    {"name": "Plain Hen Yelp", "description": "A standard yelp from a hen turkey.", "audio": "Plain_Hen_Yelp.mp3"},
    {"name": "Purrs", "description": "Soft rolling calls when turkeys are calm.", "audio": "Purrs.mp3"},
    {"name": "Putts", "description": "Sharp notes often used as alarm calls.", "audio": "Putts.mp3"},
    {"name": "Tree Calling", "description": "Soft calls made by turkeys while on the roost.", "audio": "Tree_Calling.mp3"}
]

@app.route("/api/calls", methods=["GET"])
def get_calls():
    return jsonify(turkey_calls)

# ✅ Route to Serve Audio Files (Do Not Remove This)
@app.route("/sounds/<path:filename>")
def get_sound(filename):
    sounds_dir = os.path.join(app.root_path, "sounds")
    return send_from_directory(sounds_dir, filename)

if __name__ == "__main__":
    app.run(debug=True)
