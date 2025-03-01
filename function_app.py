import azure.functions as func
import logging
import os

app = func.FunctionApp()

@app.blob_trigger(arg_name="myblob", path="mycontainer",
                  connection="charan1_STORAGE") 
def blob_trigger(myblob: func.InputStream):
    file_name = myblob.name
    file_extension = os.path.splitext(file_name)[1].lower()  # Extract file extension

    if file_extension:  # If the file has an extension
        logging.info(f"📂 File added with extension {file_extension}: {file_name}")
    else:  # If no file extension
        logging.info(f"📁 File added with no extension: {file_name}")

    logging.info(f"Blob Size: {myblob.length} bytes")
