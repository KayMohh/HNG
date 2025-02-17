from typing import Union

from fastapi import FastAPI
from datetime import datetime
from typing import Optional



app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get('/hng')
def get_data():
    email = 'thrilltim@gmail.com'
    current_datetime =  datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    github_repo_url = "https://github.com/kaymohh/HNG"

    current_day = datetime.now().strftime("%A")

    return {
        'email' : email,
        'current_datetime' : current_datetime,
        'github_repo_url' : github_repo_url,
        "status_code": 200,

    }



@app.get('/ol')
def get_data(slack_name: Optional[str] = None, track: Optional[str] = None):
    if slack_name is None or track is None:
        return {"error": "Both slack_name and track parameters are required"}
    
    # Get the current day of the week in full
    current_day = datetime.now().strftime("%A")
    
    # Get the current UTC time with a +/-2 minute window
    current_utc_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    
    # GitHub repository information
    github_repo_url = "https://github.com/franciedigital/HNG"
    github_file_url = "https://github.com/franciedigital/HNG/blob/master/main.py"
    
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200,
    }
    
    return response_data