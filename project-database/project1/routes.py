from my_project.app import app, db
from my_project.models import Games

@app.route('/add')
def add():
    new_game = Games(name="New Game")
    db.session.add(new_game)
    db.session.commit()
    return "Added new game to database"

@app.route('/read')
def read():
    all_games = Games.query.all()
    games_string = ""
    for game in all_games:
        games_string += "<br>"+ game.name
    return games_string

@app.route('/update/<name>')
def update(name):
    first_game = Games.query.first()
    first_game.name = name
    db.session.commit()
    return first_game.name

###### website basics #####

# @app.route('/')
# @app.route('/home')
# def hpme(): 
#    return "Home page"

# @app.route('/about')
# def about_page():
#    return "About page" 

# @app.route('/squared/<num>')
# def squared(num):
#    number = int(num)
#    result = number*number
#    return str(result)