import os
os.environ['RAYLIB_BIN_PATH'] = r'../cse210-batter/batter'

import random
import raylibpy
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService

# TODO: Add imports similar to the following when you create these classes
from game.brick import Brick
from game.ball import Ball
from game.paddle import Paddle
from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.handle_off_screen_action import HandleOffScreenAction
from game.move_actors_action import MoveActorsAction
from game.check_end import CheckEnd
from game.end_game import EndGame

def main():
    open_window_loop = 0
    while(constants.KEEP_PLAYING):
        constants.KEEP_PLAYING = False
        """
        Set up game
        """
        # create the cast {key: tag, value: list}
        cast = {}

        cast["bricks"] = []
        # TODO: Create bricks here and add them to the list
        brick = Brick()
        brick.set_bricks()
        cast["bricks"] = brick.get_bricks()
        
        cast["balls"] = []
        # TODO: Create a ball here and add it to the list
        ball = Ball()
        ball.set_ball()
        cast["balls"] = ball.get_ball()

        cast["paddle"] = []
        # TODO: Create a paddle here and add it to the list
        paddle = Paddle()
        paddle.set_paddle()
        cast["paddle"] = paddle.get_paddle()

        cast["end_game"] = []
        end_game = EndGame()
        end_game.set_end_game()
        cast["end_game"] = end_game.get_end_game()


        # Create the script {key: tag, value: list}
        script = {}

        input_service = InputService()
        output_service = OutputService()
        physics_service = PhysicsService()
        audio_service = AudioService()

        move_actors_action = MoveActorsAction()
        handle_off_screen_action = HandleOffScreenAction()
        control_actors_action = ControlActorsAction(input_service)
        draw_actors_action = DrawActorsAction(output_service)
        handle_collisions_action = HandleCollisionsAction(physics_service, audio_service)
        check_end = CheckEnd(audio_service)

        # TODO: Create additional actions here and add them to the script

        script["input"] = [control_actors_action]
        script["update"] = [move_actors_action, handle_off_screen_action, handle_collisions_action]
        script["output"] = [check_end, draw_actors_action]



        # Start the game run once
        if open_window_loop == 0:
            output_service.open_window("Batter")
            audio_service.start_audio()
            open_window_loop = 1
        
        """
        Play game
        """
        audio_service.play_sound(constants.SOUND_START)
        director = Director(cast, script)
        director.start_game()
        audio_service.stop_audio(check_end._sound)
        if constants.KEEP_PLAYING:
            output_service.flush_buffer()

    #close game run once
    if handle_collisions_action.num_brick_col > 0:
        audio_service.stop_audio(constants.SOUND_BOUNCE)
    if handle_collisions_action.num_paddle_col > 0:
        audio_service.stop_audio(constants.SOUND_BOUNCE)
    audio_service.close_audio()

    output_service.flush_buffer()
    raylibpy.close_window()

if __name__ == "__main__":
    main()
