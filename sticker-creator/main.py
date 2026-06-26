import logging

from agents.orchestrator_agent import OrchestratorAgent

logging.basicConfig(level=logging.INFO)


def main():
    orchestrator = OrchestratorAgent()
    example_request = {"type": "create_sticker", "payload": {"text": "כל הכבוד!"}}
    orchestrator.run(example_request)


if __name__ == "__main__":
    main()
