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
W='8730065471:AAFFqTLLSmlQI_n7ROv5Q8UStQA2spHj9Fc'
A=T.TeleBot(W)

R={}
K=5612494162
D=set()
def a(user):
	try:A={'user-agent':V(),'x-ig-app-id':'936619743392459','x-requested-with':'XMLHttpRequest','x-instagram-ajax':'1032099486','x-csrftoken':'missing','x-asbd-id':'359341','origin':'https://www.instagram.com','referer':'https://www.instagram.com/accounts/password/reset/','accept-language':'en-US','priority':'u=1, i'};C=httpx.Client(http2=True,headers=A,timeout=20).post('https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/',data={'email_or_username':user});D=C.json();E=D.get('contact_point','Email Not Found');return f"Reset Sent: {E} |     By @Beasteren"
	except H as F:return f"Even: {B(F)}{Q}"
def b(new_password):A=f"android-{''.join(C.choices(U.hexdigits.lower(),k=16))}";D=f"Instagram 394.0.0.46.81 Android ({C.choice(['28/9','29/10','30/11','31/12'])}; {C.choice(['240dpi','320dpi','480dpi'])}; {C.choice(['720x1280','1080x1920','1440x2560'])}; {C.choice(['samsung','xiaomi','huawei','oneplus','google'])}; {C.choice(['SM-G975F','Mi-9T','P30-Pro','ONEPLUS-A6003','Pixel-4'])}; intel; en_US; {C.randint(100000000,999999999)})";E=B(uuid.uuid4());F=I(O.now().timestamp());G=f"#PWD_INSTAGRAM:0:{F}:{new_password}";return A,D,E,G
def L(m='',a=''):return{'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','X-Bloks-Version-Id':'e061cacfa956f06869fc2b678270bef1583d2480bf51f508321e64cfb5cc12bd','X-Mid':m,'User-Agent':a,'Content-Length':'9481'}
def c(link,custom_pw):
	E=custom_pw
	try:G,C,K,P=b(E);D=J.post('https://i.instagram.com/api/v1/accounts/password_reset/',headers=L(a=C),data={'source':'one_click_login_email','uidb36':link.split('uidb36=')[1].split('&token=')[0],'device_id':G,'token':link.split('&token=')[1].split(':')[0],'waterfall_id':K},timeout=60);A=D.json();F=f"#PWD_INSTAGRAM:0:{I(O.now().timestamp())}:{E}";M=J.post('https://i.instagram.com/api/v1/bloks/apps/com.instagram.challenge.navigation.take_challenge/',headers=L(D.headers.get('Ig-Set-X-Mid'),C),data={'user_id':B(A.get('user_id')),'cni':B(A.get('cni')),'nonce_code':B(A.get('nonce_code')),'bk_client_context':'{"bloks_version":"e061cacfa956f06869fc2b678270bef1583d2480bf51f508321e64cfb5cc12bd","styles_id":"instagram"}','challenge_context':B(A.get('challenge_context')),'bloks_versioning_id':'e061cacfa956f06869fc2b678270bef1583d2480bf51f508321e64cfb5cc12bd','get_challenge':'true'},timeout=60);N=J.post('https://i.instagram.com/api/v1/bloks/apps/com.instagram.challenge.navigation.take_challenge/',headers=L(D.headers.get('Ig-Set-X-Mid'),C),data={'is_caa':'False','source':'','uidb36':'','error_state':{'type_name':'str','index':0,'state_id':1048583541},'afv':'','cni':B(A.get('cni')),'token':'','has_follow_up_screens':'0','bk_client_context':{'bloks_version':'e061cacfa956f06869fc2b678270bef1583d2480bf51f508321e64cfb5cc12bd','styles_id':'instagram'},'challenge_context':M.text.replace('\\','').split(f'(bk.action.i64.Const, {A.get("cni")}), "')[1].split('", (bk.action.bool.Const, false)))')[0],'bloks_versioning_id':'e061cacfa956f06869fc2b678270bef1583d2480bf51f508321e64cfb5cc12bd','enc_new_password1':F,'enc_new_password2':F},timeout=60).ok;return N
	except H as Q:return False
def E(chat_id):A=chat_id;return A in D or A==K
def M(chat_id):return chat_id==K
@A.message_handler(commands=['accessgrant'])
def A3(message):
	C=message
	if not M(C.chat.id):A.reply_to(C,'❌ Only admin can use this command');return
	try:
		G=C.text.split()
		if len(G)!=2:A.reply_to(C,'Usage: /accessgrant <chat_id>');return
		E=I(G[1]);D.add(E);A.reply_to(C,f"✅ Access granted to user: {E}");F(f"Access granted to {E} by admin {C.chat.id}")
	except S:A.reply_to(C,'❌ Invalid chat ID. Please provide a valid number')
	except H as J:A.reply_to(C,f"❌ Error: {B(J)}")
