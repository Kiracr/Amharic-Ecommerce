import os
import csv
import configparser

from telethon.sync import TelegramClient
from telethon.tl.types import Channel
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument

# Global counter for total downloaded images
image_downloaded_total = 0
IMAGE_DOWNLOAD_LIMIT = 30  # ✅ Max number of images to download

async def fetch_messages(client, channel_name, limit=1000, media_dir='media'):
    """Fetches messages from a Telegram channel with full metadata."""
    global image_downloaded_total  # Declare as global to modify

    messages_data = []

    try:
        entity = await client.get_entity(channel_name)

        if isinstance(entity, Channel):
            print(f"Fetching messages from {channel_name}...")

            async for message in client.iter_messages(entity, limit=limit):
                if not message:
                    continue

                # Prepare message data
                data = {
                    'channel': channel_name,
                    'message_id': message.id,
                    'text': message.text or "",
                    'media_file': '',
                    'date': message.date.isoformat() if message.date else "",
                    'sender_id': getattr(message.sender_id, 'user_id', message.sender_id),
                    'sender_name': '',
                    'view_count': message.views or 0,
                    'message_type': '',
                }

                # Get sender name if available
                if message.sender:
                    if hasattr(message.sender, 'username'):
                        data['sender_name'] = message.sender.username
                    elif hasattr(message.sender, 'first_name'):
                        data['sender_name'] = message.sender.first_name

                # Handle media — download only if image limit not reached
                if message.media and image_downloaded_total < IMAGE_DOWNLOAD_LIMIT:
                    os.makedirs(media_dir, exist_ok=True)
                    filename = f"{channel_name.strip('@')}_{message.id}"
                    if isinstance(message.media, MessageMediaPhoto):
                        path = await message.download_media(file=f"{media_dir}/{filename}.jpg")
                        data['media_file'] = path
                        data['message_type'] = 'photo'
                        image_downloaded_total += 1  # ✅ Increment
                    elif isinstance(message.media, MessageMediaDocument):
                        path = await message.download_media(file=f"{media_dir}/{filename}")
                        data['media_file'] = path
                        data['message_type'] = 'document'
                        image_downloaded_total += 1  # ✅ Increment
                elif message.media:
                    # Skip downloading, but record media presence
                    data['media_file'] = '[media skipped]'
                    data['message_type'] = 'media_skipped'
                else:
                    data['message_type'] = 'text'

                messages_data.append(data)

    except Exception as e:
        print(f"Error fetching from {channel_name}: {e}")

    return messages_data


def run_scraper():
    """Main function to scrape multiple channels."""
    config = configparser.ConfigParser()
    config.read('config.ini')

    api_id = config['TELEGRAM']['API_ID']
    api_hash = config['TELEGRAM']['API_HASH']
    channels = [c.strip() for c in config['TELEGRAM']['CHANNELS'].split(',')]
    output_file = config['FILES']['RAW_DATA']
    media_folder = config['FILES']['MEDIA_FOLDER']

    with TelegramClient('anon', api_id, api_hash) as client:
        all_messages = []

        for channel in channels:
            messages = client.loop.run_until_complete(fetch_messages(client, channel, media_dir=media_folder))
            all_messages.extend(messages)

        # Save to CSV
        with open(output_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'channel', 'message_id', 'text', 'media_file', 'date',
                'sender_id', 'sender_name', 'view_count', 'message_type'
            ])
            writer.writeheader()
            for msg in all_messages:
                writer.writerow(msg)

        print(f"✅ Done. Saved {len(all_messages)} messages to {output_file}")
        print(f"🖼️ Images downloaded: {image_downloaded_total} (limit: {IMAGE_DOWNLOAD_LIMIT})")


if __name__ == '__main__':
    run_scraper()
