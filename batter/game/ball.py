from game.actor import Actor
from game.point import Point
from game import constants

class Ball():
    def __init__(self):
        self._balls = []

    def set_ball(self):
        ball = Actor()
        position = Point(constants.BALL_X, constants.BALL_Y)
        velocity = Point(constants.BALL_DX, constants.BALL_DY)
        ball.set_position(position)
        ball.set_velocity(velocity)
        ball.set_width(constants.BALL_WIDTH)
        ball.set_height(constants.BALL_HEIGHT)
        ball.set_image(constants.IMAGE_BALL)
        self._balls.append(ball)

    def get_ball(self):
        return self._balls