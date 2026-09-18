from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text:str = None
    is_done: bool = False


Items = []

@app.post('/items')
def addItems(item: Item):
    Items.append(item)
    return Items


@app.get('/items/{itemid}', response_model=Item)
def getItemsById(itemid: int)->Item:
    if itemid < len(Items): 
        return Items[itemid]
    else:
        raise HTTPException(status_code=404, detail= f"Item not found")