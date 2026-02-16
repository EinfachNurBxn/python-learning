from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
player = FirstPersonController()
Sky()

boxes = []
for i in range(20):
  for j in range(20):
    box = Button(color=color.white, model='cube', position=(j,0,i),
          texture='grass.png', parent=scene, origin_y=0.5)
    boxes.append(box)

noclip_enabled = False

def update():
  if noclip_enabled:
    if held_keys['space']:
      player.position += Vec3(0, 0.05, 0)
    if held_keys['shift']:
      player.position += Vec3(0, -0.05, 0)

def input(key):
  global noclip_enabled
  if key == 'n':
    noclip_enabled = not noclip_enabled
    if noclip_enabled:
      player.gravity = 0
      print("Noclip aktiviert")
    else:
      player.gravity = 1
      print("Noclip deaktiviert")
  
  if noclip_enabled:
    if key == 'space':
      player.position += Vec3(0, 0.1, 0)
    if key == 'shift':
      player.position += Vec3(0, -0.1, 0)
  
  for box in boxes[:]:
    if box.hovered:
      if key == 'left mouse down':
        new = Button(color=color.white, model='cube', position=box.position + mouse.normal,
                    texture='grass.png', parent=scene, origin_y=0.5)
        boxes.append(new)
      if key == 'right mouse down':
        dist = distance(player.position, box.position)
        if dist <= 5:
          boxes.remove(box)
          destroy(box)
app.run()