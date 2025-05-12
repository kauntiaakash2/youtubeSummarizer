# Youtube Summarizer

Youtube Summarizer is a powerful tool that extracts and summarizes the content of YouTube videos using advanced Natural Language Processing (NLP) techniques. It saves time by generating concise summaries of long videos, allowing you to grasp key points without watching the entire content.

## Features

* **Quick Summarization:** Get concise summaries of YouTube videos within seconds.
* **Transcript Analysis:** Fetches and analyzes video transcripts for better context.
* **Multi-language Support:** Supports summarization for multiple languages.
* **Keyword Extraction:** Highlights important keywords from the video content.
* **User-Friendly Interface:** Simple and intuitive interface for easy navigation.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/kauntiaakash2/youtubeSummarizer.git
   ```
2. Navigate to the project directory:

   ```bash
   cd youtubeSummarizer
   ```
3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To start the application, simply run:

```bash
python app.py
```

Enter the YouTube video URL and click 'Summarize'. The application will fetch the transcript and generate a summary for you.

## Configuration

If you need to configure API keys or change settings, edit the `config.py` file:

```python
API_KEY = 'your_openai_api_key'
LANGUAGE = 'en'  # Change this to your preferred language
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or suggestions, feel free to open an issue or reach out to the maintainer.
