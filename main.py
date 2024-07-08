from fastapi import FastAPI  # Import the FastAPI class from the fastapi package

# Create an instance of the FastAPI class
app = FastAPI()

# Define the root endpoint ("/") with a GET method
@app.get("/")
async def read_root():
    """
    This function handles GET requests to the root endpoint.
    It returns a JSON response with a welcome message.
    """
    return {"message": "Hello, World! This is FastAPI testing"}

# Define the /items/{item_id} endpoint with a GET method
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    """
    This function handles GET requests to the /items/{item_id} endpoint.
    It takes an item_id as a path parameter and an optional query parameter q.
    It returns a JSON response with the item_id and the query parameter value.
    """
    return {"item_id": item_id, "q": q}
