using Microsoft.AspNetCore.Mvc;

namespace RiskCastBackend.Controllers
{
    [ApiController]
    [Route("api/simulation")]
    public class SimulationController : ControllerBase
    {
        [HttpGet]
        public IActionResult GetSimulationData()
        {
            
            var geoJsonData = @"{
  ""type"": ""FeatureCollection"",
  ""features"": [
    {
      ""type"": ""Feature"",
      ""properties"": {
        ""name"": ""Dehradun High-Risk Flood Zone"",
        ""risk_score"": 85,
        ""affected_buildings"": [
          ""City Hospital"",
          ""University Campus""
        ],
        ""affected_roads"": [
          ""Rajpur Road"",
          ""Main Street""
        ],
        ""description"": ""Critical flood risk due to extreme rainfall and proximity to a major river, affecting key infrastructure.""
      },
      ""geometry"": {
        ""type"": ""Polygon"",
        ""coordinates"": [
          [
            [78.03, 30.30],
            [78.05, 30.30],
            [78.05, 30.32],
            [78.03, 30.32],
            [78.03, 30.30]
          ]
        ]
      }
    },
    {
      ""type"": ""Feature"",
      ""properties"": {
        ""name"": ""Dehradun Moderate-Risk Flood Zone"",
        ""risk_score"": 45,
        ""affected_buildings"": [
          ""Local Market""
        ],
        ""affected_roads"": [
          ""Canal Road""
        ],
        ""description"": ""Moderate flood risk due to a clogged drainage system. Primarily affects low-lying commercial areas.""
      },
      ""geometry"": {
        ""type"": ""Polygon"",
        ""coordinates"": [
          [
            [78.02, 30.33],
            [78.03, 30.33],
            [78.03, 30.34],
            [78.02, 30.34],
            [78.02, 30.33]
          ]
        ]
      }
    },
    {
      ""type"": ""Feature"",
      ""properties"": {
        ""name"": ""Emergency Shelter"",
        ""type"": ""shelter"",
        ""description"": ""Designated emergency shelter and resource center.""
      },
      ""geometry"": {
        ""type"": ""Point"",
        ""coordinates"": [
          78.04, 30.33
        ]
      }
    }
  ]
}";

            return Content(geoJsonData, "application/json");
        }
    }
}