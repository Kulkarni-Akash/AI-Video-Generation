# AI-Video-Generation

**GenVids** is an AI-driven video generation platform. It allows users to generate videos based on text inputs and custom configurations.

## Tech Stack
- **Python**: Main programming language.
- **Streamlit**: Framework used to create the interactive web interface.
- **Azure OpenAI (Sora Model)**: Utilized for natural language processing and video generation.

## Features
- Generate AI-powered videos from textual descriptions.
- Customize video content with parameters and settings.
- User-friendly web interface using Streamlit.

## Prerequisites
Before running the project locally, ensure you have the following installed:
- **Python** (>= 3.7)
- **pip** (Python package installer)
- **Azure OpenAI Creds(API Endpoint & Key)** (for using Sora Model)

## Setup Instructions
#### 1. Clone the Repository
- To clone the project locally: `git clone https://github.com/yourusername/GenVids.git`
#### 2. Set Up a Virtual Environment
It's recommended to use a virtual environment to avoid conflicts with other projects.
- To create Virtual Environment: `python -m venv .venv`
- To activate Virtual Environment: `venv\Scripts\activate`
#### 3. Install Dependencies
Install the necessary Python libraries using `pip`.
- To install all the required libraries: `pip install -r requirements.txt`
#### 4. Set Up Azure OpenAI API
- Go to the Azure portal and create a new OpenAI resource.
- Obtain your API key for the Sora Model from the Azure OpenAI resource.
- Replace the API endpoint and key in `.env` file
#### 5. Run the Application Locally
After everything is set up, you can start the app by running:
`streamlit run main.py`

## References
1. [To create an Azure OpenAI Service in Azure AI Foundary](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=web-portal)
2. [Generate a video with Sora](https://learn.microsoft.com/en-us/azure/ai-services/openai/video-generation-quickstart?tabs=windows%2Ckeyless)
