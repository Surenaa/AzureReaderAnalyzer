import logging
import os
import tempfile

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Check if the request contains a file
    if not req.files or 'file' not in req.files:
        return func.HttpResponse(
            "No file found in the request.",
            status_code=400
        )

    file = req.files['file']

    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()

    try:
        # Save the uploaded file to the temporary directory
        file_path = os.path.join(temp_dir, file.filename)
        file.save(file_path)

        # Read the contents of the file
        with open(file_path, 'r') as f:
            file_contents = f.read()

        return func.HttpResponse(file_contents)

    except Exception as e:
        logging.error(str(e))
        return func.HttpResponse(
            "An error occurred while processing the file.",
            status_code=500
        )

    finally:
        # Clean up the temporary directory
        for file_name in os.listdir(temp_dir):
            file_path = os.path.join(temp_dir, file_name)
            os.remove(file_path)
        os.rmdir(temp_dir)