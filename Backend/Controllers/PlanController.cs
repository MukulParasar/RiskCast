using Microsoft.AspNetCore.Mvc;

namespace RiskCastBackend.Controllers
{
    [ApiController]
    [Route("api/plan")]
    public class PlanController : ControllerBase
    {
        [HttpGet]
        public IActionResult GetPreparednessPlan()
        {
            var planData = new
            {
                planTitle = "Your Personalized Flood Preparedness Plan",
                location = "Doon Vihar, Dehradun",
                evacuationRoute = "Evacuate to the Community Center via Canal Road, avoiding the flooded Rajpur Road.",
                survivalKit = new[]
                {
                    "Water (1 gallon per person per day)",
                    "Non-perishable food (3-day supply)",
                    "Flashlight and extra batteries",
                    "First-aid kit",
                    "Important documents in a waterproof bag"
                },
                checklist = new[]
                {
                    "Turn off all utilities at the main switch.",
                    "Unplug electronics and move them to higher floors.",
                    "Fill bathtubs and sinks with water.",
                    "Secure outdoor furniture and belongings.",
                    "Contact family and friends to let them know you are safe."
                },
                emergencyContacts = new[]
                {
                    "Emergency Services: 108",
                    "Fire Department: 101",
                    "Local Police: 100"
                }
            };
            return Ok(planData);
        }
    }
}