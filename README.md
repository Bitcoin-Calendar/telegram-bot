# Bitcoin Historical Events Telegram Bot

A modular Python Telegram bot that automatically posts Bitcoin historical events to Telegram channels. Features clean architecture, multi-language support, and comprehensive testing.

## 🚀 Quick Start

### 1. Setup Environment
```bash
cp env.example .env
# Edit .env with your configuration
```

### 2. Test the Bot
```bash
# Test English bot (posts to test channel)
./scripts/test-bot-en.sh

# Test Russian bot (posts to test channel)  
./scripts/test-bot-ru.sh
```

### 3. Run in Production
```bash
# Production English bot
docker-compose up --abort-on-container-exit bitcoin-events-bot-en

# Production Russian bot
docker-compose up --abort-on-container-exit bitcoin-events-bot-ru
```

## 📁 Project Structure

```
telegram-bot/
├── bot.py                 # Main entry point
├── config.py             # Configuration management
├── api_client.py         # API communication
├── message_formatter.py  # Message formatting & URLs
├── telegram_client.py    # Telegram posting
├── docker-compose.yml    # Docker services
├── scripts/              # Test scripts
│   ├── test-bot-en.sh   # English test script
│   └── test-bot-ru.sh   # Russian test script
└── docs/                # Detailed documentation
```

## ⚙️ Configuration

Required environment variables in `.env`:

```bash
TELEGRAM_BOT_TOKEN=your_bot_token
RUSSIAN_CHAT_ID=@your_russian_channel
ENGLISH_CHAT_ID=@your_english_channel
TELEGRAM_TEST_CHAT_ID=@your_test_channel
API_BASE_URL=http://your-api-url/api
API_KEY=your_api_key
TIMEZONE=UTC
```

## 🧪 Testing

- **Test Mode**: Posts to `TELEGRAM_TEST_CHAT_ID` instead of production channels
- **Safe Testing**: No risk to production channels
- **Both Languages**: Test English and Russian bots separately

## 📅 Automation

Add to crontab for daily posting:

```bash
# Russian bot at 12 PM UTC
0 12 * * * cd /path/to/telegram-bot && docker-compose up --abort-on-container-exit bitcoin-events-bot-ru

# English bot at 3 PM UTC  
0 15 * * * cd /path/to/telegram-bot && docker-compose up --abort-on-container-exit bitcoin-events-bot-en
```

## 📚 Documentation

- [Detailed Setup Guide](docs/setup.md)
- [Architecture Overview](docs/architecture.md)
- [API Reference](docs/api.md)
- [Contributing Guide](CONTRIBUTING.md)

## 🌟 Features

- ✅ **Modular Architecture** - Clean, maintainable code structure
- ✅ **Multi-Language Support** - Russian and English bots
- ✅ **Smart URL Generation** - Constructs proper event URLs from `url_path`
- ✅ **Media Support** - Photos, videos, and text messages
- ✅ **Test Environment** - Safe testing with separate test channel
- ✅ **Docker Ready** - Complete containerization
- ✅ **Automated Posting** - Cron job support

## 📄 License

[MIT](LICENSE)

---

[![⚡️zapmeacoffee](https://img.shields.io/badge/⚡️zap_-me_a_coffee-violet?style=plastic)](https://zapmeacoffee.com/npub1tcalvjvswjh5rwhr3gywmfjzghthexjpddzvlxre9wxfqz4euqys0309hn)