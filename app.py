S=ValueError
I=int
H=Exception
F=print
B=str
import telebot as T
from telebot import types as G
import requests as J,httpx,random as C,string as U,uuid
from datetime import datetime as O
from user_agent import generate_user_agent as V
from cfonts import render as P
import os,time
from flask import Flask, request

W='8730065471:AAFFqTLLSmlQI_n7ROv5Q8UStQA2spHj9Fc'
A=T.TeleBot(W)

R={}
K=5612494162
D=set()
def a(user):
    try:
        headers={'user-agent':V(),'x-ig-app-id':'936619743392459','x-requested-with':'XMLHttpRequest','x-instagram-ajax':'1032099486','x-csrftoken':'missing','x-asbd-id':'359341','origin':'https://www.instagram.com','referer':'https://www.instagram.com/accounts/password/reset/','accept-language':'en-US','priority':'u=1, i'}
        response=httpx.Client(http2=True,headers=headers,timeout=20).post('https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/',data={'email_or_username':user})
        data=response.json()
        contact=data.get('contact_point','Email Not Found')
        return f"Reset Sent: {contact} | By @Beasteren"
    except Exception as e:
        return f"Error: {B(e)}"

def b(new_password):
    device_id=f"android-{''.join(C.choices(U.hexdigits.lower(),k=16))}"
    user_agent=f"Instagram 394.0.0.46.81 Android ({C.choice(['28/9','29/10','30/11','31/12'])}; {C.choice(['240dpi','320dpi','480dpi'])}; {C.choice(['720x1280','1080x1920','1440x2560'])}; {C.choice(['samsung','xiaomi','huawei','oneplus','google'])}; {C.choice(['SM-G975F','Mi-9T','P30-Pro','ONEPLUS-A6003','Pixel-4'])}; intel; en_US; {C.randint(100000000,999999999)})"
    uuid_val=B(uuid.uuid4())
    timestamp=I(O.now().timestamp())
    pwd_hash=f"#PWD_INSTAGRAM:0:{timestamp}:{new_password}"
    return device_id,user_agent,uuid_val,pwd_hash

def L(m='',a=''):
    return{'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','X-Bloks-Version-Id':'e061cacfa956f06869fc2b678270bef1583d2480bf51f508321e64cfb5cc12bd','X-Mid':m,'User-Agent':a,'Content-Length':'9481'}

def c(link,custom_pw):
    try:
        device_id,user_agent,uuid_val,pwd_hash=b(custom_pw)
        response=J.post('https://i.instagram.com/api/v1/accounts/password_reset/',headers=L(a=user_agent),data={'source':'one_click_login_email','uidb36':link.split('uidb36=')[1].split('&token=')[0],'device_id':device_id,'token':link.split('&token=')[1].split(':')[0],'waterfall_id':uuid_val},timeout=60)
        data=response.json()
        new_pwd_hash=f"#PWD_INSTAGRAM:0:{I(O.now().timestamp())}:{custom_pw}"
        challenge1=J.post('https://i.instagram.com/api/v1/bloks/apps/com.instagram.challenge.navigation.take_challenge/',headers=L(response.headers.get('Ig-Set-X-Mid'),user_agent),data={'user_id':B(data.get('user_id')),'cni':B(data.get('cni')),'nonce_code':B(data.get('nonce_code')),'bk_client_context':'{"bloks_version":"e061cacfa956f06869fc2b678270bef1583d2480bf51f508321e64cfb5cc12bd","styles_id":"instagram"}','challenge_context':B(data.get('challenge_context')),'bloks_versioning_id':'e061cacfa956f06869fc2b678270bef1583d2480bf51f508321e64cfb5cc12bd','get_challenge':'true'},timeout=60)
        final=J.post('https://i.instagram.com/api/v1/bloks/apps/com.instagram.challenge.navigation.take_challenge/',headers=L(response.headers.get('Ig-Set-X-Mid'),user_agent),data={'is_caa':'False','source':'','uidb36':'','error_state':{'type_name':'str','index':0,'state_id':1048583541},'afv':'','cni':B(data.get('cni')),'token':'','has_follow_up_screens':'0','bk_client_context':{'bloks_version':'e061cacfa956f06869fc2b678270bef1583d2480bf51f508321e64cfb5cc12bd','styles_id':'instagram'},'challenge_context':challenge1.text.replace('\\','').split(f'(bk.action.i64.Const, {data.get("cni")}), "')[1].split('", (bk.action.bool.Const, false)))')[0],'bloks_versioning_id':'e061cacfa956f06869fc2b678270bef1583d2480bf51f508321e64cfb5cc12bd','enc_new_password1':new_pwd_hash,'enc_new_password2':new_pwd_hash},timeout=60).ok
        return final
    except Exception:
        return False

def is_authorized(chat_id):
    return chat_id in D or chat_id==K

def is_admin(chat_id):
    return chat_id==K

@A.message_handler(commands=['accessgrant'])
def accessgrant(message):
    if not is_admin(message.chat.id):
        A.reply_to(message,'❌ Only admin can use this command')
        return
    try:
        args=message.text.split()
        if len(args)!=2:
            A.reply_to(message,'Usage: /accessgrant <chat_id>')
            return
        user_id=I(args[1])
        D.add(user_id)
        A.reply_to(message,f"✅ Access granted to user: {user_id}")
        F(f"Access granted to {user_id} by admin {message.chat.id}")
    except ValueError:
        A.reply_to(message,'❌ Invalid chat ID. Please provide a valid number')
    except Exception as e:
        A.reply_to(message,f"❌ Error: {B(e)}")

