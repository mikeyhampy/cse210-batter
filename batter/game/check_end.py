import raylibpy
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
        self._sound = raylibpy

    def execute(self, cast):
        balls = cast["balls"]
        ball = balls[0]
        y = ball._position.get_y()
        bricks = cast["bricks"]

        if y > constants.MAX_Y:
            balls.remove(ball)
            self._audio_service.play_sound(constants.SOUND_OVER)
            self._end_game = True
            self._game_message = "GAME OVER!"
            self._sound = constants.SOUND_OVER
            self._audio_service.stop_audio(constants.SOUND_START)
        elif len(bricks) == 0:
            self._audio_service.play_sound(constants.SOUND_VICTORY)
            self._end_game = True
            self._game_message = "YOU WIN!"
            self._sound = constants.SOUND_VICTORY
            self._audio_service.stop_audio(constants.SOUND_START)
        else:
            self._sound = constants.SOUND_START