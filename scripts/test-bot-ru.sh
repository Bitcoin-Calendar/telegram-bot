#!/bin/bash

# Bitcoin Events Bot Test Script (Russian)
# This script runs the test version of the Russian bot that posts to test channel

echo "🧪 Starting Bitcoin Events Bot Test (Russian)..."
echo "📱 Will post to: test channel"
echo "🌍 Language: Russian"
echo ""

# Set the test language environment variable
export TEST_LANGUAGE=ru

# Run the test bot
docker-compose up --abort-on-container-exit bitcoin-events-bot-test

echo ""
echo "✅ Russian test completed!"
