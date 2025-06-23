import re
import pandas as pd
import configparser

def clean_text(text):
    """
    Cleans Amharic text by removing URLs, @mentions, and unwanted characters.
    """
    if not isinstance(text, str):
        return ""
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)  # Remove URLs
    text = re.sub(r'\@\w+', '', text)  # Remove @mentions
    text = re.sub(r'[^\u1200-\u137F\s\d.,!?።]', '', text)  # Keep Amharic, numbers, punctuation
    text = re.sub(r'\s+', ' ', text).strip()  # Normalize whitespace
    return text

def preprocess_raw_data():
    """
    Loads raw CSV, cleans the text field, removes media column, and saves all metadata + cleaned_text.
    """
    config = configparser.ConfigParser()
    config.read('config.ini')

    raw_file = config['FILES']['RAW_DATA']       # Should be a .csv file
    processed_file = config['FILES']['PROCESSED_DATA']

    # Load CSV instead of JSONL
    df = pd.read_csv(raw_file, encoding='utf-8')

    print(f"✅ Loaded {len(df)} messages from {raw_file}.")

    # Clean text
    df['cleaned_text'] = df['text'].apply(clean_text)

    # Drop rows with empty cleaned text
    df = df[df['cleaned_text'].str.strip() != '']

    # Drop media_file column if it exists
    if 'media_file' in df.columns:
        df = df.drop(columns=['media_file'])

    # Reorder columns for output
    desired_columns = [
        'channel', 'message_id', 'text', 'date',
        'sender_id', 'sender_name', 'view_count',
        'message_type', 'cleaned_text'
    ]
    # Filter only those that exist in the dataframe
    df = df[[col for col in desired_columns if col in df.columns]]

    # Save processed data
    df.to_csv(processed_file, index=False, encoding='utf-8')
    print(f"✅ Saved {len(df)} cleaned messages to {processed_file}.")

if __name__ == '__main__':
    preprocess_raw_data()
