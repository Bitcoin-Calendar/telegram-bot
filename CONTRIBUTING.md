# Contributing to Bitcoin Historical Events Telegram Bot

Thank you for your interest in contributing to this project! This document provides guidelines for contributing.

## 🚀 Getting Started

1. **Fork the repository**
2. **Clone your fork:**
   ```bash
   git clone https://github.com/your-username/bitcoin-events-telegram-bot.git
   cd bitcoin-events-telegram-bot
   ```

3. **Set up the development environment:**
   ```bash
   cp env.example .env
   # Edit .env with your configuration
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🧪 Testing

Before submitting any changes, please test thoroughly:

1. **Test your changes:**
   ```bash
   ./test-bot.sh
   ```

2. **Check logs:**
   ```bash
   docker-compose logs bitcoin-events-bot-test
   ```

3. **Verify functionality:**
   - Ensure the bot posts correctly to your test channel
   - Check that all features work as expected
   - Verify error handling works properly

## 📝 Code Style

- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused and concise

## 🔧 Making Changes

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
3. **Test thoroughly**
4. **Commit with clear messages:**
   ```bash
   git commit -m "Add feature: description of what was added"
   ```

5. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**

## 📋 Pull Request Guidelines

- **Clear title** describing the change
- **Detailed description** of what was changed and why
- **Test results** showing the feature works
- **Screenshots** if UI changes are involved
- **Reference issues** if applicable

## 🐛 Reporting Issues

When reporting issues, please include:

- **Clear description** of the problem
- **Steps to reproduce** the issue
- **Expected vs actual behavior**
- **Environment details** (OS, Python version, etc.)
- **Logs** if available

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙏 Thank You

Thank you for contributing to the Bitcoin Historical Events Telegram Bot!
