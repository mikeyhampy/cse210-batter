from game.actor import Actor
from game.point import Point
from game import constants

class Brick():
    def __init__(self):
        self._bricks = []

    def set_bricks(self):
        """
        Method will set all the BRICK actors and will save them in a list
        """

        loop_x = 14
        loop_y = 7
        brick_x = 30
        brick_y = 10
        for y in range(loop_y):
            brick_x = 30
            for x in range(loop_x):
                if (y != 6 or (x > 3 and x < 10)):
                    brick = Actor()
                    position = Point(brick_x, brick_y)
                    brick.set_position(position)
                    brick.set_width(constants.BRICK_WIDTH)
                    brick.set_height(constants.BRICK_HEIGHT)
                    brick.set_image(constants.IMAGE_BRICK)
                    self._bricks.append(brick)
                brick_x += constants.BRICK_WIDTH + constants.BRICK_SPACE
                
            brick_y += constants.BRICK_HEIGHT + constants.BRICK_SPACE

    def get_bricks(self):
        """
        Method will get all the BRICK actors and return them as a string
        """

        return self._bricks

    def get_x_y_pos(self):
        for brick in self._bricks:
            x = brick._position.get_x()
            y = brick._position.get_y()
            print(f" {x} {y}")