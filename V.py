import time
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Your bot token here
BOT_TOKEN = '7516244848:AAFARXueG6Lha3ldz8RdNzxeoqk9smZIiaw'  # Replace with your bot's token
ADMIN_ID = 1441704343  # Replace with your actual Telegram user ID

class ViewBoosterBot:
    def __init__(self):
        self.points = 0

    def start(self, update: Update, context: CallbackContext):
        """Start command to display the welcome message and menu"""
        welcome_message = "Welcome to View Booster Bot!\n"
        welcome_message += "Use the following commands:\n"
        welcome_message += "/view_points - View your points\n"
        welcome_message += "/add_points - Add points to your account\n"
        welcome_message += "/statistics - View statistics\n"
        welcome_message += "/help - Get help\n"
        welcome_message += "/exit - Exit the bot\n"
        update.message.reply_text(welcome_message)

    def view_points(self, update: Update, context: CallbackContext):
        """View points command"""
        update.message.reply_text(f"\nYou have {self.points} points.")

    def add_points(self, update: Update, context: CallbackContext):
        """Add points command - admin only"""
        if update.message.from_user.id != ADMIN_ID:
            update.message.reply_text("You do not have permission to add points.")
            return
        
        try:
            amount = float(" ".join(context.args))  # Read amount from user input
            if amount < 10:
                update.message.reply_text("Minimum amount should be ₹10.")
            else:
                added_points = amount * 1000  # Assuming ₹1 = 1000 points
                self.points += added_points
                update.message.reply_text(f"{added_points} points added successfully! Total points: {self.points}.")
        except ValueError:
            update.message.reply_text("Invalid input. Please enter a valid number.")

    def statistics(self, update: Update, context: CallbackContext):
        """View statistics command"""
        update.message.reply_text(f"\nStatistics:\nTotal Points: {self.points}")
        update.message.reply_text(f"Date: {time.strftime('%Y-%m-%d %H:%M:%S')}")

    def help(self, update: Update, context: CallbackContext):
        """Help command"""
        help_message = "\nHelp:\n"
        help_message += "1. To add points, use the /add_points command and follow the instructions.\n"
        help_message += "2. Minimum payment is ₹10, which equals 1,000 points.\n"
        help_message += "3. For issues, contact support.\n"
        update.message.reply_text(help_message)

    def exit(self, update: Update, context: CallbackContext):
        """Exit command"""
        update.message.reply_text("Thank you for using View Booster Bot! Bye!")
        # The bot will just stop replying to messages, as there's no direct exit command in Telegram bots.

# Initialize the bot and application
def main():
    bot = ViewBoosterBot()

    # Set up the application and handlers
    application = Application.builder().token(BOT_TOKEN).build()

    # Command handlers
    application.add_handler(CommandHandler("start", bot.start))
    application.add_handler(CommandHandler("view_points", bot.view_points))
    application.add_handler(CommandHandler("add_points", bot.add_points))
    application.add_handler(CommandHandler("statistics", bot.statistics))
    application.add_handler(CommandHandler("help", bot.help))
    application.add_handler(CommandHandler("exit", bot.exit))

    print("🤖 View Booster Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
