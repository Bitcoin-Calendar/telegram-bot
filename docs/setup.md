# Setup Guide

Complete setup instructions for the Bitcoin Historical Events Telegram Bot.

## Prerequisites

- Python 3.11+
- Docker and Docker Compose
- Telegram Bot Token (from [@BotFather](https://t.me/botfather))
- Bitcoin Calendar API access
- Telegram channel or chat ID

## 1. Clone and Setup

```bash
git clone <your-repo-url>
cd telegram-bot
cp env.example .env
```

## 2. Configure Environment Variables

Edit `.env` file with your configuration:

```bash
# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN=your_bot_token_here

# Russian Channel Configuration
RUSSIAN_CHAT_ID=@your_russian_channel

# English Channel Configuration  
ENGLISH_CHAT_ID=@your_english_channel

# Test Channel (used for both languages when TEST_MODE=true)
TELEGRAM_TEST_CHAT_ID=@your_test_channel

# API Configuration
API_BASE_URL=http://your-api-url/api
API_KEY=your_api_key_here

# Optional Configuration
TIMEZONE=UTC
```

### Environment Variables Reference

| Variable | Required | Description | Example |
|----------|----------|-------------|---------|
| `TELEGRAM_BOT_TOKEN` | Yes | Your Telegram bot token | `123456789:ABC...` |
| `RUSSIAN_CHAT_ID` | Yes | Russian production channel | `@your_russian_channel` |
| `ENGLISH_CHAT_ID` | Yes | English production channel | `@your_english_channel` |
| `TELEGRAM_TEST_CHAT_ID` | Yes | Test channel for both languages | `@your_test_channel` |
| `API_BASE_URL` | Yes | Bitcoin Calendar API base URL | `http://api.example.com/api` |
| `API_KEY` | Yes | API authentication key | `your_api_key_here` |
| `TIMEZONE` | No | Timezone for date calculations | `UTC` |

## 3. Build Docker Images

```bash
docker-compose build
```

## 4. Test the Setup

### Test English Bot
```bash
./scripts/test-bot-en.sh
```

### Test Russian Bot
```bash
./scripts/test-bot-ru.sh
```

Both test scripts will:
- Post to your test channel (`TELEGRAM_TEST_CHAT_ID`)
- Use current date events for testing
- Show detailed logs

## 5. Production Deployment

### Manual Run
```bash
# English production bot
docker-compose up --abort-on-container-exit bitcoin-events-bot-en

# Russian production bot
docker-compose up --abort-on-container-exit bitcoin-events-bot-ru
```

### Automated Deployment (Cron)

Add to your crontab:
```bash
crontab -e
```

Add these lines:
```bash
# Russian bot at 12 PM UTC (3 PM Moscow time)
0 12 * * * cd /path/to/telegram-bot && docker-compose up --abort-on-container-exit bitcoin-events-bot-ru

# English bot at 3 PM UTC
0 15 * * * cd /path/to/telegram-bot && docker-compose up --abort-on-container-exit bitcoin-events-bot-en
```

## 6. Verification

### Check Logs
```bash
# View all logs
docker-compose logs

# View specific bot logs
docker-compose logs bitcoin-events-bot-en
docker-compose logs bitcoin-events-bot-ru
```

### Verify Posts
- Check your test channel for test posts
- Check production channels for daily posts
- Verify URLs are correctly formatted
- Confirm media (photos/videos) are posted correctly

## Troubleshooting

### Common Issues

1. **Bot not posting to test channel**
   - Verify `TEST_MODE=true` is set in docker-compose
   - Check `TELEGRAM_TEST_CHAT_ID` is correct

2. **API connection errors**
   - Verify `API_BASE_URL` and `API_KEY` are correct
   - Check network connectivity

3. **Docker build failures**
   - Ensure all Python files are present
   - Check Dockerfile syntax

4. **Permission errors**
   - Ensure bot has admin rights in target channels
   - Verify bot token is valid

### Debug Mode

Run with debug logging:
```bash
docker run --rm --env-file .env -e TEST_MODE=true -e LANGUAGE=en telegram-bot_bitcoin-events-bot-test
```

## Next Steps

- [Architecture Overview](architecture.md)
- [API Reference](api.md)
- [Contributing Guide](../CONTRIBUTING.md)
