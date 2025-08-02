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
        load_dotenv()
        self.log = CustomLogger().get_logger(__name__)
        self.model_loader = ModelLoader()
        self.llm = self.model_loader.load_llm()
        self.parser = JsonOutputParser(pydantic_object=SummaryResponse)
        self.fixing_parser = OutputFixingParser.from_llm(parser=self.parser, llm=self.llm)
        self.prompt = PROMPT_REGISTRY["document_comparison"]
        self.chain = self.prompt | self.llm | self.parser
        self.log.info("DocumentCompareLLM initialized with model and parser")


    def compare_documents(self, combined_docs:str)-> pd.DataFrame:
        try:
            inputs = {
                "combined_docs": combined_docs,
                "format_instruction": self.parser.get_format_instructions()
            }
            self.log.info("Starting document comparison", inputs=inputs)
            response = self.chain.invoke(inputs)
            self.log.info("Document comparison completed")
            return self._format_response(response)

        except Exception as e:
            self.log.error(f"Error in compare_documents: {e}")
            raise DocumentPortalException("Error while comparing documents", sys)
    

    def _format_response(self, response_parsed:list[dict])-> pd.DataFrame:
        try:
            df = pd.DataFrame(response_parsed)
            self.log.info("Response formatted into dataframe")
            return df
        except Exception as e:
            self.log.error(f"Error formatting response into dataframe: {e}")
            raise DocumentPortalException("Error while formatting response", sys)