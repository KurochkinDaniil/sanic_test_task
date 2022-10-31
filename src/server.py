from sanic import Sanic, text

app = Sanic("App")


@app.get("/")
async def test_get(request):
    return text("Test")
