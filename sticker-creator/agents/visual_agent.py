from core.base_agent import BaseAgent


class VisualAgent(BaseAgent):
    def __init__(self):
        super().__init__("VisualAgent")

    def handle_visuals(self, request):
        # TODO: יצירה וניהול תמונות גרפיות למדבקות — יתווסף בהמשך
        self.log(f"handle_visuals stub called with request: {request}")

    def run(self, request):
        self.log(f"received request from OrchestratorAgent: {request}")
        self.handle_visuals(request)
        self.log("reporting back to OrchestratorAgent: visuals stub done")