@A.message_handler(commands=['accessrevoke'])
def A4(message):
	C=message
	if not M(C.chat.id):A.reply_to(C,'❌ Only admin can use this command');return
	try:
		G=C.text.split()
		if len(G)!=2:A.reply_to(C,'Usage: /accessrevoke <chat_id>');return
		E=I(G[1])
		if E in D:D.remove(E);A.reply_to(C,f"✅ Access revoked for user: {E}");F(f"Access revoked from {E} by admin {C.chat.id}")
		else:A.reply_to(C,f"❌ User {E} is not authorized")
	except S:A.reply_to(C,'❌ Invalid chat ID. Please provide a valid number')
	except H as J:A.reply_to(C,f"❌ Error: {B(J)}")
@A.message_handler(commands=['listusers'])
def A5(message):
	C=message
	if not M(C.chat.id):A.reply_to(C,'❌ Only admin can use this command');return
	if D:E='\n'.join([B(A)for A in D]);A.reply_to(C,f"✅ Authorized Users:\n{E}")
	else:A.reply_to(C,'📝 No authorized users yet')
@A.message_handler(commands=['start'])
def A6(message):
	B=message;F('\x1b[0;91m \n\n',P('PAID',colors=['red','red'],align='center',space=False),P('WORK',colors=['red','red'],align='center'))
	if not E(B.chat.id):A.reply_to(B,'❌ You are not authorized to use this bot. Please contact admin');return
	C=G.InlineKeyboardMarkup(row_width=2);D=G.InlineKeyboardButton('📧 Send Reset Link',callback_data='send_reset');H=G.InlineKeyboardButton('🔗 Link to Password',callback_data='link_to_pass');C.add(D,H);I=f"\nYou Can Send Reset Link And Can Chnage Your Password withoud login... by @Beasteren\n    ";A.send_message(B.chat.id,I,reply_markup=C,parse_mode='HTML')
@A.callback_query_handler(func=lambda call:True)
def A7(call):
	B=call
	if not E(B.message.chat.id):A.answer_callback_query(B.id,'❌ You are not authorized');A.send_message(B.message.chat.id,'❌ You are not authorized to use this bot. Please contact admin');return
	if B.data=='send_reset':C=A.send_message(B.message.chat.id,f"Enter Email or Username:");A.register_next_step_handler(C,d)
	elif B.data=='link_to_pass':C=A.send_message(B.message.chat.id,f"Enter Your Password Reset Link:");A.register_next_step_handler(C,e)
def d(message):
	B=message
	if not E(B.chat.id):A.reply_to(B,'❌ You are not authorized to use this bot');return
	C=B.text;D=a(C);F=D.replace(X,'').replace(Y,'').replace(Z,'').replace(Q,'');A.send_message(B.chat.id,f"Result:\n{F}");N(B.chat.id)
def e(message):
	B=message
	if not E(B.chat.id):A.reply_to(B,'❌ You are not authorized to use this bot');return
	R[B.chat.id]={'link':B.text};C=A.send_message(B.chat.id,f"Enter Your Password:");A.register_next_step_handler(C,f)
def f(message):
	C=message
	if not E(C.chat.id):A.reply_to(C,'❌ You are not authorized to use this bot');return
	B=C.chat.id;D=C.text;F=R[B]['link'];G=c(F,D)
	if G:H=f"\n        Password Changed Successfully      New Password Is : {D}\n        ";A.send_message(B,H)
	else:A.send_message(B,f"Failed To Reset")
	A.send_message(B,'\n-- @Beasteren');N(B)
def N(chat_id):
	B=chat_id
	if not E(B):return
	C=G.InlineKeyboardMarkup(row_width=2);D=G.InlineKeyboardButton('📧 Send Reset Link',callback_data='send_reset');F=G.InlineKeyboardButton('🔗 Link to Password',callback_data='link_to_pass');C.add(D,F);H=f"\n    Send Reset Instagram Email/Username\n  Reset Via Link\n    ";A.send_message(B,H,reply_markup=C,parse_mode='HTML')
@A.message_handler(commands=['menu'])
def A8(message):
	B=message
	if not E(B.chat.id):A.reply_to(B,'❌ You are not authorized to use this bot');return
	N(B.chat.id)
F(f"Bot started...")
F(f"Developed By @Beasteren")
F(f"Admin ID: {K}")
A.infinity_polling()
