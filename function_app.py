import azure.functions as func
import logging

# Define the FunctionApp instance
app = func.FunctionApp()

# Define the route for the function
@app.route(route="YT-Downloader", methods=["GET", "POST"])
def YT_Downloader(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Get the 'name' parameter from the query string
    name = req.params.get('name')

    if not name:
        try:
            # Try to parse JSON from the request body
            req_body = req.get_json()
            name = req_body.get('name')
        except ValueError:
            pass

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
        )
