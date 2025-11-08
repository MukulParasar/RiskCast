using Microsoft.AspNetCore.Mvc;
using System.Net.Http;
using System.Threading.Tasks;

[Route("api/[controller]")]
[ApiController]
public class RiskController : ControllerBase
{
    private readonly IHttpClientFactory _clientFactory;

    public RiskController(IHttpClientFactory clientFactory)
    {
        _clientFactory = clientFactory;
    }

    [HttpGet]
    public async Task<IActionResult> GetRiskData()
    {
       
        var mlApiUrl = "http://localhost:8000/api/risk-data";

        var client = _clientFactory.CreateClient();
        var response = await client.GetAsync(mlApiUrl);

        if (response.IsSuccessStatusCode)
        {
            var content = await response.Content.ReadAsStringAsync();
            return Content(content, "application/json");
        }

        return StatusCode(500, "Error fetching data from ML service.");
    }
}