#!/usr/bin/env python3
"""
Message Formatter module for Bitcoin Historical Events Telegram Bot

Handles message formatting and URL construction.
"""

import json
import logging
from typing import Dict, Tuple


class MessageFormatter:
    """Handles message formatting and URL construction"""
    
    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger(__name__)
        # Video file extensions that Telegram supports
        self.video_extensions = {'.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm', '.m4v', '.3gp'}
    
    def construct_event_url(self, url_path: str) -> str:
        """Construct the full event URL based on language and url_path"""
        if not url_path:
            return ""
        
        base_url = "https://bitcoin-calendar.org"
        lang_prefix = "ru" if self.config.language == "ru" else "en"
        return f"{base_url}/{lang_prefix}/events/{url_path}"
    
    def is_video_file(self, url: str) -> bool:
        """Check if a URL points to a video file based on its extension"""
        if not url:
            return False
        
        # Extract file extension from URL
        url_lower = url.lower()
        for ext in self.video_extensions:
            if url_lower.endswith(ext):
                return True
        
        # Also check for video in the URL path
        if any(video_type in url_lower for video_type in ['/video/', '/videos/', '.mp4', '.avi', '.mov']):
            return True
        
        return False
    
    def format_event_message(self, event: Dict) -> Tuple:
        """Format an event into a readable Telegram message and return (message, media_url, media_type)"""
        self.logger.info("Entering format_event_message method")
        try:
            # Get title, description, and url_path
            title = event.get('title', 'No title')
            description = event.get('description', 'No description available')
            url_path = event.get('url_path', '')
            
            # Build the message
            message = f"<b>{title}</b>\n\n"
            message += f"{description}"
            
            # Add event link if url_path is available
            if url_path:
                event_url = self.construct_event_url(url_path)
                if event_url:
                    # Use bitcoin-calendar.org as link text
                    message += f"\n\n<a href=\"{event_url}\">bitcoin-calendar.org</a>"
            
            # Add footer with links based on language
            if self.config.language == 'en':
                message += "\n\n⚡️ <b><a href=\"https://bitcoin-calendar.org/en/support\">Zap Me a Coffee</a></b> • <b><a href=\"https://bitcoin-calendar.org/en\">Website</a></b>"
            else:
                message += "\n\n⚡️ <b><a href=\"https://bitcoin-calendar.org/ru/support\">Донат</a></b> • <b><a href=\"https://bitcoin-calendar.org/ru\">Сайт</a></b> • <b><a href=\"https://21ideas.org/hermes/\">Обменник</a></b>"
            
            # Debug: Log the final message
            self.logger.info(f"Final formatted message: {message}")
            
            # Check for media files
            media_url = None
            media_type = None  # 'photo', 'video', or None
            media = event.get('media', '')
            if media:
                try:
                    # Parse JSON media if they exist
                    if media.startswith('[') and media.endswith(']'):
                        media_list = json.loads(media)
                        if isinstance(media_list, list) and media_list:
                            media_url = media_list[0]  # Use first media file
                            # Determine media type
                            if self.is_video_file(media_url):
                                media_type = 'video'
                                self.logger.info(f"Found video URL: {media_url}")
                            else:
                                media_type = 'photo'
                                self.logger.info(f"Found photo URL: {media_url}")
                    else:
                        # If JSON parsing fails, treat as plain URL
                        if media.startswith('http'):
                            media_url = media
                            if self.is_video_file(media_url):
                                media_type = 'video'
                                self.logger.info(f"Found video URL: {media_url}")
                            else:
                                media_type = 'photo'
                                self.logger.info(f"Found photo URL: {media_url}")
                except json.JSONDecodeError:
                    # If JSON parsing fails, treat as plain URL
                    if media.startswith('http'):
                        media_url = media
                        if self.is_video_file(media_url):
                            media_type = 'video'
                            self.logger.info(f"Found video URL: {media_url}")
                        else:
                            media_type = 'photo'
                            self.logger.info(f"Found photo URL: {media_url}")
            
            return message, media_url, media_type
            
        except Exception as e:
            self.logger.error(f"Error formatting event message: {e}")
            return f"Error formatting event: {str(e)}", None, None
