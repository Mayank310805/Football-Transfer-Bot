from transformers import pipeline

summarizer_pipeline = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text, max_length=120, min_length=30):
    try:
        result = summarizer_pipeline(text[:1024], max_length=max_length, min_length=min_length, do_sample=False)
        return result[0]['summary_text']
    except Exception:
        return "Summary not available due to error."
