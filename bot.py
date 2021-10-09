import os, json, datetime, sys
from requests import get
from random import randint
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, InlineQueryHandler
from telegram import InlineQueryResultArticle, InlineQueryResultPhoto, InlineQueryResultGif, InputTextMessageContent, Update, Bot, ReplyKeyboardMarkup

token = os.getenv("token", "")
app_name = os.getenv("RAILWAY_STATIC_URL", "")

if len(str(app_name)) < 2:
   app_name_heroku = os.getenv("HEROKU_APP_NAME", "")
   if app_name_heroku == "":
      print("please put your app url for webhook in env or disable webhook")
      sys.exit(1)
   app_name = app_name_heroku + ".herokuapp.com"

print(app_name)

app_url = "https://" + app_name + "/"
print(app_url)

if len(str(token)) < 5: print("please put your token in env"); sys.exit(1) # telegram bot token
PORT12 = int(os.environ.get('PORT', 8443))

x = datetime.datetime.utcnow()
i = x + datetime.timedelta(hours=3)
y = i.strftime("%Y-%m-%d_%I:%M%P")
d = i.strftime("%Y-%m-%d")
na = d + ".txt"
o = open(na, "a")
print(y)
print("""  """ + y , file = o)

print("My PID is:", os.getpid())

def gimmememe():
    api_link = "https://meme-api.herokuapp.com/gimme"
    res = get(api_link)
    jsond = json.loads(res.text)
    #print(jsond)
    try:
        post_title = jsond["title"]
        memelink = jsond["url"]
        print(memelink)
        return(post_title, memelink)
    except Exception as e:
        print(e)
        sndlog(str(e))



def sndlog(log):
    context = context_main
    bot = Bot(token)
    context.bot.send_message(chat_id = ch_id, text = log )


def inlinequery(update, context):
    des, meme_link = gimmememe()
    have_description = 0
    if len(des) == 0:
        have_description = 0
    else: have_description = 1

    if ".jpg" in meme_link or ".png" in meme_link or ".jpeg":
        if have_description == 0:
           results = [InlineQueryResultPhoto(id=str(uuid4()), photo_url = meme_link, thumb_url = meme_link)]

        elif have_description == 1:
           results = [InlineQueryResultPhoto(id=str(uuid4()), photo_url = meme_link, caption = des, thumb_url = meme_link)]

    elif ".gif" in meme_link or ".mp4" in meme_link:
        if have_description == 0:
           results = [InlineQueryResultGif(id=str(uuid4()), gif_url = meme_link, thumb_url = meme_link)]
        elif have_description == 1:
           results = [InlineQueryResultGif(id=str(uuid4()), gif_url = meme_link, caption = des, thumb_url = meme_link)]


    update.inline_query.answer(results, cache_time=0)

def gimme(update, context):
    global context_main; global ch_id
    context_main = context; ch_id = update.message.chat_id
    des, meme_link = gimmememe()
    have_description = 0
    if len(des) == 0:
        have_description = 0
    else: have_description = 1

    if ".jpg" in meme_link or ".png" in meme_link or ".jpeg":
        if have_description == 0:
            context.bot.send_photo(chat_id = update.message.chat_id, photo=meme_link)
        elif have_description == 1:
            context.bot.send_photo(chat_id = update.message.chat_id, photo=meme_link, caption = des)

    elif ".gif" in meme_link or ".mp4" in meme_link:
        if have_description == 0:
            context.bot.send_animation(chat_id = update.message.chat_id, photo=meme_link)
        elif have_description == 1:
            context.bot.send_animation(chat_id = update.message.chat_id, photo=meme_link, caption = des)


    print("msg from ", str(update.effective_user.first_name), str(update.effective_user.last_name) ,str(update.effective_user.username), file = o)
    print("msg from ", str(update.effective_user.first_name), str(update.effective_user.last_name) ,str(update.effective_user.username))

def thak(update, context):
    ran = randint(0, 1)
    if ran == 1:
       update.message.reply_text(" You are welcome")
    else:
       update.message.reply_text(" it's my duty")
    print("Thanks from ", str(update.effective_user.first_name), str(update.effective_user.last_name) ,str(update.effective_user.username), file = o)
    print("Thanks from ", str(update.effective_user.first_name), str(update.effective_user.last_name) ,str(update.effective_user.username))

