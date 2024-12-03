from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace with your Bot's Token
TOKEN = "7074559050:AAE8P3KU9NvpUgKFxJXgl9NOoBUHWZK_SLY"

# Replace with your Admin's chat ID
ADMIN_CHAT_ID = "1441704343"

# Start command handler
def start(update: Update, context: CallbackContext):
    # Custom keyboard to interact with the admin
    keyboard = [
        [KeyboardButton("Contact Admin")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    update.message.reply_text(
        "Welcome! Please send your feedback. We appreciate your input. If you'd like to talk to the admin, click the button below.",
        reply_markup=reply_markup
    )

# Help command handler
def help_command(update: Update, context: CallbackContext):
    help_text = (
        "This bot allows you to send feedback. Here's how it works:\n\n"
        "/start - Start the bot and send your feedback\n"
        "/help - Get help about the bot's functionality\n"
        "Click the 'Contact Admin' button to directly send a message to the admin."
    )
    update.message.reply_text(help_text)

# Feedback message handler
def feedback(update: Update, context: CallbackContext):
    feedback_message = update.message.text
    if feedback_message.lower() == "contact admin":
        # If the user requests to talk to the admin, send the message to the admin
        context.bot.send_message(
            chat_id=ADMIN_CHAT_ID,
            text=f"User {update.message.from_user.username} ({update.message.from_user.id}) wants to contact you."
        )
        update.message.reply_text("You are now connected with the admin. Please wait for a response.")
    else:
        # Forward feedback to the admin
        context.bot.send_message(
            chat_id=ADMIN_CHAT_ID,
            text=f"New Feedback from {update.message.from_user.username} ({update.message.from_user.id}):\n{feedback_message}"
        )
        # Acknowledge the feedback
        update.message.reply_text("Thank you for your feedback!")

# Error handler
def error(update: Update, context: CallbackContext):
    print(f"Error: {context.error}")

# Main function to run the bot
def main():
    # Set up the Updater with the bot token
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Add command handler for /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Add command handler for /help
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Add message handler for feedback (any text message will be treated as feedback)
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, feedback))

    # Add an error handler
    dispatcher.add_error_handler(error)

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl+C
    updater.idle()

# Entry point to run the bot
if __name__ == "__main__":
    main()
