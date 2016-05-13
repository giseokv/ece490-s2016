##Runs vacuum control commands
from Arduino import Arduino
class vacuum:
    def __init__(self):
        self.board=Arduino('9600');
        self.board.pinMode(13, "OUTPUT")

    def on(self):
        self.board.digitalWrite(13,"HIGH");
    def off(self):
        self.board.digitalWrite(13,"LOW");
        
