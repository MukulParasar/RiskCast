var builder = WebApplication.CreateBuilder(args);

//adding services to the container
builder.Services.AddControllers();
builder.Services.AddOpenApi();


builder.Services.AddHttpClient();


var app = builder.Build();

//HTTP request pipeline here
if (app.Environment.IsDevelopment())
{
    app.MapOpenApi();
}

app.UseHttpsRedirection();


app.UseCors(builder => builder
    .AllowAnyOrigin()
    .AllowAnyMethod()
    .AllowAnyHeader());

app.UseAuthorization();

app.MapControllers();

app.Run();
