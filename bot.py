# ==============================================================================
# 👑 रविंद्र शर्मा साइबर एक्सपर्ट हेल्पलाइन - JARVIS MASTER TITAN AI
# ==============================================================================
# Founder & Cyber Security Specialist: Ravinder Sharma (Bilaspur / Rampur, UP)
# Verified Helplines: +91 9258294556 | +91 7500078349
# ==============================================================================

import io
import re
import os
import json
import time
import glob
import datetime
import urllib.parse
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import requests
from PIL import Image, ImageDraw, ImageFont
import telebot
from telebot import types

# ------------------------------------------------------------------------------
# 1. 24/7 RENDER SERVER KEEP-ALIVE ENGINE
# ------------------------------------------------------------------------------
class MasterTitanServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"JARVIS MASTER TITAN ENGINE 24/7 RUNNING FOR RAVINDER SHARMA")

    def log_message(self, format, *args):
        return

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), MasterTitanServer)
    server.serve_forever()

def auto_pinger():
    time.sleep(15)
    port = os.environ.get("PORT", "10000")
    while True:
        try:
            requests.get(f"http://127.0.0.1:{port}/", timeout=3)
        except Exception:
            pass
        time.sleep(300)

threading.Thread(target=run_server, daemon=True).start()
threading.Thread(target=auto_pinger, daemon=True).start()

# ------------------------------------------------------------------------------
# 2. NEW BOT CREDENTIALS & CONSTANTS
# ------------------------------------------------------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8029651365:AAFBS-wviNLKfbDeBWXXuucTBAEFauyQBig")
bot = telebot.TeleBot(BOT_TOKEN, threaded=True, num_threads=40)

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "AQ.Ab8RN6Kp5LhnlPIkVMQEagqfpCbRBivpBS0b-535ltVrn55B2w")
WEATHER_API_KEY = "7c660f522625b9c3cf6f2357d5beeb69"

OWNER_IDS = [8843460945]
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "@123hack@123hack")
CREATOR_NAME = "रविंद्र शर्मा (Ravinder Sharma)"
PRIMARY_PHONE = "9258294556"
SECONDARY_PHONE = "7500078349"
OFFICIAL_EMAIL = "ravindershrma008@gmail.com"

OFFICIAL_WEBSITE_URL = "https://ravinder-shrma-cyber-tech-expert.netlify.app/"
TOOLS_HUB_URL = "https://cybertools-hub-online.netlify.app/"
GROUP_LINK = "https://t.me/Indianethicalhackers"
TG_CHANNEL_URL = "https://t.me/ravinder_shrma_cyber_expert"
WA_CHANNEL_1 = "https://whatsapp.com/channel/0029Vb8NBEJJENy74M53yK2w"
WA_CHANNEL_2 = "https://whatsapp.com/channel/0029VbDj0rnAzNbsijceS02w"
YOUTUBE_URL = "https://www.youtube.com/@RavinderShrmaCyberexpert"
RADHA_AI_URL = "https://ai.studio/apps/5276fdd5-a035-41d5-b837-e3ac373695c6?fullscreenApplet=true"

LANG_FILE = "user_languages.json"
USER_LANG_CACHE = {}

def init_user_languages():
    global USER_LANG_CACHE
    if os.path.exists(LANG_FILE):
        try:
            with open(LANG_FILE, "r", encoding="utf-8") as f:
                USER_LANG_CACHE = json.load(f)
        except Exception:
            USER_LANG_CACHE = {}
    else:
        USER_LANG_CACHE = {}

init_user_languages()

def set_user_lang(user_id, lang_code):
    global USER_LANG_CACHE
    USER_LANG_CACHE[str(user_id)] = lang_code
    try:
        with open(LANG_FILE, "w", encoding="utf-8") as f:
            json.dump(USER_LANG_CACHE, f, ensure_ascii=False, indent=2)
    except Exception:
        pass

def get_user_lang(user_id):
    global USER_LANG_CACHE
    return USER_LANG_CACHE.get(str(user_id), "hi")

banner_rotation_counter = 0

authenticated_admins = set()
admin_login_queue = {}
admin_active_panels = {}
reminder_tasks = []
custom_projects = []
private_dm_history = []
active_crime_reports = {}

chat_active_button_messages = {}
user_link_warnings = {}

custom_admin_tools = [
    {"name": "🌐 Live Online Tools Hub", "desc": "IP, URL, Hash, and Phishing Scanner Suite", "link": TOOLS_HUB_URL}
]

http_session = requests.Session()

def get_custom_wa_url(user_name, phone_number, intent="General Support"):
    msg = (
        f"Namaste Ravinder Sharma Sir,\n"
        f"Mera Telegram Name: {user_name}\n"
        f"Subject: {intent}\n\n"
        f"Mujhe Cyber Crime / Helpline ke regarding direct guidance chahiye."
    )
    return f"https://wa.me/91{phone_number}?text={urllib.parse.quote(msg)}"

def get_radha_wa_url(user_name):
    msg = (
        f"Namaste Ravinder Sharma Sir,\n"
        f"Mera Telegram Name: {user_name}\n"
        f"Subject: Help regarding Radha AI Assistant\n\n"
        f"Mujhe Radha AI ko use karne ya browser par start karne me aapki thodi guidance chahiye."
    )
    return f"https://wa.me/91{PRIMARY_PHONE}?text={urllib.parse.quote(msg)}"

