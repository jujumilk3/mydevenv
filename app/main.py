from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


fix_test_dict = dict(())
fix_test_list = list(())
fix_test_tuple = tuple(())
fix_test_set = set()
y = {
    "a": 1,
    "b": 2,
}
test = {a: b for a, b in y}
test2 = "{}" "{}".format(1, 2)
