from telegram.ext.updater import Updater 
from telegram.update import Update 
from telegram.ext.callbackcontext import CallbackContext 
from telegram.ext.commandhandler import CommandHandler 
from telegram.ext.messagehandler import MessageHandler 
from telegram.ext.filters import Filters 


updater = Updater("your_own_API_Token got from BotFather", 
				use_context=True) 


def start(update: Update, context: CallbackContext): 
	update.message.reply_text( 
		"Enter the text you want to show to the user whenever they start the bot") 

def help(update: Update, context: CallbackContext): 
	update.message.reply_text("Your Message") 


def gmail_url(update: Update, context: CallbackContext): 
	update.message.reply_text("gmail link here") 


def youtube_url(update: Update, context: CallbackContext): 
	update.message.reply_text("youtube link") 


def linkedIn_url(update: Update, context: CallbackContext): 
	update.message.reply_text("Your linkedin profile url") 


def geeks_url(update: Update, context: CallbackContext): 
	update.message.reply_text("GeeksforGeeks url here") 


def unknown_text(update: Update, context: CallbackContext): 
	update.message.reply_text( 
		"Sorry I can't recognize you , you said '%s'" % update.message.text) 


def unknown(update: Update, context: CallbackContext): 
	update.message.reply_text( 
		"Sorry '%s' is not a valid command" % update.message.text) 


