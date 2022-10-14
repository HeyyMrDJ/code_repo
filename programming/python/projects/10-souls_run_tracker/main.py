"""This module tracks Soul game runs"""
import json
import os

class SoulsRun:
    """A class for tracking Soulsborne runs"""
    def __init__(self, name, game, length, run_type, notes):
        self.name = name
        self.game = game
        self.length = length
        self.run_type = run_type
        self.notes = notes
    def show_run(self):
        '''Show current run'''
        return print(
            f"""
            Game: {self.game}
            Length: {self.length}
            Type: {self.run_type}
            Notes: \"{self.notes}\"
            """
            )
    def save_run(self):
        """Saves run information"""
        run_info = [self.name, self.game, self.length, self.run_type]
        dirpath = os.path.dirname(__file__)
        filename = os.path.join(dirpath,'runs.json')
        with open(filename, 'a',encoding="utf8") as file:
            json.dump(run_info, file)
            file.write('\n')
    def show_runs(self):
        '''Show list of runs'''
        dirpath = os.path.dirname(__file__)
        filename = os.path.join(dirpath, 'runs.json')
        # pylint: disable=redefined-outer-name
        run_list = []
        with open(filename, 'r',encoding="utf8") as runs:
            run_list.append(json.load(runs))
        print(run_list)

run_list = []

souls1 = SoulsRun('Run1', 'Bloodborne', 2.24, "Speedrun", "Shadows gave me a hard time")
souls2 = SoulsRun('Run2', 'Bloodborne', 2.24, "Speedrun", "Shadows gave me a hard time")
run_list.append(souls1)
run_list.append(souls2)
print(run_list)
souls1.show_runs()
