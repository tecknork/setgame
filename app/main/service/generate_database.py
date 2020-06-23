from app.main.model.card import Card


def save_to_database():
    """
    from the images folder iterate over all files and save them all to database
    :return:
    """
    sample_card = Card(color="blue", id=1, number_of_shapes="3")
    sample_card.save()
