"""
Arcade example testing. BREAK IT THEN FIX IT. UNDERSTAND IT. 
"""

import arcade

#constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

#Constants used to scale our sprites from their original size
CHARACTER_SCALING = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5

#Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 20
GRAVITY = .3
PLAYER_JUMP_SPEED = 100

#How many pixels to keep as a minimum margin between the character and the edge of the screen
LEFT_VIEWPORT_MARGIN = 250
RIGHT_VIEWPORT_MARGIN = 250
BOTTOM_VIEWPORT_MARGIN = 50
TOP_VIEWPORT_MARGIN = 100

class MyGame(arcade.Window):
  """
  Main application class.
  """

  def __init__(self):

    #call the parent class and set up the window
    super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)

    self.coin_list = None
    self.wall_list = None
    self.player_list = None
    self.star_list = None

    #variable to hold player sprite
    self.player_sprite = None

    #variable to hold physics engine
    self.physics_engine = None

    #used to keep track of our scrolling
    self.view_bottom = 0
    self.view_left = 0

    #Load Sounds
    self.collect_coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
    self.collect_star_sound = arcade.load_sound(":resources:sounds/coin3.wav")
    self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")

    #keep track of score
    self.score = 0
    arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
    """
    Note about __init__ : init only sets up the variables, but doesn't create any class instances.
    They just deault to 0 or None. The setup method actually creates the object instances, such as graphical sprites.
    Theres a reason they are split into two.  With a setup method split out, later we can easily
    add 'restart/play again' features.  A simple call to setup will reset everything. 
    We can also add additional levels and have setup_level_1 and setup_level_2 etc. 

    """

    
  def setup(self):
    """
    Set up the game here.  Call this function to restart the game.
    """
    #create sprite lists
    self.player_list = arcade.SpriteList()
    self.wall_list = arcade.SpriteList()
    self.coin_list = arcade.SpriteList()
    self.star_list = arcade.SpriteList()
    self.coin_list = arcade.SpriteList()
    
    #keep track of score
    self.score = 0


    #Set up the player, specifically placing it at the coordinates.
    image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
    self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
    self.player_sprite.center_x = 64
    self.player_sprite.center_y = 124
    self.player_list.append(self.player_sprite)

    #Create the ground
    #this shows using a loop to place multiple sprites horizontally
    for x in range(0, 1250,64):
        wall = arcade.Sprite(":resources:/images/tiles/grassMid.png", TILE_SCALING)
        wall.center_x = x
        wall.center_y = 32
        self.wall_list.append(wall)

    #put some crates on the ground
    #This shows using a coordinate list to place sprites
    coordinate_list = [
        [512,96],
        [256,96],
        [768,96]
    ]
    for coordinate in coordinate_list:
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", TILE_SCALING)
        wall.position = coordinate
        self.wall_list.append(wall)

    for x in range(128,1250,256):
      coin = arcade.Sprite(":resources:/images/items/coinGold.png", COIN_SCALING)
      coin.center_x = x
      coin.center_y = 96
      self.coin_list.append(coin)

    #trying to add a star somewhere
    star_coordinate_list = [
        [512,242],
        [768,272],
    ]
    for coordinate in star_coordinate_list:
      star = arcade.Sprite(":resources:images/items/star.png", TILE_SCALING)
      star.position = coordinate
      self.star_list.append(star)
    
    #Create the 'physics engine'
    self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list, GRAVITY)


  def on_draw(self):
    """render the screen"""

    #Clear the screen to the background color
    arcade.start_render()

    #Draw our sprites
    self.wall_list.draw()
    self.coin_list.draw()
    self.player_list.draw()
    self.star_list.draw()

    #draw our score on the screen, scrolling it with the viewport
    score_text = f"Score: {self.score}"
    arcade.draw_text(score_text, 10 +self.view_left, 10 +self.view_bottom, arcade.csscolor.WHITE, 18)


  def on_key_press(self, key, modifiers):
    """Called whenever a key is pressed. """
    if key == arcade.key.UP or key == arcade.key.W:
      if self.physics_engine.can_jump():
        self.player_sprite.change_y = PLAYER_JUMP_SPEED
    # elif key ==arcade.key.DOWN or key == arcade.key.S:
    #   self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
    elif key ==arcade.key.LEFT or key == arcade.key.A:
      self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
    elif key ==arcade.key.RIGHT or key == arcade.key.D:
      self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
  
  def on_key_release(self, key, modifiers):
    """Called when the user releases a key. """
    # if key == arcade.key.UP or key == arcade.key.W:
    #   self.player_sprite.change_y = 0
    # elif key ==arcade.key.DOWN or key == arcade.key.S:
    #   self.player_sprite.change_y = 0
    if key ==arcade.key.LEFT or key == arcade.key.A:
      self.player_sprite.change_x = 0
    elif key ==arcade.key.RIGHT or key == arcade.key.D:
      self.player_sprite.change_x = 0

  def on_update(self, delta_time):
    """movement and game logic """
    #move the player with the physics engine
    self.physics_engine.update()

    #See if we hit any coins
    coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
    star_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.star_list)

    #loop through each coin we hit (if any) and remove it
    for coin in coin_hit_list:
      #remove the coin
      coin.remove_from_sprite_lists()
      #play a sound
      arcade.play_sound(self.collect_coin_sound)
      #add one to the score
      self.score +=1
    
    for star in star_hit_list:
      #remove the coin
      star.remove_from_sprite_lists()
      #play a sound
      arcade.play_sound(self.collect_star_sound)
      #add one to the score
      self.score += 10

    #----MANAGE SCROLLING----

    #track if we need to change the viewport

    changed = False

    #Scroll left
    left_boundary = self.view_left + LEFT_VIEWPORT_MARGIN
    if self.player_sprite.left < left_boundary:
      self.view_left -= left_boundary - self.player_sprite.left
      changed = True

    #Scroll right
    right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN
    if self.player_sprite.right > right_boundary:
      self.view_left += self.player_sprite.right - right_boundary
      changed = True

    #Scroll Up
    top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
    if self.player_sprite.top > top_boundary:
      self.view_bottom += self.player_sprite.top - top_boundary
      changed = True

    #Scroll down

    bottom_boundary = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
    if self.player_sprite.bottom < bottom_boundary:
      self.view_bottom -= bottom_boundary - self.player_sprite.bottom
      changed = True

    if changed:
      #only scroll to integers. Otherwise we end up with pixels that don't line up on the screen
      self.view_bottom = int(self.view_bottom)
      self.view_left = int(self.view_left)

      #Do the scrolling
      arcade.set_viewport(self.view_left,SCREEN_WIDTH + self.view_left, self.view_bottom, SCREEN_HEIGHT + self.view_bottom)
def main():
    """main method"""
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()