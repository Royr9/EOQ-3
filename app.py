
from flask import Flask, render_template, request, redirect, url_for
from game_objects.player import Player
from game_objects.game import load
from game_objects.demon import get_demon_by_name
from game_objects.items import Spell
import random
import pygame
import os
# Initialize pygame mixer
pygame.mixer.init()


app = Flask(__name__)
app.secret_key = 'fdkdlsfsbvbsadfsdf'

game_object = load()
level = game_object.get_current_level()
player = None
action_res = None
demon = None


@app.route("/fight", methods=["POST", "GET"])
def fight():
    global demon  # noqa: PLW0603
    spell = None
    action_description = None
    demon_attack = None
    # handle user action
    if request.method == "POST" and player and demon:
        # choose random spell and use it on the demon
        if request.form.get("attack"):
            user_spells = player.inventory.get_spells()
            spell = user_spells[random.randint(0, len(user_spells) - 1)]
            
            dmg_taken = demon.set_damage(spell.damage)
            action_description = f"{demon.name} has suffered {dmg_taken} damage"
        if request.form.get("heal"):
            heal_amount = player.heal(random.randint(20, 80))
            action_description = f"You have healed {heal_amount} hp"
        
        # demon attack
        # attack is a dict "attack description": "message": ,"Damage":
        demon_attack = demon.attack()
        if demon.name == "Timothy":
            file_path = os.path.join(os.getcwd(), "static", "tim.wav")
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            
        player.take_damage(demon_attack[1]["Damage"])
        
        if player.health == 0:
            return redirect(url_for("game_over"))
        
        if demon.health == 0:
            player.heal(150)
            if demon.name == "Frank":
                return redirect(url_for("game_won"))
            
            game_object.get_current_level().kill_demon()
            demon = None
            return redirect("/")
            
    return render_template("fight.html", demon=demon, demon_attack=demon_attack, player=player, spell=spell, action_description=action_description)

@app.route("/game_won")
def game_won():
    return render_template("game_won.html")


@app.route("/game_over")
def game_over():
    return render_template("game_over.html")

@app.route("/restart", methods=["POST"])
def restart_game():
    global player, action_res, demon, level, game_object
    game_object = load()
    level = game_object.get_current_level()
    player = None
    action_res = None
    demon = None
    return redirect("start-game")

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
    global action_res, player  # noqa: PLW0602
    if not player:
        return redirect("/start-game")
    location = game_object.get_current_level().get_current_location()
    actions = location.get_action_names()
    return render_template('game.html', location=location, actions=actions, player=player, action_res=action_res)


@app.route('/choose_action', methods=['POST'])
def choose_action():
    global action_res, demon  # noqa: PLW0603
    action_name = request.form.get('action')
    location = game_object.get_current_level().get_current_location()

    if not game_object.get_current_level().is_demon_killed() and "Fight" in action_name or "Disturb" in action_name:
        demon = get_demon_by_name(location.demon)
        if demon and demon.name != "Frank":
            demon.health = 30
        demon = get_demon_by_name("Frank")
        return redirect(url_for("fight"))

    if action_name in location.get_action_names():
        action_res = location.get_action(action_name).use(game_object, player)
        return redirect(url_for('game'))

    return redirect(url_for('game'))


if __name__ == "__main__":
    app.run(debug=True)
