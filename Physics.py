import arcade
from arcade.geometry import check_for_collision_with_list

class Physics(arcade.PhysicsEngineSimple):
    """
    This class will move everything, and take care of collisions.
    """

    def __init__(self, player_sprite, walls):
        super().__init__(player_sprite, walls)
        self.collision = None
        self.id_collided_object = None

    def getCollided(self):
        return {
            'collision' : self.collision,
            'student_id' : self.id_collided_object
        }

    def update(self):
        """
        Move everything and resolve collisions.
        """
        # --- Move in the x direction
        self.player_sprite.center_x += self.player_sprite.change_x

        self.collision = ""
        # Check for wall hit
        hit_list = \
            check_for_collision_with_list(self.player_sprite,
                                          self.walls)


        # If we hit a wall, move so the edges are at the same point
        if len(hit_list) > 0:
            self.id_collided_object = hit_list[0]
            self.collision = True
            if self.player_sprite.change_x > 0:
                for item in hit_list:
                    self.player_sprite.right = min(item.left,
                                                   self.player_sprite.right)
            elif self.player_sprite.change_x < 0:
                for item in hit_list:
                    self.player_sprite.left = max(item.right,
                                                  self.player_sprite.left)
            else:
                print("Error, collision while player wasn't moving.")


        # --- Move in the y direction
        self.player_sprite.center_y += self.player_sprite.change_y

        # Check for wall hit
        hit_list = \
            check_for_collision_with_list(self.player_sprite,
                                          self.walls)

        # If we hit a wall, move so the edges are at the same point
        if len(hit_list) > 0:
            self.collision = True
            self.id_collided_object = hit_list[0]
            if self.player_sprite.change_y > 0:
                for item in hit_list:
                    self.player_sprite.top = min(item.bottom,
                                                 self.player_sprite.top)
            elif self.player_sprite.change_y < 0:
                for item in hit_list:
                    self.player_sprite.bottom = max(item.top,
                                                    self.player_sprite.bottom)
            else:
                print("Error, collision while player wasn't moving.")


