from tkinter import W
from urllib import response
import aiohttp
import settings

from errors import DataNotRecieved

class TestClass():
    URL = settings.URL
    errors = {
        DataNotRecieved: ("Data not recieved", "data_not_recieved")
    }

    @classmethod
    async def get_data(cls):
        async with aiohttp.ClientSession(raise_for_status=False) as session:
            async with session.get(cls.URL) as request:
                return await request.json()




    @classmethod
    def get_url(cls):
        return cls.URL

    @classmethod
    def _generate_signature(cls):
        pass

