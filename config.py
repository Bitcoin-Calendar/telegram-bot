#!/usr/bin/env python3
"""
Configuration module for Bitcoin Historical Events Telegram Bot

Handles environment variables and configuration validation.
"""

import os
import pytz
from datetime import datetime


class Config:
    """Handles configuration and environment variables"""
    
    def __init__(self):
        self.telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')
        self.russian_chat_id = os.getenv('RUSSIAN_CHAT_ID')
        self.english_chat_id = os.getenv('ENGLISH_CHAT_ID')
        self.test_chat_id = os.getenv('TELEGRAM_TEST_CHAT_ID')
        self.api_base_url = os.getenv('API_BASE_URL', 'http://localhost:3000/api')
        self.api_key = os.getenv('API_KEY')
        self.timezone_str = os.getenv('TIMEZONE', 'UTC')
        self.language = os.getenv('LANGUAGE', 'en')
        self.is_test_mode = os.getenv('TEST_MODE', 'false').lower() == 'true'
        
        self._validate_config()
        self.target_chat_id = self._determine_target_chat_id()
        self.timezone = pytz.timezone(self.timezone_str)
    
    def _validate_config(self):
        """Validate required environment variables"""
        if not self.telegram_token:
            raise ValueError("TELEGRAM_BOT_TOKEN environment variable is required")
        if not self.api_key:
            raise ValueError("API_KEY environment variable is required")
    
    def _determine_target_chat_id(self):
        """Determine which chat ID to use based on language and test mode"""
        if self.is_test_mode and self.test_chat_id:
            return self.test_chat_id
        elif self.language == 'en' and self.english_chat_id:
            return self.english_chat_id
        elif self.language == 'ru' and self.russian_chat_id:
            return self.russian_chat_id
        else:
            raise ValueError(f"Invalid configuration: LANGUAGE={self.language}, ENGLISH_CHAT_ID={self.english_chat_id}, RUSSIAN_CHAT_ID={self.russian_chat_id}")
    
    def get_todays_date_parts(self) -> tuple:
        """Get today's month and day as strings"""
        today = datetime.now(self.timezone)
        month = f"{today.month:02d}"
        day = f"{today.day:02d}"
        return month, day
