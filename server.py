"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the home page.
    <a href="http://localhost:5000/hello">Hello</a></html>"""
    # <a href="http://localhost:5000/hello">Hello</a>

    


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit">

          <br>
          <br>Select a compliment from menu<br> 
          <input type="radio" name="compliment" value="nice">nice<br>
          <input type="radio" name="compliment" value="cool">cool<br>
          <input type="radio" name="compliment" value="chill">chill<br>
        </form>
      </body>
    </html>
    """

@app.route('/diss')
def say_diss():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/diss">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit">

          <br>
          <br>Select a compliment from menu<br> 
          <input type="radio" name="compliment" value="nice">nice<br>
          <input type="radio" name="compliment" value="cool">cool<br>
          <input type="radio" name="compliment" value="chill">chill<br>
        </form>
      </body>
    </html>
    """    


@app.route('/greet')
def greet_person():
    """Get user by name."""

    # player = request.args.get("person")
    player = request.args.get("person")

    # compliment = choice(AWESOMENESS)
    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
