class Decision:
    def __init__(self, action, model):
        self.action = action
        self.model = model


class Engine:
    def evaluate(self, task):
        t = task.lower()

        if "api" in t or "delete" in t:
            return Decision("block", None)

        if "forgot" in t or "context" in t:
            return Decision("hold", "standard")

        return Decision("commit", "mini")
