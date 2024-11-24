
# Enhanced AI-Powered Content Generator

This Streamlit application leverages OpenAI's GPT models to generate high-quality content for various use cases, such as blog posts, social media content, product descriptions, emails, and news articles.

## Features

- **Content Customization**: Choose from different content types and tones.
- **Adjustable Length**: Specify the approximate word count (50–1000 words).
- **Creative Control**: Set the temperature to adjust the creativity level of the AI.
- **Model Selection**: Select between GPT-3.5-Turbo and GPT-4 for content generation.

## Requirements

- Python 3.9 or higher
- OpenAI Python library (`openai`)
- Streamlit (`streamlit`)
- Python-dotenv (`python-dotenv`)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/enhanced-content-generator.git
   cd enhanced-content-generator
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open the app in your browser (usually at `http://localhost:8501`).

3. Fill in the required fields:
   - **Content Topic**: Enter the topic for your content.
   - **Content Type**: Choose the type of content (e.g., blog post, email).
   - **Tone**: Select the desired tone (e.g., professional, humorous).
   - **Word Count**: Adjust the slider for the approximate word count.
   - **AI Model**: Choose the GPT model (GPT-3.5-Turbo or GPT-4).
   - **Temperature**: Adjust creativity (higher values produce more creative content).

4. Click "Generate Content" to create your customized content.

## Error Handling

- **Missing API Key**: Ensure you set your OpenAI API key in the `.env` file.
- **Invalid Inputs**: The app validates inputs and provides feedback for corrections.
- **API Errors**: Handles API and unexpected errors gracefully, displaying meaningful messages.

## Example

- **Content Type**: Blog Post
- **Tone**: Professional
- **Word Count**: 300 words
- **Topic**: "The Future of AI in Healthcare"

Generated output will be displayed in the app.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Happy content generating! 🚀
