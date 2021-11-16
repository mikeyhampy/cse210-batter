from game import constants
from game.action import Action

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self, physics_service, audio_service):
        super().__init__()
        self._physics_service = physics_service
        self._audio_service = audio_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["balls"][0]
        paddle = cast["paddle"][0]
        bricks = cast["bricks"]
        if self._physics_service.is_collision(ball, paddle):
            self._audio_service.play_sound(constants.SOUND_BOUNCE)
            ball._velocity._y = ball._velocity._y * -1

        for brick in bricks:
            if self._physics_service.is_collision(ball, brick):
                self._audio_service.play_sound(constants.SOUND_BOUNCE)
                ball._velocity._y = ball._velocity._y * -1
                bricks.remove(brick)