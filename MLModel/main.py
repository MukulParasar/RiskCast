from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


origins = [
    "http://localhost:5030", # .NET Backend
    "http://localhost:4200", # Angular Frontend
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)


def get_enhanced_geojson_data():
    return {
      "type": "FeatureCollection",
      "features": [
        {
          "type": "Feature",
          "properties": {
            "city": "Dehradun", "area": "Prem Nagar", "risk_score": 51,
            "description": "Moderate flood risk area due to proximity to Asan river.", "risk_category": "Moderate",
            "mitigation_plan_id": "plan_001"
          },
          "geometry": { "type": "Point", "coordinates": [78.0284, 30.3196] }
        },
        {
          "type": "Feature",
          "properties": {
            "city": "Dehradun", "area": "Special Wing, Prem Nagar", "risk_score": 51,
            "description": "Moderate flood risk due to older drainage infrastructure.", "risk_category": "Moderate",
            "mitigation_plan_id": "plan_002"
          },
          "geometry": { "type": "Point", "coordinates": [78.029, 30.3185] }
        },
        {
          "type": "Feature",
          "properties": {
            "city": "Dehradun", "area": "FRI & College Area", "risk_score": 48,
            "description": "Moderate risk from overflowing natural streams on campus.", "risk_category": "Moderate",
            "mitigation_plan_id": "plan_003"
          },
          "geometry": { "type": "Point", "coordinates": [78.0304, 30.3173] }
        },
        {
          "type": "Feature",
          "properties": {
            "city": "Dehradun", "area": "Clement Town", "risk_score": 46,
            "description": "Moderate risk from high-velocity runoff on paved surfaces.", "risk_category": "Moderate",
            "mitigation_plan_id": "plan_004"
          },
          "geometry": { "type": "Point", "coordinates": [78.007, 30.267] }
        },
        {
          "type": "Feature",
          "properties": {
            "city": "Dehradun", "area": "Rajpur Road", "risk_score": 45,
            "description": "Moderate risk from overflowing Rispana river.", "risk_category": "Moderate",
            "mitigation_plan_id": "plan_005"
          },
          "geometry": { "type": "Point", "coordinates": [78.05, 30.35] }
        },
        {
          "type": "Feature",
          "properties": {
            "city": "Dehradun", "area": "Sahastradhara Road", "risk_score": 46,
            "description": "Moderate risk of landslides triggered by waterlogging.", "risk_category": "Moderate",
            "mitigation_plan_id": "plan_006"
          },
          "geometry": { "type": "Point", "coordinates": [78.11, 30.3] }
        },
        {
          "type": "Feature",
          "properties": {
            "city": "Dehradun", "area": "Maldevta", "risk_score": 48,
            "description": "Moderate risk of flash floods from cloudbursts in upper catchment area.", "risk_category": "Moderate",
            "mitigation_plan_id": "plan_007"
          },
          "geometry": { "type": "Point", "coordinates": [78.103986, 30.3199264] }
        },
        {
          "type": "Feature",
          "properties": {
            "city": "Dehrad.un", "area": "Paltan Bazaar", "risk_score": 75,
            "description": "High risk area. Extremely dense, low-lying market with very poor drainage capacity, adjacent to Bindal river.", "risk_category": "High",
            "mitigation_plan_id": "plan_008"
          },
          "geometry": { "type": "Point", "coordinates": [78.035, 30.325] }
        },
        {
          "type": "Feature",
          "properties": {
            "city": "Dehradun", "area": "Vasant Vihar", "risk_score": 35,
            "description": "Low risk area. Well-planned residential area with modern drainage and higher elevation.", "risk_category": "Low",
            "mitigation_plan_id": "plan_009"
          },
          "geometry": { "type": "Point", "coordinates": [78.005, 30.31] }
        },
        {
          "type": "Feature",
          "properties": {
            "city": "Dehradun", "area": "ISBT Area", "risk_score": 55,
            "description": "Moderate risk due to large paved surfaces and proximity to a major canal.", "risk_category": "Moderate",
            "mitigation_plan_id": "plan_010"
          },
          "geometry": { "type": "Point", "coordinates": [77.99, 30.285] }
        },
        {
          "type": "Feature",
          "properties": {
            "city": "Dehradun", "area": "Raipur", "risk_score": 58,
            "description": "Moderate risk. Rapidly developing area where new construction has impacted natural drainage patterns.", "risk_category": "Moderate",
            "mitigation_plan_id": "plan_011"
          },
          "geometry": { "type": "Point", "coordinates": [78.08, 30.3] }
        },
        
        {
          "type": "Feature",
          "properties": {
            "city": "Dehradun", "area": "Karanpur", "risk_score": 68,
            "description": "High risk. Dense commercial and residential area near Rispana river with frequent waterlogging issues.", "risk_category": "High",
            "mitigation_plan_id": "plan_012"
          },
          "geometry": { "type": "Point", "coordinates": [78.045, 30.328] }
        },
        {
          "type": "Feature",
          "properties": {
            "city": "Dehradun", "area": "Ballupur Chowk", "risk_score": 52,
            "description": "Moderate risk. Major traffic intersection prone to severe waterlogging after short, intense rainfall.", "risk_category": "Moderate",
            "mitigation_plan_id": "plan_013"
          },
          "geometry": { "type": "Point", "coordinates": [78.015, 30.335] }
        },
        {
          "type": "Feature",
          "properties": {
            "city": "Dehradun", "area": "Dalanwala", "risk_score": 38,
            "description": "Low risk area. Posh residential area with good green cover and effective, modern drainage systems.", "risk_category": "Low",
            "mitigation_plan_id": "plan_014"
          },
          "geometry": { "type": "Point", "coordinates": [78.048, 30.315] }
        }
      ]
    }


@app.get("/api/risk-data")
def read_risk_data():
    return get_enhanced_geojson_data()

