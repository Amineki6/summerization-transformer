import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


def generate_summary(text, tokenizer, model):
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)
    summary_ids = model.generate(inputs, max_length=150, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

def create_streamlit_app(tokenizer, model):
    st.title("AML Summarization")
    
    input_text = st.text_area("Enter Text Here", height=400)
    
    if st.button("Generate Summary"):
        if input_text.strip() == "":
            st.warning("Please enter some text")
        else:
            with st.spinner("Generating summary"):
                summary = generate_summary(input_text, tokenizer, model)
                st.success("Summary Generated")
                st.write(summary)

def main():

    model_name = "bnamazci/summarization_aml"  

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    create_streamlit_app(tokenizer, model)

if __name__ == "__main__":
    main()