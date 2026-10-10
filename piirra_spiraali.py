from turtle import *

def piirra_spiraali(vari, kaarilkm, alkusade, sadekasvu, paksuus=1):
    color(vari)
    if paksuus == 1:
        pensize(1)
    else:
        pensize(paksuus)

    while kaarilkm > 0:
        down()
        circle(alkusade, 90)
        kaarilkm = kaarilkm - 1
        alkusade = alkusade + sadekasvu

    up()
        


piirra_spiraali("black", 20, 10, 3)
piirra_spiraali("red", 10, 20, 4, 3)
piirra_spiraali("blue", 10, -20, -4, 3)
done()