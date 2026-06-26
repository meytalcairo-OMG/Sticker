from core.base_agent import BaseAgent


class ContentAgent(BaseAgent):
    def __init__(self):
        super().__init__("ContentAgent")

    def handle_content(self, request):
        # TODO: כתיבת טקסטים ועימוד למדבקות — יתווסף בהמשך
        self.log(f"handle_content stub called with request: {request}")

    def run(self, request):
        self.log(f"received request from OrchestratorAgent: {request}")
        self.handle_content(request)
        self.log("reporting back to OrchestratorAgent: content stub done")
