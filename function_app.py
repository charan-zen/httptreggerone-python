import azure.functions as func
import logging
import os
from datetime import datetime

app = func.FunctionApp()

@app.blob_trigger(
    arg_name="myblob",
    path="zen-charan-blob-test/{name}",  # Captures dynamic blob names
    connection="AzureWebJobsStorage"     # Uses default Azure storage connection
)
def blob_trigger(myblob: func.InputStream):
    file_name = myblob.name  # Full blob path
    file_extension = os.path.splitext(file_name)[1].lower()  # Extract file extension
    file_size = myblob.length  # Get file size

    # Add a timestamp for debugging
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    # Logging file details
    if file_extension:
        logging.info(f"📂 [{timestamp}] File uploaded with extension {file_extension}: {file_name}")
    else:
        logging.info(f"📁 [{timestamp}] File uploaded without an extension: {file_name}")

    logging.info(f"📦 [{timestamp}] Blob Size: {file_size} bytes")
