#!/usr/bin/env python3
"""
API Client module for Bitcoin Historical Events Telegram Bot

Handles communication with the Bitcoin Calendar API.
"""

import json
import logging
import requests
from typing import List, Dict


class ApiClient:
    """Handles API communication"""
    
    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger(__name__)
    
    def fetch_todays_events(self) -> List[Dict]:
        """Fetch events that occurred on today's month and day from the API"""
        month, day = self.config.get_todays_date_parts()
        
        self.logger.info(f"Fetching events for month: {month}, day: {day}")
        
        try:
            headers = {
                'X-API-KEY': self.config.api_key,
                'Content-Type': 'application/json'
            }
            
            params = {
                'month': month,
                'day': day,
                'limit': 100,  # Get up to 100 events
                'lang': self.config.language
            }
            
            response = requests.get(
                f"{self.config.api_base_url}/events",
                headers=headers,
                params=params,
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                events = data.get('events', [])
                self.logger.info(f"Successfully fetched {len(events)} events for today")
                return events
            else:
                self.logger.error(f"API request failed with status {response.status_code}: {response.text}")
                return []
                
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Failed to fetch events from API: {e}")
            return []
        except json.JSONDecodeError as e:
            self.logger.error(f"Failed to parse API response: {e}")
            return []
