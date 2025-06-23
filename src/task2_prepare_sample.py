import pandas as pd

# Load the preprocessed dataset
df = pd.read_csv("data/processed/preprocessed_messages.csv")  # Adjust path as needed

# Select 50 messages with non-empty cleaned_text
sampled_df = df[['cleaned_text']].dropna().head(50)

# Save the messages into a plain text file for manual annotation
sampled_df.to_csv("data/task2_sample_messages.txt", index=False, header=False)

print("✅ Sample messages saved to 'data/task2_sample_messages.txt'")
