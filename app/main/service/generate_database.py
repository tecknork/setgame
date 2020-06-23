import os
import enum
from app.main.model.card import Card

colors = { 
   "purple" : "0",
   "green" : "1",
   "red"  : "2"
}

count = {
    "1" : "0",
    "2" : "1",
    "3" : "2"
 }

shapes = {
    "diamond" : "0",
    "squiggle" : "1",
    "Oval" : "2"
 }


fill = {
    "outline" : "0",
    "Filled" : "1",
    "filled" : "1",
    "stripes" : "2"
 }
def save_to_database():
    dictin = os.listdir("/home/empteck/setgame/images")
    for filename in dictin:
        filedetails = filename.split("_")
        if len(filedetails) != 1:
            variable += 1
            file_sub_detail = filedetails[3]
            shapenumber_filetype = file_sub_detail.split(".")
            number_of_shapes = shapenumber_filetype[0]
            num_of_shape = str(number_of_shapes)
            bit_details="{0}{1}{2}{3}".format(colors[color],fill[fill_type],shapes[shape],count[num_of_shape])
            sample_card = Card(color=filedetails[1], card_id=variable,shape=filedetails[0], number_of_shapes=num_of_shape,fill_type=filedetails[2],bitlist = bit_details)
            sample_card.save()
            

    """
    from the images folder iterate over all files and save them all to database
    :return:
    """
    