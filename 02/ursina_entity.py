from ursina import *

app = Ursina()

cube_color = color.red
cube_size = 2

my_cube = Entity(
    model='cube',
    color=cube_color,
    scale=cube_size,
    position=(0, 0, 0)
)

my_sphere = Entity(
    model='sphere',
    position=(0, 2, 0)
)

EditorCamera()

app.run()
