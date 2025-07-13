from fastapi import FastAPI
app = FastAPI()

@app.get('/test_page')
def display_message():
    return {
        'message': "FastAPI is working well now!"
    }