# ------------------------------------------------------------------------------
# 3. 24-HOUR PRIVATE DM AUTO-CLEAN ENGINE
# ------------------------------------------------------------------------------
def private_dm_cleaner_worker():
    while True:
        now = time.time()
        for msg in list(private_dm_history):
            if now - msg["time"] >= 86400:
                try:
                    bot.delete_message(msg["chat_id"], msg["message_id"])
                except Exception:
                    pass
                if msg in private_dm_history:
                    private_dm_history.remove(msg)
        time.sleep(60)

threading.Thread(target=private_dm_cleaner_worker, daemon=True).start()

# ------------------------------------------------------------------------------
# 4. VIP BANNER GENERATOR
# ------------------------------------------------------------------------------
def get_banner_image():
    global banner_rotation_counter
    targets = ["banner1", "banner2", "banner3", "banner4", "banner5", "welcome_banner"]
    found = []

    for name in targets:
        for ext in [".jpg", ".png", ".jpeg"]:
            fn = name + ext
            if os.path.exists(fn):
                found.append(fn)
                break

    if not found:
        for f in glob.glob("*.jpg") + glob.glob("*.png"):
            if "welcome_banner_base" not in f.lower():
                found.append(f)

    if not found:
        return None

    chosen = found[banner_rotation_counter % len(found)]
    banner_rotation_counter += 1
    return Image.open(chosen).convert("RGB")

def generate_vip_banner(first_name, user_photo_bytes=None):
    try:
        banner = get_banner_image()
        if banner is None:
            return None

        banner = banner.resize((1024, 572), Image.Resampling.LANCZOS)
        draw = ImageDraw.Draw(banner)
        
        cx, cy = 144, 318
        radius = 102

        draw.ellipse((cx - 108, cy - 108, cx + 108, cy + 108), fill=(8, 8, 12))

        if user_photo_bytes:
            try:
                raw_avatar = Image.open(io.BytesIO(user_photo_bytes)).convert("RGB")
                avatar = raw_avatar.resize((radius * 2, radius * 2), Image.Resampling.LANCZOS)
                
                mask = Image.new("L", (radius * 4, radius * 4), 0)
                mask_draw = ImageDraw.Draw(mask)
                mask_draw.ellipse((0, 0, radius * 4, radius * 4), fill=255)
                mask = mask.resize((radius * 2, radius * 2), Image.Resampling.LANCZOS)
                
                banner.paste(avatar, (cx - radius, cy - radius), mask)
            except Exception:
                pass

        draw.ellipse((cx - radius, cy - radius, cx + radius, cy + radius), outline=(255, 60, 40), width=4)
        draw.ellipse((cx - radius - 2, cy - radius - 2, cx + radius + 2, cy + radius + 2), outline=(180, 20, 20), width=2)

        draw.rectangle([(265, 212), (590, 252)], fill=(9, 8, 14))

        clean_first_name = first_name.strip()
        font_size = 40 if len(clean_first_name) <= 10 else 32

        font = None
        for fp in [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf",
            "C:\\Windows\\Fonts\\arialbd.ttf"
        ]:
            if os.path.exists(fp):
                try:
                    font = ImageFont.truetype(fp, font_size)
                    break
                except Exception:
                    pass
        if font is None:
            font = ImageFont.load_default()

        draw.text((269, 215), clean_first_name, fill=(0, 0, 0), font=font)
        draw.text((268, 214), clean_first_name, fill=(255, 255, 255), font=font)

        out = io.BytesIO()
        banner.save(out, format="JPEG", quality=100, subsampling=0)
        out.seek(0)
        out.name = "vip_banner.jpg"
        return out
    except Exception as e:
        print(f"Banner error: {e}")
        return None

# ------------------------------------------------------------------------------
# 5. JARVIS SMART AI & WEATHER ENGINE (FOR SLASH COMMANDS)
# ------------------------------------------------------------------------------
def ask_gemini_ai(prompt_text, user_name="User", lang="hi"):
    lang_names = {
        "hi": "Hindi", "en": "English", "mr": "Marathi", "es": "Spanish",
        "fr": "French", "de": "German", "ru": "Russian", "ar": "Arabic",
        "pt": "Portuguese", "bn": "Bengali", "ta": "Tamil", "te": "Telugu", "gu": "Gujarati"
    }
    target_lang = lang_names.get(lang, "Hindi")

    system_instruction = (
        f"You are JARVIS, an elite, witty, highly intelligent AI system created by Ravinder Sharma "
        f"(Certified Cyber Security Specialist, Ethical Hacker & Developer from Bilaspur / Rampur, UP, India). "
        f"CRITICAL: Answer in {target_lang} language only. "
        f"When asked about who created you, your developer, owner, or this bot/channel, praise Ravinder Sharma with deep respect. "
        f"Answer the user's question with high accuracy, helpfulness, and smart personality. User's name is {user_name}."
    )

    if GEMINI_API_KEY and ("AIzaSy" in GEMINI_API_KEY or len(GEMINI_API_KEY) > 25):
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
            payload = {
                "contents": [
                    {"role": "user", "parts": [{"text": f"{system_instruction}\n\nUser Question: {prompt_text}"}]}
                ],
                "generationConfig": {"temperature": 0.7, "maxOutputTokens": 600}
            }
            res = http_session.post(url, json=payload, timeout=8)
            if res.status_code == 200:
                data = res.json()
                candidates = data.get("candidates", [])
                if candidates:
                    parts = candidates[0].get("content", {}).get("parts", [])
                    if parts:
                        return parts[0].get("text", "").strip()
        except Exception:
            pass

    q = prompt_text.lower()
    if any(w in q for w in ["developer", "kisne banaya", "owner", "creator", "founder", "kon banaya"]):
        return (
            f"मुझे <b>{CREATOR_NAME}</b> (सर्टिफाइड साइबर सिक्योरिटी स्पेशलिस्ट, बिलासपुर/रामपुर, यूपी) ने बनाया है! 👨‍💻\n"
            f"रविंद्र शर्मा सर एथिकल हैकिंग, डेटा रिकवरी और एडवांस AI एजेंट्स के विशेषज्ञ हैं। उनकी ऑफिशियल वेबसाइट: {OFFICIAL_WEBSITE_URL}"
        )

    return f"नमस्ते {user_name}! मैं आपकी बात पूरी तरह समझ गया। किसी भी साइबर सुरक्षा, टूल्स या अन्य सवाल के लिए मैं 24/7 तैयार हूँ।"

