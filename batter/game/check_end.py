from game import constants
from game.action import Action

class CheckEnd(Action):
    """
    Check if the game ends
    """

    def __init__(self, audio_service):
        super().__init__()
        self._audio_service = audio_service
        self._end_game = False
        self._game_message = ""

    def execute(self, cast):
        balls = cast["balls"]
        ball = balls[0]
        y = ball._position.get_y()
        bricks = cast["bricks"]

        if y > constants.MAX_Y:
            balls.remove(ball)
            #ball._position._y = 0 + constants.PADDLE_HEIGHT + 1
            self._audio_service.play_sound(constants.SOUND_OVER)
            self._end_game = True
            self._game_message = "GAME OVER!"
        elif len(bricks) == 0:
            self._audio_service.play_sound(constants.SOUND_VICTORY)
            self._end_game = True
            self._game_message = "YOU WIN!"