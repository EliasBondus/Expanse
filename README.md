# Telegram AI Bot 🤖

Цей бот для Telegram вміє:
- Відповідати на запитання за допомогою ChatGPT
- Показувати поточний час
- Нагадувати про події
- Мати зручну кнопку **AI Відповідь**

## 🚀 Запуск локально

1. Клонуйте репозиторій:
```bash
git clone https://github.com/<your-username>/telegram_ai_bot.git
cd telegram_ai_bot
```

2. Створіть та активуйте віртуальне середовище:
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

3. Встановіть залежності:
```bash
pip install -r requirements.txt
```

4. Створіть файл `.env` (на основі `.env.example`):
```env
TELEGRAM_TOKEN=ваш_токен_бота
OPENAI_API_KEY=ваш_openai_api_key
```

5. Запустіть бота:
```bash
python bot.py
```

## 📦 Deploy на Railway

1. Створіть новий проєкт на [Railway](https://railway.app/)
2. Підключіть свій GitHub репозиторій
3. У `Variables` додайте:
   - `TELEGRAM_TOKEN`
   - `OPENAI_API_KEY`
4. Запустіть деплой.

## 📜 Ліцензія
MIT License.
