from game import constants
from game.action import Action

class HandleOffScreenAction(Action):
    """
    Bounces the ball off the walls
    """

    def execute(self, cast):
        #get ball data
        ball = cast["balls"][0]
        x = ball._position.get_x()
        y = ball._position.get_y()

        #bounces horizontal
        if( x <= 0 or x >= constants.MAX_X - constants.BALL_WIDTH):
            ball._velocity._x = ball._velocity._x * -1

        #bounces vertical
        if(y <= 0):
            ball._velocity._y = ball._velocity._y * -1

        #get paddle data
        paddle = cast["paddle"][0]
        paddle_x = paddle._position.get_x()

        #paddle won't go off screen
        if(paddle_x <= 0):
            paddle._position._x = 0
        if(paddle_x >= constants.MAX_X - constants.PADDLE_WIDTH):
            paddle._position._x = constants.MAX_X - constants.PADDLE_WIDTH
