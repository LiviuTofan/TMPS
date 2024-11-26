class CommandQueue:
    def __init__(self):
        self.queue = []

    def add_command(self, command):
        self.queue.append(command)

    def execute_commands(self):
        for command in self.queue:
            command.execute()
        self.queue.clear()
