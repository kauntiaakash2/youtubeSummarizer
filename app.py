import os

from flask import Flask, render_template, request
from google import genai
from google.genai import types

app = Flask(__name__)

PROJECT_ID = "youtubesummarize-2006"

client = genai.Client(
   vertexai=True,
   project=PROJECT_ID,
   location="us-central1",
)

# Define the home page route.
@app.route('/', methods=['GET'])
def index():
   '''
   Renders the home page.
   Returns:The rendered template.
   '''
   return render_template('index.html')


def generate(youtube_link, model, additional_prompt):

   # Prepare youtube video using the provided link
   youtube_video = types.Part.from_uri(
       file_uri=youtube_link,
       mime_type="video/*",
   )

   # If addtional prompt is not provided, just append a space
   if not additional_prompt:
       additional_prompt = " "

   # Prepare content to send to the model
   contents = [
       youtube_video,
       types.Part.from_text(text="""Provide a summary of the video."""),
       additional_prompt,
   ]

   # Define content configuration
   generate_content_config = types.GenerateContentConfig(
       temperature = 1,
       top_p = 0.95,
       max_output_tokens = 8192,
       response_modalities = ["TEXT"],
   )

   return client.models.generate_content(
       model = model,
       contents = contents,
       config = generate_content_config,
   ).text

@app.route('/summarize', methods=['GET', 'POST'])
def summarize():
   '''
   Summarize the user provided YouTube video.
   Returns: Summary.
   '''

   # If the request is a POST request, process the form data.
   if request.method == 'POST':
       youtube_link = request.form['youtube_link']
       model = request.form['model']
       additional_prompt = request.form['additional_prompt']
     
       # Generate the summary.
       try:
           summary = generate(youtube_link, model, additional_prompt)
           return summary

       except ValueError as e:
           raise e
 
   # If the request is a GET request, redirect to the home page.
   else:
       return redirect('/')


if __name__ == '__main__':
   server_port = os.environ.get('PORT', '8080')
   app.run(debug=False, port=server_port, host='0.0.0.0')