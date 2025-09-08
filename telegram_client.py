#!/usr/bin/env python3
"""
Telegram Client module for Bitcoin Historical Events Telegram Bot

Handles posting messages to Telegram.
"""

import logging
from telegram import Bot
from telegram.error import TelegramError


class TelegramClient:
    """Handles Telegram posting"""
    
    def __init__(self, config):
        self.config = config
        self.bot = Bot(token=config.telegram_token)
        self.logger = logging.getLogger(__name__)
        
        # Validate chat_id format
        try:
            self.target_chat_id = int(config.target_chat_id)
        except ValueError:
            # If it's a channel username (starts with @), keep as string
            if not config.target_chat_id.startswith('@'):
                raise ValueError("Chat ID must be a valid integer or channel username starting with @")
            self.target_chat_id = config.target_chat_id
    
    async def post_event_to_telegram(self, message: str, media_url: str = None, media_type: str = None) -> bool:
        """Post a message, photo, or video to Telegram"""
        try:
            if media_url and media_type:
                if media_type == 'video':
                    # Send video with caption
                    await self.bot.send_video(
                        chat_id=self.target_chat_id,
                        video=media_url,
                        caption=message,
                        parse_mode='HTML'
                    )
                    self.logger.info("Successfully posted event with video to Telegram")
                else:
                    # Send photo with caption
                    await self.bot.send_photo(
                        chat_id=self.target_chat_id,
                        photo=media_url,
                        caption=message,
                        parse_mode='HTML'
                    )
                    self.logger.info("Successfully posted event with photo to Telegram")
            else:
                # Send text message only
                # Enable web preview if there are references but no media
                has_references = 'http' in message
                disable_preview = not has_references
                await self.bot.send_message(
                    chat_id=self.target_chat_id,
                    text=message,
                    parse_mode='HTML',
                    disable_web_page_preview=disable_preview
                )
                self.logger.info("Successfully posted event to Telegram")
            return True
            
        except TelegramError as e:
            self.logger.error(f"Failed to post to Telegram: {e}")
            return False
        except Exception as e:
            self.logger.error(f"Unexpected error posting to Telegram: {e}")
            return False
