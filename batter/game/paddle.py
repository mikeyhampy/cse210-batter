from game.actor import Actor
from game.point import Point
from game import constants

class Paddle():
    def __init__(self):
        self._paddles = []

    def set_paddle(self):
        paddle = Actor()
        position = Point(constants.PADDLE_X, constants.PADDLE_Y)
        paddle.set_position(position)
        paddle.set_width(constants.PADDLE_WIDTH)
        paddle.set_height(constants.PADDLE_HEIGHT)
        paddle.set_image(constants.IMAGE_PADDLE)
        self._paddles.append(paddle)

    def get_paddle(self):
        return self._paddles