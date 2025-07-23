from src.app.ai_engine.core.ai_engine import AIEngine
import logging

def retrieve_resume_data(prompt: str, model_name: str):
    ai_engine = AIEngine()
    response = None
    try:
        response = ai_engine.generate_text(prompt, model_name)
    except Exception as ex:
        logging.error(f"Error generating resume data: {ex}")
    return response