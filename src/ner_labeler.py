import re

# Define the keywords and functions FIRST

locations = ['ቦሌ', 'አዲስ', 'አበባ', 'ማዕከል']
product_keywords = ['ጫማ', 'ልብስ', 'ባልሸምበት', 'ሻንጣ', 'የሴቶች', 'የልጆች']

def tokenize_amharic(text):
    return text.split()

def label_token(token):
    if re.match(r'^\d{2,5}$', token):
        return 'B-PRICE'
    elif token == 'ብር':
        return 'I-PRICE'
    elif token in locations:
        return 'B-LOC'
    elif token in product_keywords:
        return 'B-Product'
    return 'O'

def auto_label_txt(input_txt_path, output_path, limit=None):
    with open(input_txt_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    if limit:
        lines = lines[:limit]
    with open(output_path, 'w', encoding='utf-8') as out_file:
        for sentence in lines:
            sentence = sentence.strip()
            if not sentence:
                continue
            tokens = tokenize_amharic(sentence)
            for token in tokens:
                label = label_token(token)
                out_file.write(f"{token}\t{label}\n")
            out_file.write("\n")
    print(f"✅ CoNLL file saved: {output_path}")

# CALL the function AFTER defining it
auto_label_txt('data/task2_sample_messages.txt', 'data/amharic_ner_labels_auto.conll', limit=50)
