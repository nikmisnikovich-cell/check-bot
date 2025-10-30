import logging
import re
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# ВСТАВЬТЕ СЮДА ВАШ ТОКЕН
BOT_TOKEN = "8099989104:AAFyAi8SgmCN0NkFRIxlFBcb5n3pU-a_BUQ"

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Словарь для сопоставления ключевых слов с пользователями
KEYWORD_MAPPING = {
    "совлд": "@yuoookii",
    "влд": "@Xilway"
}

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик сообщений"""
    if not update.message or not update.message.text:
        return
    
    message_text = update.message.text.lower()
    
    # Проверяем комбинацию "со влд" (раздельное написание)
    if "со влд" in message_text:
        response = "🕵️‍♂️ Дело раскрыто! Обнаружен зов - @yuoookii 👁️‍🗨️"
        await update.message.reply_text(response)
        return
    
    # Проверяем обычное написание "совлд"
    if "совлд" in message_text:
        response = "🕵️‍♂️ Дело раскрыто! Обнаружен зов - @yuoookii 👁️‍🗨️"
        await update.message.reply_text(response)
        return
    
    # Проверяем отдельное слово "влд"
    words = re.findall(r'\b\w+\b', message_text)
    if "влд" in words:
        response = "🕵️‍♂️ Дело раскрыто! Обнаружен зов - @Xilway 👁️‍🗨️"
        await update.message.reply_text(response)

def main():
    """Основная функция запуска бота"""
    # Создаем приложение
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Добавляем обработчик текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Запускаем бота
    print("🕵️‍♂️ Детектив-бот запущен и ведёт наблюдение...")
    application.run_polling()

if __name__ == "__main__":
    main()