@A.message_handler(commands=['accessrevoke'])
def accessrevoke(message):
    if not is_admin(message.chat.id):
        A.reply_to(message,'❌ Only admin can use this command')
        return
    try:
        args=message.text.split()
        if len(args)!=2:
            A.reply_to(message,'Usage: /accessrevoke <chat_id>')
            return
        user_id=I(args[1])
        if user_id in D:
            D.remove(user_id)
            A.reply_to(message,f"✅ Access revoked for user: {user_id}")
            F(f"Access revoked from {user_id} by admin {message.chat.id}")
        else:
            A.reply_to(message,f"❌ User {user_id} is not authorized")
    except ValueError:
        A.reply_to(message,'❌ Invalid chat ID. Please provide a valid number')
    except Exception as e:
        A.reply_to(message,f"❌ Error: {B(e)}")

@A.message_handler(commands=['listusers'])
def listusers(message):
    if not is_admin(message.chat.id):
        A.reply_to(message,'❌ Only admin can use this command')
        return
    if D:
        users='\n'.join([B(u)for u in D])
        A.reply_to(message,f"✅ Authorized Users:\n{users}")
    else:
        A.reply_to(message,'📝 No authorized users yet')

@A.message_handler(commands=['start'])
def start(message):
    F('\x1b[0;91m \n\n',P('PAID',colors=['red','red'],align='center',space=False),P('WORK',colors=['red','red'],align='center'))
    if not is_authorized(message.chat.id):
        A.reply_to(message,'❌ You are not authorized to use this bot. Please contact admin')
        return
    markup=G.InlineKeyboardMarkup(row_width=2)
    btn1=G.InlineKeyboardButton('📧 Send Reset Link',callback_data='send_reset')
    btn2=G.InlineKeyboardButton('🔗 Link to Password',callback_data='link_to_pass')
    markup.add(btn1,btn2)
    text="\nYou Can Send Reset Link And Can Change Your Password without login... by @Beasteren\n"
    A.send_message(message.chat.id,text,reply_markup=markup,parse_mode='HTML')

@A.callback_query_handler(func=lambda call:True)
def callback(call):
    if not is_authorized(call.message.chat.id):
        A.answer_callback_query(call.id,'❌ You are not authorized')
        A.send_message(call.message.chat.id,'❌ You are not authorized to use this bot. Please contact admin')
        return
    if call.data=='send_reset':
        msg=A.send_message(call.message.chat.id,"Enter Email or Username:")
        A.register_next_step_handler(msg,handle_reset)
    elif call.data=='link_to_pass':
        msg=A.send_message(call.message.chat.id,"Enter Your Password Reset Link:")
        A.register_next_step_handler(msg,handle_link)

def handle_reset(message):
    if not is_authorized(message.chat.id):
        A.reply_to(message,'❌ You are not authorized to use this bot')
        return
    username=message.text
    result=a(username)
    # Remove any undefined variables
    clean_result=result
    A.send_message(message.chat.id,f"Result:\n{clean_result}")
    show_menu(message.chat.id)

def handle_link(message):
    if not is_authorized(message.chat.id):
        A.reply_to(message,'❌ You are not authorized to use this bot')
        return
    R[message.chat.id]={'link':message.text}
    msg=A.send_message(message.chat.id,"Enter Your Password:")
    A.register_next_step_handler(msg,handle_password)

def handle_password(message):
    if not is_authorized(message.chat.id):
        A.reply_to(message,'❌ You are not authorized to use this bot')
        return
    chat_id=message.chat.id
    password=message.text
    link=R[chat_id]['link']
    success=c(link,password)
    if success:
        text=f"\nPassword Changed Successfully! New Password: {password}\n"
        A.send_message(chat_id,text)
    else:
        A.send_message(chat_id,"Failed To Reset")
    A.send_message(chat_id,'\n-- @Beasteren')
    show_menu(chat_id)

def show_menu(chat_id):
    if not is_authorized(chat_id):
        return
    markup=G.InlineKeyboardMarkup(row_width=2)
    btn1=G.InlineKeyboardButton('📧 Send Reset Link',callback_data='send_reset')
    btn2=G.InlineKeyboardButton('🔗 Link to Password',callback_data='link_to_pass')
    markup.add(btn1,btn2)
    text="\nSend Reset Instagram Email/Username\nReset Via Link\n"
    A.send_message(chat_id,text,reply_markup=markup,parse_mode='HTML')

@A.message_handler(commands=['menu'])
def menu(message):
    if not is_authorized(message.chat.id):
        A.reply_to(message,'❌ You are not authorized to use this bot')
        return
    show_menu(message.chat.id)

# Flask app for Vercel
web_app = Flask(__name__)

@web_app.route("/", methods=['POST', 'GET'])
def webhook():
    if request.method == 'POST':
        try:
            json_str = request.get_data().decode('UTF-8')
            update = T.types.Update.de_json(json_str)
            A.process_new_updates([update])
            return "OK", 200
        except Exception as e:
            return f"Error: {e}", 200
    return "Bot is running. Use Telegram bot", 200

@web_app.route("/health", methods=['GET'])
def health():
    return "OK", 200

if __name__ == "__main__":
    F(f"Bot started...")
    F(f"Developed By @Beasteren")
    F(f"Admin ID: {K}")
    A.infinity_polling()
