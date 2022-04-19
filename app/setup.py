import asyncio

from example import TestClass

if __name__ == "__main__":
   testClass = TestClass()

   classUrl = testClass.get_url()
   response = asyncio.run(testClass.get_data())

   print(classUrl)
   print(response)
