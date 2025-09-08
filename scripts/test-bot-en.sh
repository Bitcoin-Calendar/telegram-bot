#!/bin/bash

# Bitcoin Events Bot Test Script (English)
# This script runs the test version of the English bot that posts to test channel

echo "🧪 Starting Bitcoin Events Bot Test (English)..."
echo "📱 Will post to: test channel"
echo "🌍 Language: English"
echo ""

# Set the test language environment variable
export TEST_LANGUAGE=en

# Run the test bot
docker-compose up --abort-on-container-exit bitcoin-events-bot-test

echo ""
echo "✅ English test completed!"
