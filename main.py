from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Define a function to handle the /start command
def start(update, context):
    update.message.reply_text("Welcome to the Addition Bot! Please send me two numbers separated by space.")

# Define a function to handle regular messages
def handle_message(update, context):
    # Split the user's message into two numbers
    numbers = update.message.text.split()
    
    # Check if exactly two numbers were provided
    if len(numbers) == 2:
        try:
            # Try converting the numbers to floats and summing them
            num1 = float(numbers[0])
            num2 = float(numbers[1])
            result = num1 + num2
            update.message.reply_text(f"The sum of {num1} and {num2} is: {result}")
        except ValueError:
            update.message.reply_text("Invalid input! Please enter two valid numbers.")
    else:
        update.message.reply_text("Invalid input! Please provide exactly two numbers separated by space.")

def main():
    # Set up the updater and dispatcher
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN", use_context=True)
    dp = updater.dispatcher

    # Add command handler for the /start command
    dp.add_handler(CommandHandler("start", start))

    # Add message handler for regular messages
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
