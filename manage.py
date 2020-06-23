"""
manage.py
this is the main file to run the project

use python manage.py command_name --parameters
"""

import os
import click
from flask_cli import FlaskCLI
from app.main import create_app
from app.main.service.generate_database import save_to_database
from app.main.model.deck import Deck
from typing import List
import logging

app = create_app(os.getenv("BOILERPLATE_ENV") or "dev")
FlaskCLI(app)


@app.cli.command("migrate")
def migrate():
    """
    run this command to store all cards information to database table
    :return:
    """
    save_to_database()
    logging.info("this function is used to run function to add all information to mongo database")


@app.cli.command("drawcards")
@click.option("--cards", "-c", default=12, help="Number of cards to draw")
def draw_cards(cards):
    """
    draw 12 cards print them in proper format
    :return:
     Card 1 - blue 3 fill oval - 00 10 01 11
     Card 21 - blue 3 fill oval - 00 10 01 11
     Card 42 - blue 3 fill oval - 00 10 01 11
    """
    deck = Deck(cards)
    deck.print_deck()
    logging.info("this function is used to draw cards  and print them to user in proper format")


@app.cli.command("checkcards")
@click.option("--cards", "-c", multiple=True, help="Provide 3 cards to check if they are valid or not")
def check_cards(cards: List[int]):
    """
    you can use this function like following
    python manage.py checkcards -c 12 -c 13 -c 15
    :param cards: list[int]
    :return: True/False
    """
    deck = Deck()
    deck.check_card(cards)
    logging.info("this function is used to draw cards  and print them to user in proper format")


if __name__ == "__main__":
    app.run()