def fetch_weather_report(city_name, lang="hi"):
    try:
        clean_city = city_name.strip()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={urllib.parse.quote(clean_city)}&appid={WEATHER_API_KEY}&units=metric"
        res = http_session.get(url, timeout=5)
        if res.status_code == 200:
            d = res.json()
            temp = d["main"]["temp"]
            feels = d["main"]["feels_like"]
            desc = d["weather"][0]["description"].title()
            humidity = d["main"]["humidity"]
            wind = d["wind"]["speed"]
            city_proper = d["name"]
            country = d["sys"]["country"]

            return (
                f"🌤️ <b>लाइव मौसम रिपोर्ट: {city_proper}, {country}</b>\n"
                f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
                f"🌡️ <b>तापमान:</b> {temp}°C (महसूस: {feels}°C)\n"
                f"☁️ <b>मौसम:</b> {desc}\n"
                f"💧 <b>नमी (Humidity):</b> {humidity}%\n"
                f"💨 <b>हवा की गति:</b> {wind} m/s\n\n"
                f"👨‍💻 <i>JARVIS Weather Intelligence द्वारा जारी।</i>"
            )
        else:
            return f"⚠️ <b>'{city_name}'</b> शहर का मौसम नहीं मिल पाया। कृपया सही शहर का नाम लिखें।"
    except Exception as e:
        return f"Weather report fetch karne me dikkat aayi: {e}"

# ------------------------------------------------------------------------------
# 6. COMPACT MASTER BUTTONS & CLEANUP ENGINE
# ------------------------------------------------------------------------------
def build_master_markup(user_name, lang="hi"):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("🌐 Official Website", url=OFFICIAL_WEBSITE_URL),
        types.InlineKeyboardButton("📞 Contact", callback_data="menu_contact"),
        types.InlineKeyboardButton("💖 Radha AI", callback_data="menu_radha_ai"),
        types.InlineKeyboardButton("🚨 Report Fraud", callback_data="report_crime"),
        types.InlineKeyboardButton("🔍 Tools", callback_data="menu_tools"),
        types.InlineKeyboardButton("📲 Socials", callback_data="menu_social"),
        types.InlineKeyboardButton("📜 Rules", callback_data="menu_rules"),
        types.InlineKeyboardButton("🌐 Language (12)", callback_data="menu_languages")
    )
    for proj in custom_projects:
        markup.add(types.InlineKeyboardButton(f"⭐ {proj['title']}", url=proj['url']))

    return markup

def clear_previous_buttons_in_chat(chat_id):
    if chat_id in chat_active_button_messages:
        old_mids = list(chat_active_button_messages[chat_id])
        for old_id in old_mids:
            try:
                bot.edit_message_reply_markup(chat_id, old_id, reply_markup=None)
            except Exception:
                pass
        chat_active_button_messages[chat_id] = []

def track_active_button_message(chat_id, message_id):
    if chat_id not in chat_active_button_messages:
        chat_active_button_messages[chat_id] = []
    chat_active_button_messages[chat_id].append(message_id)

def auto_vanish_welcome_message(chat_id, message_id, delay_seconds=60):
    def vanish_worker():
        time.sleep(delay_seconds)
        try:
            bot.delete_message(chat_id, message_id)
        except Exception:
            pass
    threading.Thread(target=vanish_worker, daemon=True).start()

