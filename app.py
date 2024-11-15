# from string import printable

from flask import Flask, render_template, request, redirect, url_for
from game_objects.player import Player
from game_objects.game import load
from game_objects.demon import get_demon_by_name
from game_objects.items import Spell


app = Flask(__name__)
app.secret_key = 'fdkdlsfsbvbsadfsdf'

game_object = load()
level = game_object.get_current_level()
player = None
action_res = None
demon = None



@app.route("/fight", methods=["POST", "GET"])
def fight():
    global demon  # noqa: PLW0602
    spell = None
    action_description = None
    demon_attack = None
    # handle user action
    if request.method == "POST" and player and demon:
        # choose random spell and use it on the demon
        if request.form.get("attack"):
            spell = player.inventory.get_spells()[0]
            dmg_taken = demon.set_damage(spell.damage)
            action_description = f"{demon.name} has suffered {dmg_taken} damage"
        if request.form.get("heal"):
            heal_amount = player.heal(15)
            action_description = f"You have healed {heal_amount} hp"
        
        # demon attack
        # attack is a dict "attack description": "message": ,"Damage":
        demon_attack = demon.attack()
        player.take_damage(demon_attack[1]["Damage"])

    return render_template("fight.html", demon=demon, demon_attack=demon_attack, player=player, spell=spell, action_description=action_description)


@app.route("/start-game", methods=['GET', 'POST'])
def start_game():
    global player  # noqa: PLW0603
    if request.method == "GET":
        return render_template("start-screen.html")
    
    player = Player(request.form.get("username"), health=100)
    player.inventory.add_item(Spell(level.level))
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
    global action_res, demon  # noqa: PLW0603
    action_name = request.form.get('action')
    location = level.get_current_location()

    if location.demon and action_name != "Go back":
        demon = get_demon_by_name(location.demon)
        return redirect(url_for("fight"))
    
    if action_name in location.get_action_names():
        action_res = location.get_action(action_name).use(game_object, player)
        return redirect(url_for('game'))

    return redirect(url_for('game'))

if __name__ == "__main__":
    app.run(debug=True)
