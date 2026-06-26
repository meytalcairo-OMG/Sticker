from core.base_agent import BaseAgent
from agents.content_agent import ContentAgent
from agents.visual_agent import VisualAgent


class OrchestratorAgent(BaseAgent):
    def __init__(self):
        super().__init__("OrchestratorAgent")
        self.content_agent = ContentAgent()
        self.visual_agent = VisualAgent()

    def route_request(self, request):
        # TODO: לוגיקת ניתוב ספציפית לפי סוג הבקשה — יתווסף בהמשך
        self.log(f"routing request: {request}")

    def run(self, request):
        self.log(f"received request from client: {request}")
        self.route_request(request)
        self.log("routing complete")
