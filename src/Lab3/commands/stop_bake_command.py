from Lab3.commands.command import Command

class StopBakeCommand(Command):
    def __init__(self, oven):
        self.oven = oven

    def execute(self):
        self.oven.stop_baking()
