import aiofiles
import os
from aiocsv import AsyncReader
import pandas as pd

async def read_csv(file:str):
    try:
        data_list = []
        count :int = 0
        async with aiofiles.open(os.path.join(os.path.dirname(__file__), file), "r", encoding="utf-8", newline="") as csv_file:
            async for row in AsyncReader(csv_file):               
                if count == 0:
                    obj_properties = row
                else:
                    data_dist = ({key: value for key, value in zip(obj_properties, row)})
                    data_list.append(data_dist)
                count = count+1
            return data_list

    except FileNotFoundError as csv_not_found:
        return None
