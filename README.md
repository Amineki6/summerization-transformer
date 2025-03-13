# Fine-Tuned Model Summarizer with Streamlit

This project demonstrates how to fine-tune a pre-trained model on Google Colab, upload it to Hugging Face, and deploy it using Streamlit. The model is designed to generate concise summaries for text inputs of up to 512 tokens, producing outputs between 50 to 150 words.

## Project Structure
```
.
│-- README.md            # Documentation
│-- training.ipynb       # Model fine-tuning and preprocessing
│-- streamlit.py         # Streamlit app for text summarization
│-- requirements.txt     # Dependencies for virtual environment
```

## Prerequisites
- Python 3.7+
- Google Colab (for training)
- Hugging Face account (for model hosting)
- Streamlit (for deployment)

## Setup
1. **Create Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: .\venv\Scripts\activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Training the Model
All model training and fine-tuning is completed on Google Colab. The steps include:
- Downloading and preprocessing the dataset
- Tokenizing the data
- Fine-tuning a pre-trained model using Hugging Face Transformers
- Uploading the model and tokenizer to Hugging Face

### Running `training.ipynb`
Open `training.ipynb` in Google Colab and execute the cells in the following order:
1. Download and preprocess dataset (First cell)
2. Load and fine-tune pre-trained model (Second cell)
3. Call necessary functions using `main()` (Third and Fourth cells)

## Deploying with Streamlit
The Streamlit app allows users to input text (up to 512 tokens) and receive a summarized version (50-150 words).

### Running `streamlit.py`
Activate the virtual environment and run the Streamlit app:
```bash
streamlit run streamlit.py
```

### How It Works
- `generate_summary`: Takes input text, summarizes it using the fine-tuned model.
- `create_streamlit_app`: Handles the UI and calls `generate_summary`.
- `main`: Downloads the model and tokenizer from Hugging Face and initializes the app.

## Model and Tokenizer
The fine-tuned model and tokenizer are hosted on Hugging Face. In `streamlit.py`, they are automatically downloaded when the app starts.

## Requirements
Ensure the following libraries are installed:
- `transformers`
- `torch`
- `streamlit`

## Notes
- Fine-tuning was done using Google Colab GPU.
- The model and tokenizer are downloaded directly from Hugging Face in the Streamlit app.

## Acknowledgements
- Hugging Face for the pre-trained models and hosting.
- Streamlit for easy-to-use web deployment.


