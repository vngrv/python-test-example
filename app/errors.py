
from shutil import ExecError
from turtle import st

from typing import Dict

class MainExeption(Exception):
    error_message: str

    def __init__(self, message: Dict[str, str]):
        self.message: Dict[str, str] = message
        super().__init__(self.message)

class DataNotRecieved(MainExeption):
    error_message: str = "Data not recieved"
    code_last_part: str = "DataRevieveError" 
    