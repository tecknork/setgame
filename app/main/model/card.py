from mongoengine import Document, IntField, StringField


class Card(Document):
    """
    Add All Fields here
    """

    id = IntField(required=True)
    color = StringField(required=True)
    number_of_shapes = StringField(required=True)


# class Card:
#
#     def __init__(self, _id:int, color:str, shape:str, fill_type:str, number_of_shapes:int, bits:str):
#         self._id = _id
#         self.color = color
#         self.shape = shape
#         self.fill_type = fill_type
#         self.number_of_shapes = number_of_shapes
#         self.bits = bits
