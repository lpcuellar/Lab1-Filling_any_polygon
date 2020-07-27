##
##  UNIVERSIDAD DEL VALLE DE GUATEMALA
##  GRÁFICAS POR COMPUTADORA
##  SECCIÓN 20
##
##  SR3: Obj Models
##  LUIS PEDRO CUÉLLAR - 18220
##

from gl import Render, color

filename = "output.bmp"

render = Render(800, 700)

p1 = [(165, 380), (185, 360), (180, 330),
        (207, 345), (233, 330), (230, 360),
        (250, 380), (220, 385), (205, 410),
        (193, 383)]

p2 = [(321, 335), (288, 286), (339, 251),
    (374, 302)]

p3 = [(377, 249), (411, 197), (436, 249)]

p4 = [(413, 177), (448, 159), (502, 88),
    (553, 53), (535, 36), (676, 37),
    (660, 52), (750, 145), (761, 179),
    (672, 192), (659, 214), (615, 214),
    (632, 230), (580, 230), (597, 215),
    (552, 214), (517, 144), (466, 180)]

p5 = [(682, 175), (708, 120), (735, 148),
    (739, 170)]

print("A continuación se graficarán y se llenarán polígonos ")

enter = input("Apache ENTER para continuar...")

##  changes the color to yellow
render.glColor(1, 1, 0)
render.glDrawPolygon(p1)

##  changes the color to blue
render.glColor(0, 0, 1)
render.glDrawPolygon(p2)

##  changes the color to green
render.glColor(0, 1, 0)
render.glDrawPolygon(p3)

##  changes the color to red
render.glColor(1, 0, 0)
render.glDrawPolygon(p4)

##  changes the color to white
render.glColor(1, 1, 1)
render.glDrawPolygon(p5)

render.glFinish(filename)
