from string import printable

from flask import Flask, render_template, request, redirect, url_for
from game_objects.player import Player
from game_objects.game import load

app = Flask(__name__)
app.secret_key = 'fdkdlsfsbvbsadfsdf'

game_object = load()
print(game_object.get_current_level())
player = None
action_res = None

@app.route("/start-game", methods=['GET', 'POST'])

def start_game():
    global player  # noqa: PLW0603
    if request.method == "GET":
        return render_template("start-screen.html")
    
    player = Player(request.form.get("username"), health=100)
    
    return redirect("/")
    

@app.route('/')
def game():
    global action_res, player
    if not player:
        return redirect("/start-game")
    location = game_object.get_current_level().get_current_location()
    actions = location.get_action_names()
    return render_template('game.html', location=location, actions=actions, player=player, action_res=action_res)

@app.route('/choose_action', methods=['POST'])
def choose_action():
    global action_res  # noqa: PLW0603
    action_name = request.form.get('action')
    location = game_object.get_current_level().get_current_location()

    if action_name in location.get_action_names():
        action_res = location.get_action(action_name).use(game_object, player)
        return redirect(url_for('game'))

    return redirect(url_for('game'))

if __name__ == "__main__":
    app.run(debug=True)