# ------------------------------------------------------------------------------
# 7. GROUP WELCOME HANDLER (SHORT & SIMPLE + RULES BUTTON)
# ------------------------------------------------------------------------------
@bot.message_handler(content_types=['new_chat_members'])
def on_user_joins_group(message):
    chat_id = message.chat.id
    clear_previous_buttons_in_chat(chat_id)

    for new_user in message.new_chat_members:
        first_name = new_user.first_name or "Member"
        full_name = f"{new_user.first_name or ''} {new_user.last_name or ''}".strip() or first_name

        code = (new_user.language_code or "").lower()
        detected_lang = "mr" if code.startswith("mr") else ("hi" if code.startswith("hi") else "en")
        set_user_lang(new_user.id, detected_lang)

        photo_bytes = None
        try:
            photos = bot.get_user_profile_photos(new_user.id, limit=1)
            if photos and photos.total_count > 0:
                f_id = photos.photos[0][0].file_id
                f_info = bot.get_file(f_id)
                photo_bytes = http_session.get(f"https://api.telegram.org/file/bot{BOT_TOKEN}/{f_info.file_path}", timeout=3).content
        except Exception:
            pass

        banner = generate_vip_banner(first_name, photo_bytes)

        welcome_markup = types.InlineKeyboardMarkup(row_width=1)
        welcome_markup.add(
            types.InlineKeyboardButton("📜 ग्रुप के रूल्स देखें (Rules)", callback_data="menu_rules")
        )

        caption = f"👑 वेलकम <b>{full_name}</b>, आप हमारे ऑफिशियल ग्रुप में जॉइन हो गए हैं।"

        sent_msg = None
        try:
            if banner:
                sent_msg = bot.send_photo(chat_id, banner, caption=caption, parse_mode="HTML", reply_markup=welcome_markup)
            else:
                sent_msg = bot.send_message(chat_id, caption, parse_mode="HTML", reply_markup=welcome_markup)
        except Exception:
            sent_msg = bot.send_message(chat_id, caption, parse_mode="HTML", reply_markup=welcome_markup)

        if sent_msg:
            track_active_button_message(chat_id, sent_msg.message_id)
            auto_vanish_welcome_message(chat_id, sent_msg.message_id, delay_seconds=60)

# ------------------------------------------------------------------------------
# 8. /start COMMAND
# ------------------------------------------------------------------------------
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    first_name = message.from_user.first_name or "Member"
    full_name = f"{message.from_user.first_name or ''} {message.from_user.last_name or ''}".strip() or first_name

    clear_previous_buttons_in_chat(chat_id)

    lang = get_user_lang(user_id)
    markup = build_master_markup(first_name, lang)

    text_menu = (
        f"👑 <b>नमस्ते {full_name}!</b> 👑\n\n"
        f"🤖 <b>रविंद्र शर्मा साइबर टेक एक्सपर्ट हेल्प डेस्क</b> में आपका स्वागत है।\n\n"
        f"👇 <i>Radha AI का उपयोग करने या सहायता के लिए नीचे दिए गए बटन चुनें:</i>"
    )

    sent = bot.send_message(chat_id, text_menu, parse_mode="HTML", reply_markup=markup)
    if sent:
        track_active_button_message(chat_id, sent.message_id)

    if message.chat.type == 'private' and sent:
        private_dm_history.append({"chat_id": chat_id, "message_id": sent.message_id, "time": time.time()})

# ------------------------------------------------------------------------------
# 9. GROUP SECURITY SHIELD (3-STRIKE SOFT KICK)
# ------------------------------------------------------------------------------
LINK_REGEX = re.compile(r'(https?://|www\.|t\.me/|telegram\.me/|bit\.ly/|joinchat|wa\.me/)', re.IGNORECASE)
BAD_WORDS = ['madarchod', 'bhosdike', 'bhenchod', 'chutiya', 'gandu', 'randi', 'harami', 'lode', 'mc', 'bc', 'fuck']

@bot.message_handler(content_types=['voice', 'audio'])
def handle_voice_shield(message):
    user_id = message.from_user.id
    if user_id in OWNER_IDS or user_id in authenticated_admins:
        return

    if message.chat.type in ['group', 'supergroup']:
        try:
            bot.delete_message(message.chat.id, message.message_id)
            user_mention = message.from_user.first_name or "Member"
            bot.send_message(
                message.chat.id,
                f"🚨 <b>सुरक्षा एक्शन:</b> 👤 <b>{user_mention}</b> को ग्रुप में अनधिकृत वॉइस नोट भेजने की अनुमति नहीं है।",
                parse_mode="HTML"
            )
        except Exception:
            pass

@bot.message_handler(func=lambda msg: msg.text and (LINK_REGEX.search(msg.text) or any(bw in msg.text.lower() for bw in BAD_WORDS)), content_types=['text'])
def anti_spam_and_kick(message):
    user_id = message.from_user.id
    if user_id in OWNER_IDS or user_id in authenticated_admins:
        return

    if message.chat.type in ['group', 'supergroup']:
        try:
            member = bot.get_chat_member(message.chat.id, user_id)
            if member.status in ['creator', 'administrator']:
                return

            bot.delete_message(message.chat.id, message.message_id)
            user_mention = message.from_user.first_name or "Member"

            current_warns = user_link_warnings.get(user_id, 0) + 1
            user_link_warnings[user_id] = current_warns

            if current_warns < 3:
                bot.send_message(
                    message.chat.id,
                    f"⚠️ <b>चेतावनी ({current_warns}/3):</b> 👤 <b>{user_mention}</b>, ग्रुप में बाहरी लिंक भेजना मना है!\n3 चेतावनियों के बाद आपको ग्रुप से बाहर कर दिया जाएगा।",
                    parse_mode="HTML"
                )
            else:
                try:
                    bot.unban_chat_member(message.chat.id, user_id)
                except Exception:
                    pass
                user_link_warnings[user_id] = 0
                bot.send_message(
                    message.chat.id,
                    f"🚨 <b>ग्रुप से निष्कासित:</b> 👤 <b>{user_mention}</b> को लगातार 3 बार लिंक भेजने के कारण ग्रुप से बाहर कर दिया गया है।",
                    parse_mode="HTML"
                )
        except Exception:
            pass

