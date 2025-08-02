import sys, pandas as pd
from dotenv import load_dotenv

from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from model.models import *
from prompt.prompt_library import PROMPT_REGISTRY
from utils.model_loader import ModelLoader

from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import OutputFixingParser

class DocumentCompareLLM:
    def __init__(self):
        pass

    def compare_documents(self):
        pass

    def _format_response(self):
        pass