def slash_start(update, context):
    keyboard = [
        ["👊meme","🥴ultra bored"],
        ["🤖 Start the Bot","⁉️ Help"]]

    username = "@" + update.effective_user.username
    frname = update.effective_user.first_name
    lasname = update.effective_user.last_name
    name = ""

    if username != "None":
       name = username
    elif frname != "None":
       if lasname != "None":
           name = frname + "" + lasname
       else: name = frname
    elif username == "None" and frname == "None":
       name = str(update.message.chat_id)


    msg0 = """ Hi %s,
 
Welcome to @Memes_XD_bot 👋

I can scrape reddit for memes just grab a coffee and click the button below
 
 ⚠️ REPORT any bugs at @xd2222 or @Pine_Orange ⚠️ """ %name
    update.message.reply_text(msg0, reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))
    print("New user !", str(update.effective_user.first_name), str(update.effective_user.last_name) ,str(update.effective_user.username), file = o)
    print("New user !", str(update.effective_user.first_name), str(update.effective_user.last_name) ,str(update.effective_user.username))

def help_cmd(update, context):
    username = "@" + update.effective_user.username
    frname = update.effective_user.first_name
    lasname = update.effective_user.last_name
    name = ""

    if username != "None":
       name = username
    elif frname != "None":
       if lasname != "None":
           name = frname + "" + lasname
       else: name = frname
    elif username == "None" and frname == "None":
       name = str(update.message.chat_id)


    help = """ Hi %s,
 
Welcome to @Memes_XD_bot 👋

I can scrape reddit for memes just grab a coffee and click the button below
 
 ⚠️ REPORT any bugs at @xd2222 or @Pine_Orange ⚠️ """ %name
    update.message.reply_text(help)
    print("User Need Help !", str(update.effective_user.first_name), str(update.effective_user.last_name) ,str(update.effective_user.username), file = o)
    print("User Need Help !", str(update.effective_user.first_name), str(update.effective_user.last_name) ,str(update.effective_user.username))


def beta(update, context):
    msg = "Sorry this feature is still under development"
    update.message.reply_text(msg)

def listfil(update, context):
    c = o.flush()
    q = os.listdir()
    r = open("ki.txt", "w+")
    w = json.dump(q, r, indent =2)
    n = r.close()
    e = open("ki.txt", "r")
    z = e.read()
    print(z)
    print(z, file = o.l)
    t = update.message.reply_text(z)

def sendfil(update, context):
    fn = " ".join(context.args)
    clo = o.flush()
    context.bot.send_document(chat_id=update.message.chat_id, document = open(str(fn), "rb"))
    print("file sent s")
    print("file sent s", file = o.l)
    clo = o.flush()



def main():
    updater = Updater(token)
    dp = updater.dispatcher
    dp.add_handler(InlineQueryHandler(inlinequery))
    dp.add_handler(CommandHandler('start', slash_start))
    dp.add_handler(CommandHandler('help', help_cmd))
    dp.add_handler(CommandHandler('gimme', gimme))
    dp.add_handler(CommandHandler('list', listfil))
    dp.add_handler(CommandHandler('snd', sendfil))
    dp.add_handler(MessageHandler(Filters.regex('👊meme'), gimme))
    dp.add_handler(MessageHandler(Filters.regex('🤖 Start the Bot'), slash_start))
    dp.add_handler(MessageHandler(Filters.regex('🥴ultra bored'), beta))
    dp.add_handler(MessageHandler(Filters.regex('⁉️ Help'), help_cmd))
    dp.add_handler(MessageHandler(Filters.regex('thanks'), thak))
    dp.add_handler(MessageHandler(Filters.regex('thank you'), thak))
    dp.add_handler(MessageHandler(Filters.regex('Thanks'), thak))
    dp.add_handler(MessageHandler(Filters.regex('Thank you'), thak))
    # comment the following line to disable webhook (for local testing)
    updater.start_webhook(listen="0.0.0.0",
                      port=PORT12,
                      url_path=token,
                      webhook_url=app_url + token) # change this with your heroku app name
    #updater.start_polling() # uncomment this line for local testing
    updater.idle()
    print("received SIGTERM")
    o.flush()
    # Any code here will be executed before exit


main()



