from fastapi import FastAPI

app = FastAPI()

items = []

@app.get("/")
def read_root():
    return{'Hello':'World'}


@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items


