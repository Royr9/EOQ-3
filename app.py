from flask import Flask, render_template, request, redirect, url_for, session
from game_objects.player import Player
from game_objects.level import load

app = Flask(__name__)
app.secret_key = 'fdkdlsfsbvbsadfsdf'

levels = load()
level = levels[0]
player = Player(name="notDemonFrank", health=100)

@app.route('/')
def game():
    location = level.get_current_location()
    actions = location.get_action_names()

    return render_template('game.html', location=location, actions=actions)

@app.route('/choose_action', methods=['POST'])
def choose_action():
    action_name = request.form.get('action')
    location = level.get_current_location()

    if action_name in location.get_action_names():
        location.get_action(action_name).use(level, player)
        return redirect(url_for('game'))

    return redirect(url_for('game'))

if __name__ == "__main__":
    app.run(debug=True)
