from src.exceptions.no_more_undo_redo import NoMoreUndoException, NoMoreRedoException

class ServicesUndo:
    def __init__(self):
        self.history = []
        self.index = 0

    def record_operation(self, operation):
        if self.index != len(self.history):
            self.history = self.history[:self.index]
        self.history.append(operation)
        self.index = len(self.history)

    def undo(self):
        if self.index == 0:
            raise NoMoreUndoException

        self.index -= 1
        self.history[self.index].undo()

    def redo(self):
        if self.index == len(self.history):
            raise NoMoreRedoException

        self.history[self.index].redo()
        self.index += 1


class FunctionCall:
    def __init__(self, function, *params):
        self.function = function
        self.params = params

    def call(self):
        self.function(*self.params)


class Operation:
    def __init__(self, undo_fc, redo_fc):
        self.undo_fc = undo_fc
        self.redo_fc = redo_fc

    def undo(self):
        self.undo_fc.call()

    def redo(self):
        self.redo_fc.call()


class CascadedOperation:
    def __init__(self,  *operations):
        self.operations = operations

    def undo(self):
        for op in self.operations:
            op.undo()

    def redo(self):
        for op in self.operations:
            op.redo()


