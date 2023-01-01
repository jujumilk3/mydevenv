from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


fix_test_dict = dict()
fix_test_list = list()
fix_test_tuple = tuple()
fix_test_set = set()
