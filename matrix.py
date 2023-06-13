import time
import fliclib
from api_calls import *
from matrixbase import MatrixBase
from rgbmatrix import graphics
from game import PingPongGame

# Matrix Color Values
fillColor = graphics.Color(255, 255, 255)
fill_r = 255
fill_g = 255
fill_b = 255
player1Color =  graphics.Color(255, 255, 255)
player2Color =  graphics.Color(2,160,165)


class RunText(MatrixBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)

    def run(self):
        
        # Setup Font and Colors for Matrix
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("fonts/clR6x12.bdf")
        textFont = graphics.Font()
        textFont.LoadFont("fonts/4x6.bdf")
        textColor = graphics.Color(255, 255, 255)
        
        # Create Game Object
        game = PingPongGame()
        # Get initial game info from server
        game = get_game_info()

        largeNumberOffest = 4

        pos1_x = 14
        pos1_x_offset = pos1_x - largeNumberOffest
        pos2_x = 14
        pos2_x_offset = pos2_x - largeNumberOffest

        pos1_y = 24
        pos2_y = 58

        servePosition_x = 15
        servePosition_y = 35

        graphics.DrawText(offscreen_canvas, font, pos1_x, pos1_y, textColor, str(game.player1Score))
        graphics.DrawText(offscreen_canvas, font, pos2_x, pos2_y, textColor, str(game.player2Score))

        scoreRefreshInteration = 0

        while True:
            offscreen_canvas.Clear()

            # Update score every half second
            if scoreRefreshInteration % 5 == 0:
                game = get_game_info()

                if game.servingPlayer == "1":
                    fillColor = player1Color
                    fill_r = 255
                    fill_g = 255
                    fill_b = 255
                else:
                    fillColor = player2Color
                    fill_r = 2
                    fill_g = 160
                    fill_b = 165

            if game.player1Score <= 9:
                graphics.DrawText(offscreen_canvas, font, pos1_x, pos1_y, textColor, str(game.player1Score))
            else:
                graphics.DrawText(offscreen_canvas, font, pos1_x_offset, pos1_y, textColor, str(game.player1Score))

            if game.player2Score <= 9:
                graphics.DrawText(offscreen_canvas, font, pos2_x, pos2_y, player2Color, str(game.player2Score))
            else:
                graphics.DrawText(offscreen_canvas, font, pos2_x_offset, pos2_y, player2Color, str(game.player2Score))


            graphics.DrawText(offscreen_canvas, textFont, 13, 11, textColor, "P1")
            graphics.DrawText(offscreen_canvas, textFont, 13, 45, player2Color, "P2")

            # Server Arrow
            graphics.DrawText(offscreen_canvas, textFont, servePosition_x, servePosition_y, fillColor, "|")


            # Inner Fill
            for x in range(0, offscreen_canvas.width):
                offscreen_canvas.SetPixel(x, 0, fill_r, fill_g, fill_b)
                offscreen_canvas.SetPixel(x, offscreen_canvas.height - 1, fill_r, fill_g, fill_b)

            for y in range(0, offscreen_canvas.height):
                offscreen_canvas.SetPixel(0, y, fill_r, fill_g, fill_b)
                offscreen_canvas.SetPixel(offscreen_canvas.width - 1, y, fill_r, fill_g, fill_b)

            for x in range(1, offscreen_canvas.width - 1):
                offscreen_canvas.SetPixel(x, 1, fill_r, fill_g, fill_b)
                offscreen_canvas.SetPixel(x, offscreen_canvas.height - 2, fill_r, fill_g, fill_b)

            for y in range(1, offscreen_canvas.height -1):
                offscreen_canvas.SetPixel(1, y, fill_r, fill_g, fill_b)
                offscreen_canvas.SetPixel(2, y, fill_r, fill_g, fill_b)
                offscreen_canvas.SetPixel(offscreen_canvas.width - 2, y, fill_r, fill_g, fill_b)
                offscreen_canvas.SetPixel(offscreen_canvas.width - 3, y, fill_r, fill_g, fill_b)

            scoreRefreshInteration += 1  # increment the counter at the end of the loop

            time.sleep(0.1)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


def run():
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()

run()