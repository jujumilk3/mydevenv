from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


fix_test_dict = {}
fix_test_list = []
fix_test_tuple = ()
fix_test_set = set()
fix_test_dict["test"] = "test"
y = {
    "a": 1,
    "b": 2,
}
test = {a: b for a, b in y}
test2 = "{}" "{}".format(1, 2)
