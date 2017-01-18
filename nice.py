from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html><a href='/hello'>Hi! This is the home page.</a><html>"


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
          <label>What's your name? <input type="text" name="person"></label>
          <select name="compliment">
            <option value='awesome'>Awesome</option>
            <option value='terrific'>Terrific</option>
            <option value='neato'>Neato</option>
            <option value='coolio'>Coolio</option>
            <option value='ducky'>Ducky</option>
          </select>
          <input type="submit">
        </form>
        <br>
        <br>
        <form action="/diss">
          <label>What's your name? <input type="text" name="person"></label>
          Diss:
            <select name="diss">
              <option value='dumb'>Dumb</option>
              <option value='smelly'>Smelly</option>
              <option value='unmotivated'>Unmotivated</option>
              <option value='unthinking'>Unthinking</option>
              <option value='not-funny'>Not Funny</option>
            </select>
          Height:
            <input type="radio" name="height" value="5'5&quot;under">5"5' or under
            <input type="radio" name="height" value="5'6&quot;Over">5"6' or over          <input type="submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, compliment)


@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")

    diss = request.args.get("diss")

    height = request.args.get("height")

    if height == "5'5&quot;under":
      height = "hello"


    return """
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi %s I think you're %s!

        %s
      </body>
    </html>
    """ % (player, diss, height)



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
