"""
manage.py
this is the main file to run the project

use python manage.py command_name --parameters
"""

import os
from app.main import create_app
from app.main.util import log

app = create_app(os.getenv("BOILERPLATE_ENV") or "dev")


@app.cli.command("migrate")
def migrate():
    """
    run this command to store all cards information to database table
    :return:
    """
    log.info("this function is used to run function to add all information to mongo database")


@app.cli.command("drawcards")
@app.click.option("--cards", "-c", default=12, help="Number of cards to draw")
def draw_cards(cards):
    """
    draw 12 cards print them in proper format
    :return:
     Card 1 - blue 3 fill oval - 00 10 01 11
     Card 21 - blue 3 fill oval - 00 10 01 11
     Card 42 - blue 3 fill oval - 00 10 01 11
    """
    log.info("this function is used to draw cards  and print them to user in proper format")


@app.cli.command("checkcards")
@app.click.option("--cards", "-c", multiple=True, help="Provide 3 cards to check if they are valid or not")
def check_cards(cards):
    """
    you can use this function like following
    python manage.py checkcards -c 12 -c 13 -c 15
    :param cards: list[int]
    :return: True/False
    """
    log.info("this function is used to draw cards  and print them to user in proper format")