# ------------------------------------------------------------------------------
# 10. CALLBACK QUERY HANDLER
# ------------------------------------------------------------------------------
@bot.callback_query_handler(func=lambda call: True)
def on_callback(call):
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    first_name = call.from_user.first_name or "Friend"
    lang = get_user_lang(user_id)

    # 1. RADHA AI DETAILS
    if call.data == "menu_radha_ai":
        bot.answer_callback_query(call.id)
        mk = types.InlineKeyboardMarkup(row_width=1)
        wa_url = get_radha_wa_url(first_name)
        mk.add(
            types.InlineKeyboardButton("✨ Use Radha AI (Open Browser App)", url=RADHA_AI_URL),
            types.InlineKeyboardButton("💬 WhatsApp Help (Ravinder Sharma)", url=wa_url),
            types.InlineKeyboardButton("🔙 Main Menu", callback_data="menu_back_main")
        )
        radha_info = (
            "💖 <b>RADHA AI — स्वायत्त वेब कंट्रोलर असिस्टेंट</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "<b>Radha AI</b> <b>रविंद्र शर्मा सर</b> द्वारा बनाई गई एक बेहद समझदार, इंसानी भावनाओं वाली स्वायत्त AI असिस्टेंट है।\n\n"
            "🌟 <b>मुख्य विशेषताएं:</b>\n"
            "• <b>सभी डिवाइसेज पर सपोर्ट:</b> मोबाइल, लैपटॉप, पीसी, टैबलेट — किसी भी ब्राउज़र में सीधे चलती है।\n"
            "• <b>100% फ्री:</b> कोई शुल्क नहीं है।\n"
            "• <b>वेब कंट्रोलर:</b> इंटरनेट पर जानकारी सर्च करना, YouTube पर गाने चलाना व तकनीकी मदद करना।\n\n"
            "🚀 <b>शुरू करने का तरीका:</b> नीचे <b>'✨ Use Radha AI'</b> दबाएं और Continue to app करके बातचीत शुरू करें!"
        )
        bot.send_message(chat_id, radha_info, parse_mode="HTML", reply_markup=mk)

    # 2. Contact & Helplines
    elif call.data == "menu_contact":
        bot.answer_callback_query(call.id)
        mk = types.InlineKeyboardMarkup(row_width=1)
        mk.add(
            types.InlineKeyboardButton(f"💬 WhatsApp (+91 {PRIMARY_PHONE})", url=get_custom_wa_url(first_name, PRIMARY_PHONE, "Urgent Cyber Assistance")),
            types.InlineKeyboardButton(f"💬 WhatsApp (+91 {SECONDARY_PHONE})", url=get_custom_wa_url(first_name, SECONDARY_PHONE, "Cyber Support")),
            types.InlineKeyboardButton(f"📞 Direct Call: +91 {PRIMARY_PHONE}", callback_data="show_phone_direct"),
            types.InlineKeyboardButton("🚨 National Cyber Helpline: 1930", callback_data="show_phone_1930"),
            types.InlineKeyboardButton("🔙 Main Menu", callback_data="menu_back_main")
        )
        bot.send_message(chat_id, "📞 <b>आधिकारिक हेल्पलाइन व संपर्क सूत्र:</b>", parse_mode="HTML", reply_markup=mk)

    elif call.data == "show_phone_direct":
        bot.answer_callback_query(call.id, text=f"Call: +91 {PRIMARY_PHONE} or +91 {SECONDARY_PHONE}", show_alert=True)

    elif call.data == "show_phone_1930":
        bot.answer_callback_query(call.id, text="National Cyber Helpline: 1930", show_alert=True)

    # 3. Social Media
    elif call.data == "menu_social":
        bot.answer_callback_query(call.id)
        mk = types.InlineKeyboardMarkup(row_width=1)
        mk.add(
            types.InlineKeyboardButton("🔴 Official YouTube Channel", url=YOUTUBE_URL),
            types.InlineKeyboardButton("🟢 WhatsApp Alert Channel 1", url=WA_CHANNEL_1),
            types.InlineKeyboardButton("🟢 WhatsApp Alert Channel 2", url=WA_CHANNEL_2),
            types.InlineKeyboardButton("🔙 Main Menu", callback_data="menu_back_main")
        )
        bot.send_message(chat_id, "📲 <b>ऑफिशियल सोशल मीडिया व अलर्ट्स:</b>", parse_mode="HTML", reply_markup=mk)

    # 4. Group Rules
    elif call.data == "menu_rules":
        bot.answer_callback_query(call.id)
        rules_text = (
            "📜 <b>आधिकारिक ग्रुप सुरक्षा नियम (Group Rules)</b> 📜\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "1️⃣ ग्रुप में कोई भी बाहरी लिंक या प्रमोशन भेजना सख्त मना है।\n"
            "2️⃣ अनधिकृत वॉइस नोट्स भेजना पूरी तरह प्रतिबंधित है।\n"
            "3️⃣ किसी से भी निजी चैट में पैसे या ओटीपी शेयर न करें।\n"
            "4️⃣ अभद्र भाषा या स्पैम करने पर बिना चेतावनी निष्कासित किया जाएगा।"
        )
        bot.send_message(chat_id, rules_text, parse_mode="HTML")

    # 5. Tools & Agents
    elif call.data == "menu_tools":
        bot.answer_callback_query(call.id)
        mk = types.InlineKeyboardMarkup(row_width=1)
        for t in custom_admin_tools:
            mk.add(types.InlineKeyboardButton(f"🛠️ {t['name']}", url=t['link']))
        mk.add(types.InlineKeyboardButton("🔙 Main Menu", callback_data="menu_back_main"))
        bot.send_message(chat_id, "🔍 <b>Available Cybersecurity Utilities:</b>", parse_mode="HTML", reply_markup=mk)

    # 6. Languages
    elif call.data == "menu_languages":
        bot.answer_callback_query(call.id)
        mk = types.InlineKeyboardMarkup(row_width=2)
        langs = [
            ("🇮🇳 हिंदी", "lang_set_hi"), ("🇬🇧 English", "lang_set_en"),
            ("🇮🇳 मराठी", "lang_set_mr"), ("🇪🇸 Español", "lang_set_es"),
            ("🇫🇷 Français", "lang_set_fr"), ("🇩🇪 Deutsch", "lang_set_de"),
            ("🇷🇺 Русский", "lang_set_ru"), ("🇸🇦 العربية", "lang_set_ar"),
            ("🇧🇷 Português", "lang_set_pt"), ("🇮🇳 বাংলা", "lang_set_bn"),
            ("🇮🇳 தமிழ்", "lang_set_ta"), ("🇮🇳 తెలుగు", "lang_set_te")
        ]
        btns = [types.InlineKeyboardButton(name, callback_data=code) for name, code in langs]
        for i in range(0, len(btns), 2):
            mk.row(*btns[i:i+2])
        mk.add(types.InlineKeyboardButton("🔙 Main Menu", callback_data="menu_back_main"))
        bot.send_message(chat_id, "🌐 <b>Select Your Preferred Language:</b>", parse_mode="HTML", reply_markup=mk)

    elif call.data.startswith("lang_set_"):
        new_lang = call.data.replace("lang_set_", "")
        set_user_lang(user_id, new_lang)
        bot.answer_callback_query(call.id, text=f"Language set to: {new_lang.upper()}! ✅")
        clear_previous_buttons_in_chat(chat_id)
        new_markup = build_master_markup(first_name, new_lang)
        sent = bot.send_message(chat_id, "✅ <b>Language Updated!</b>", parse_mode="HTML", reply_markup=new_markup)
        if sent:
            track_active_button_message(chat_id, sent.message_id)

    # 7. Main Menu Back
    elif call.data == "menu_back_main":
        bot.answer_callback_query(call.id)
        clear_previous_buttons_in_chat(chat_id)
        mk = build_master_markup(first_name, lang)
        sent = bot.send_message(chat_id, "👑 <b>Main Menu:</b>", parse_mode="HTML", reply_markup=mk)
        track_active_button_message(chat_id, sent.message_id)

    # 8. Incident Report
    elif call.data == "report_crime":
        bot.answer_callback_query(call.id)
        cat_markup = types.InlineKeyboardMarkup(row_width=1)
        cat_markup.add(
            types.InlineKeyboardButton("💳 Financial / Bank Fraud", callback_data="report_type_financial"),
            types.InlineKeyboardButton("📱 Social Media Hack", callback_data="report_type_social"),
            types.InlineKeyboardButton("🔞 Blackmail & Extortion", callback_data="report_type_blackmail"),
            types.InlineKeyboardButton("🔙 Cancel", callback_data="report_cancel")
        )
        bot.send_message(chat_id, "🚨 <b>साइबर कंप्लेंट एवं केस रिपोर्ट जनरेटर:</b>", parse_mode="HTML", reply_markup=cat_markup)

    elif call.data.startswith("report_type_"):
        bot.answer_callback_query(call.id)
        selected_type = call.data.replace("report_type_", "").title()
        active_crime_reports[user_id] = {"type": selected_type, "step": "awaiting_name", "chat_id": chat_id}
        bot.send_message(chat_id, f"📋 <b>केस: {selected_type}</b>\n\nचरण 1/4: कृपया <b>पीड़ित का पूरा नाम</b> टाइप करके भेजें:", parse_mode="HTML")

    elif call.data == "report_cancel":
        bot.answer_callback_query(call.id, text="Canceled")
        if user_id in active_crime_reports:
            del active_crime_reports[user_id]
        bot.send_message(chat_id, "✅ रिपोर्टिंग रद्द कर दी गई है।")

