# Cloud Computing Car API

This is a simple API for inserting and retrieving car details with their features. The API is built using Flask, and it communicates with a MongoDB instance to store and fetch the data.

## API Overview

1. Insert a new car into the database.
2. Retrieve a car by its make.

## Requirements
- Flask
- mongoengine
- flask_cors

## Setting Up and Running Locally

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the API**:
   ```bash
   python docker_app.py
   ```

## API Endpoints

### Insert Car

**Endpoint**: `/insert_car`

**Method**: `POST`

**Payload**:

```json
{
    "make": "<car_make>",
    "model": "<car_model>",
    "year": "<manufacturing_year>",
    "features": [
        {
            "featureName": "<feature_name_1>",
            "featureType": "<feature_type_1>"
        },
        {
            "featureName": "<feature_name_2>",
            "featureType": "<feature_type_2>"
        }
    ]
}
```

### Retrieve Car

**Endpoint**: `/get_car?make=<car_make>`

**Method**: `GET`

## Docker Deployment

The provided Dockerfile allows you to easily containerize and run the application. 

1. **Build the Docker Image**:
   ```bash
   docker build -t carapi:latest .
   ```

2. **Run the Docker Container**:
   ```bash
   docker run -p 5001:5001 carapi:latest
   ```

Upon successful deployment, the API will be accessible on `http://localhost:5001`.

## Contributions
Nishan Ali
ROLL - M22AIE208

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

Feel free to modify and adapt this README according to the additional specifics of your project!
