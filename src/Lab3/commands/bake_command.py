from Lab3.commands.command import Command

class BakeCommand(Command):
    def __init__(self, oven, pizza_name):
        self.oven = oven
        self.pizza_name = pizza_name

    def execute(self):
        self.oven.start_baking(self.pizza_name)