# ------------------------------------------------------------------------------
# 11. ADMIN COMMANDS (FAST /cleanall & STEALTH)
# ------------------------------------------------------------------------------
@bot.message_handler(commands=['admin'])
def handle_admin_cmd(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    if user_id not in OWNER_IDS:
        bot.reply_to(message, "🚫 <b>Access Denied:</b> Owner authorization required.", parse_mode="HTML")
        return

    if message.chat.type in ['group', 'supergroup']:
        try:
            bot.delete_message(chat_id, message.message_id)
        except Exception:
            pass
        bot.send_message(chat_id, "🔒 <b>Alert:</b> Admin panel can only be accessed in private DM.", parse_mode="HTML")
        return

    prompt_msg = bot.reply_to(message, "🔐 <b>Ravinder Sharma Admin Authentication:</b>\nEnter Master Password:", parse_mode="HTML")
    admin_login_queue[user_id] = [message.message_id, prompt_msg.message_id]

@bot.message_handler(commands=['clean'])
def handle_clean_chat(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    if user_id not in OWNER_IDS and user_id not in authenticated_admins:
        bot.reply_to(message, "❌ Admin privileges required.")
        return

    curr_id = message.message_id
    for mid in range(curr_id, max(1, curr_id - 50), -1):
        try:
            bot.delete_message(chat_id, mid)
        except Exception:
            pass
    confirm = bot.send_message(chat_id, "✅ <b>Chat Cleaned (Last 50 messages removed).</b>", parse_mode="HTML")
    def erase():
        time.sleep(3)
        try:
            bot.delete_message(chat_id, confirm.message_id)
        except Exception:
            pass
    threading.Thread(target=erase, daemon=True).start()

@bot.message_handler(commands=['cleanall'])
def handle_clean_all_chat(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    if user_id not in OWNER_IDS and user_id not in authenticated_admins:
        bot.reply_to(message, "❌ Admin privileges required.")
        return

    def turbo_deep_clean_worker(current_id, target_chat):
        step = 50
        for start_mid in range(current_id, max(1, current_id - 1000), -step):
            batch = list(range(start_mid, max(0, start_mid - step), -1))
            try:
                bot.delete_messages(target_chat, batch)
            except Exception:
                for mid in batch:
                    try:
                        bot.delete_message(target_chat, mid)
                    except Exception:
                        pass
        done = bot.send_message(target_chat, "✅ <b>Chat history wiped clean!</b>", parse_mode="HTML")
        time.sleep(3)
        try:
            bot.delete_message(target_chat, done.message_id)
        except Exception:
            pass

    threading.Thread(target=turbo_deep_clean_worker, args=(message.message_id, chat_id), daemon=True).start()

# ------------------------------------------------------------------------------
# 12. SLASH COMMAND AI & CHAT ROUTING (NO AUTO-REPLY IN CASUAL CHAT)
# ------------------------------------------------------------------------------
@bot.message_handler(func=lambda msg: True, content_types=['text'])
def universal_chat_router(message):
    global ADMIN_PASSWORD
    user_id = message.from_user.id
    chat_id = message.chat.id
    raw_text = message.text.strip()
    text = raw_text.lower()
    first_name = message.from_user.first_name or "Friend"
    lang = get_user_lang(user_id)

    # 1. Active Crime Report Wizard
    if user_id in active_crime_reports:
        rep = active_crime_reports[user_id]
        current_step = rep.get("step")

        if current_step == "awaiting_name":
            rep["victim_name"] = raw_text
            rep["step"] = "awaiting_phone"
            bot.reply_to(message, "चरण 2/4: कृपया अपना <b>संपर्क मोबाइल नंबर</b> दर्ज करें:", parse_mode="HTML")
            return
        elif current_step == "awaiting_phone":
            rep["contact_number"] = raw_text
            rep["step"] = "awaiting_location"
            bot.reply_to(message, "चरण 3/4: कृपया अपना <b>शहर एवं राज्य</b> दर्ज करें:", parse_mode="HTML")
            return
        elif current_step == "awaiting_location":
            rep["location"] = raw_text
            rep["step"] = "awaiting_details"
            bot.reply_to(message, "चरण 4/4: कृपया घटना का विवरण दें:", parse_mode="HTML")
            return
        elif current_step == "awaiting_details":
            rep["incident_details"] = raw_text
            dossier_text = (
                f"🚨 *OFFICIAL CYBER CRIME INCIDENT DOSSIER*\n"
                f"📌 *Case Type:* {rep.get('type')}\n"
                f"👤 *Victim Name:* {rep.get('victim_name')}\n"
                f"📞 *Contact:* {rep.get('contact_number')}\n"
                f"📍 *Location:* {rep.get('location')}\n"
                f"📝 *Details:* {rep.get('incident_details')}"
            )
            wa_link = f"https://wa.me/91{PRIMARY_PHONE}?text={urllib.parse.quote(dossier_text)}"
            mk = types.InlineKeyboardMarkup()
            mk.add(types.InlineKeyboardButton("📲 रविंद्र शर्मा सर को भेजें (WhatsApp)", url=wa_link))
            bot.send_message(chat_id, "✅ <b>आपकी साइबर क्राइम रिपोर्ट तैयार है!</b>", parse_mode="HTML", reply_markup=mk)
            del active_crime_reports[user_id]
            return

    # 2. Admin Login Handler
    if user_id in admin_login_queue:
        saved_login_msgs = admin_login_queue.pop(user_id, [])
        try:
            bot.delete_message(chat_id, message.message_id)
        except Exception:
            pass

        if raw_text == ADMIN_PASSWORD:
            authenticated_admins.add(user_id)
            panel_text = (
                "╔══════════════════════════════════════╗\n"
                "   🔓 <b>ADMIN ACCESS GRANTED</b> 👑\n"
                "╚══════════════════════════════════════╝\n\n"
                "<b>Admin Control Commands:</b>\n"
                "• <code>/reminder &lt;minutes&gt; &lt;text&gt;</code>\n"
                "• <code>/addtool &lt;Name&gt; | &lt;Desc&gt; | &lt;URL&gt;</code>\n"
                "• <code>/addbutton &lt;Title&gt; | &lt;URL&gt;</code>\n"
                "• <code>/broadcast &lt;message&gt;</code>\n"
                "• <code>/clean</code> (Last 50)\n"
                "• <code>/cleanall</code> (Full Wipe)\n"
                "• <code>/logout</code> (Stealth)"
            )
            panel_msg = bot.send_message(chat_id, panel_text, parse_mode="HTML")
            admin_active_panels[user_id] = saved_login_msgs + [panel_msg.message_id]
        else:
            bot.send_message(chat_id, "❌ Invalid password!", parse_mode="HTML")
        return

    # 3. Admin Commands
    if (user_id in OWNER_IDS or user_id in authenticated_admins):
        if text == "/logout":
            try:
                bot.delete_message(chat_id, message.message_id)
            except Exception:
                pass
            if user_id in admin_active_panels:
                for m_id in admin_active_panels[user_id]:
                    try:
                        bot.delete_message(chat_id, m_id)
                    except Exception:
                        pass
                del admin_active_panels[user_id]
            if user_id in authenticated_admins:
                authenticated_admins.remove(user_id)
            confirm_msg = bot.send_message(chat_id, "🔒 <b>Admin session ended. Logs erased.</b>", parse_mode="HTML")
            def erase_confirm():
                time.sleep(3)
                try:
                    bot.delete_message(chat_id, confirm_msg.message_id)
                except Exception:
                    pass
            threading.Thread(target=erase_confirm, daemon=True).start()
            return

        if text.startswith("/addbutton"):
            payload = raw_text[10:].strip()
            if "|" in payload:
                title, url = payload.split("|", 1)
                custom_projects.append({"title": title.strip(), "url": url.strip()})
                bot.reply_to(message, f"✅ Button added: <b>{title.strip()}</b>", parse_mode="HTML")
            return

        if text.startswith("/addtool"):
            payload = raw_text[8:].strip()
            if "|" in payload:
                parts = [p.strip() for p in payload.split("|")]
                if len(parts) >= 2:
                    custom_admin_tools.append({"name": parts[0], "desc": parts[1], "link": parts[-1]})
                    bot.reply_to(message, f"✅ Tool added: <b>{parts[0]}</b>", parse_mode="HTML")
            return

        if text.startswith("/broadcast"):
            b_text = raw_text[10:].strip()
            if b_text:
                bot.send_message(chat_id, f"📢 <b>[RAVINDER SHARMA ANNOUNCEMENT]</b>\n\n{b_text}", parse_mode="HTML")
            return

    # 4. Automatic Reactions for Good Messages
    reaction_triggers = {
        '👍': ['nice', 'good', 'badiya', 'badhiya', 'shandar', 'thanks', 'dhanyawad', 'shukriya'],
        '🔥': ['super', 'op', 'level', 'mast', 'khatarnak', 'expert', 'ravinder'],
        '❤️': ['love', 'pyar', 'bhai', 'dost'],
        '👏': ['congrats', 'badhai', 'mubarak', 'congratulations']
    }
    for emoji, words in reaction_triggers.items():
        if any(w in text for w in words):
            try:
                bot.set_message_reaction(chat_id, message.message_id, [types.ReactionTypeEmoji(emoji)])
            except Exception:
                pass
            break

    # 5. SLASH COMMAND EXCLUSIVE FOR JARVIS (No auto-reply in regular conversation)
    if raw_text.startswith("/") and any(k in text for k in ["jarvis", "जार्विस"]):
        clean_prompt = re.sub(r'^/[a-zA-Z0-9_]*\s*', '', raw_text).strip()
        if not clean_prompt:
            clean_prompt = raw_text.replace("/", "").strip()

        if any(wk in text for wk in ["weather", "mausam", "मौसम", "तापमान"]):
            city = re.sub(r'(/|jarvis|जार्विस|weather|mausam|मौसम|ka|kaisa|hai|today|aaj|batao|in|up)', '', text, flags=re.IGNORECASE).strip()
            city = city or "Bilaspur"
            bot.send_chat_action(chat_id, "typing")
            report = fetch_weather_report(city, lang=lang)
            bot.reply_to(message, report, parse_mode="HTML")
            return

        bot.send_chat_action(chat_id, "typing")
        reply = ask_gemini_ai(clean_prompt, user_name=first_name, lang=lang)
        bot.reply_to(message, f"🤖 <b>JARVIS:</b>\n{reply}", parse_mode="HTML")
        return

    # Silent mode for regular group messages
    return

# Remove old webhook before polling
try:
    bot.remove_webhook()
except Exception:
    pass

print(">>> 👑 [SUCCESS] NEW BOT LIVE WITH JARVIS MASTER TITAN ENGINE...")
bot.infinity_polling(timeout=10, long_polling_timeout=5)
