from flask import Flask, request, jsonify
from mongoengine import connect, ValidationError
from flask_cors import CORS

from mongoengine import Document, EmbeddedDocument, connect
from mongoengine.fields import StringField, IntField, ListField, EmbeddedDocumentField


connect(db="cloud_computing_assignment_db", host="3.109.202.37", port = 27017)

app = Flask(__name__)
CORS(app)

class CarFeatures(EmbeddedDocument):
    featureName = StringField(required=True)
    featureType = StringField(required=True)

class Car(Document):
    make = StringField(required=True)
    model = StringField(required=True)
    year = StringField(required=True)
    features = ListField(EmbeddedDocumentField(CarFeatures))





app = Flask(__name__)
CORS(app)


@app.route('/insert_car', methods=['POST'])
def insert_car():
    data = request.get_json()
    
    car_features = [CarFeatures(featureName=feature['featureName'], featureType=feature['featureType']) for feature in data.get('features', [])]
    
    car = Car(
        make=data['make'],
        model=data['model'],
        year=data['year'],
        features=car_features
    )
    
    car.save()
    return jsonify({'message': 'Car saved successfully!'}), 201

@app.route('/get_car', methods=['GET'])
def get_car():
    make = request.args.get('make')
    
    car = Car.objects(make=make).first()
    if car:
        car_data = {
            "make": car.make,
            "model": car.model,
            "year": car.year,
            "features": [{"featureName": feature.featureName, "featureType": feature.featureType} for feature in car.features]
        }
        return jsonify(car_data)
    return jsonify({'error': 'Car not found'}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
