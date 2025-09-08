#!/usr/bin/env python3
"""
Bitcoin Historical Events Telegram Bot

This bot fetches today's Bitcoin historical events from the API and posts them
to specified Telegram chats/channels. Supports both Russian and English languages.
If multiple events exist for today, it posts them with a 1-hour delay between each post.
"""

import sys
import logging
import asyncio

from config import Config
from api_client import ApiClient
from message_formatter import MessageFormatter
from telegram_client import TelegramClient


class BitcoinEventsBot:
    """Main bot class that orchestrates the posting workflow"""
    
    def __init__(self):
        # Initialize components
        self.config = Config()
        self.api_client = ApiClient(self.config)
        self.message_formatter = MessageFormatter(self.config)
        self.telegram_client = TelegramClient(self.config)
        
        # Setup logging
        self.setup_logging()
        
        # Log configuration details
        if self.config.is_test_mode and self.config.test_chat_id:
            self.logger.info(f"Running in TEST MODE for {self.config.language} - using TELEGRAM_TEST_CHAT_ID")
        elif self.config.language == 'en' and self.config.english_chat_id:
            self.logger.info(f"Running for ENGLISH language - posting to {self.config.english_chat_id}")
        elif self.config.language == 'ru' and self.config.russian_chat_id:
            self.logger.info(f"Running for RUSSIAN language - posting to {self.config.russian_chat_id}")
    
    def setup_logging(self):
        """Setup logging configuration"""
        log_filename = f"bitcoin_events_bot_{self.config.language}.log"
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_filename),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
        self.logger.info(f"Bot initialized for language: {self.config.language}, target chat: {self.config.target_chat_id}")
    
    async def run_daily_posting(self):
        """Main function to fetch and post today's events"""
        self.logger.info("Starting daily Bitcoin events posting")
        
        # Fetch today's events
        events = self.api_client.fetch_todays_events()
        
        if not events:
            self.logger.info("No events found for today")
            return
        
        self.logger.info(f"Found {len(events)} events for today")
        
        # Post events with delays
        for i, event in enumerate(events):
            self.logger.info(f"Processing event {i+1}: {event.get('title', 'Unknown')}")
            
            # Format the event message and get media URL and type
            message, media_url, media_type = self.message_formatter.format_event_message(event)
            self.logger.info(f"Formatted message length: {len(message)}")
            self.logger.info(f"Media URL: {media_url}")
            self.logger.info(f"Media type: {media_type}")
            
            # Post the event
            success = await self.telegram_client.post_event_to_telegram(message, media_url, media_type)
            
            if success:
                self.logger.info(f"Posted event {i+1}/{len(events)}: {event.get('title', 'Unknown')}")
            else:
                self.logger.error(f"Failed to post event {i+1}/{len(events)}: {event.get('title', 'Unknown')}")
            
            # Wait before posting the next event (except for the last one)
            if i < len(events) - 1:
                self.logger.info("Waiting 1 hour before posting next event...")
                await asyncio.sleep(3600)  # 1 hour delay between events
        
        self.logger.info("Daily posting completed")
        # Exit after completing the posting
        sys.exit(0)


async def main():
    """Main entry point"""
    try:
        bot = BitcoinEventsBot()
        await bot.run_daily_posting()
    except Exception as e:
        logging.error(f"Bot failed to run: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())