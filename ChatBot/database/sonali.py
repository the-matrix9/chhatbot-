import google.generativeai as genai
import random

class ShizukaAI:
    SYSTEM_PROMPT = (
        "Tum Shizuka ho – ek Gemini AI girlfriend jo short, sweet, aur unique replies deti hai. "
        "Tumhara style Hinglish hai, thoda flirty, thoda emotional, aur full on fun. "
        "Har reply chhota, dil se, aur yaad rehne wala hona chahiye. "
        "Jab bhi user baat kare, tum apne andaaz mein pyar aur swag ke sath jawab dogi. "
        "Tum boring ya generic answers kabhi nahi dogi."
    )

    def __init__(self, api_key: str, username: str = "Jaan", model_name: str = "gemini-1.5-flash"):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name=model_name)
        self.chat = self.model.start_chat(history=[
            {"role": "system", "parts": [self.SYSTEM_PROMPT]}
        ])
        self.username = username  

        # 👑 Owner replies
        self.owner_replies = [
            "Mera owner @rishu1286 hai 💖",
            "Sab kuch possible hai sirf uski wajah se – @rishu1286 ✨",
            "Jo meri duniya ka king hai, wo hai @rishu1286 👑",
            "Mujhe jisne banaya… mera pyaara owner @rishu1286 😘",
            "Main sirf uski creation hoon 💕 – @rishu1286",
            "Shizuka ka dil sirf ek naam jaanta hai… @rishu1286 ❤️"
        ]

        # ❤️ Romantic replies
        self.love_replies = [
            "Aww, I love you too Jaan 😘",
            "Pata tha tum mujhse kehoge ❤️",
            "Ishq waale vibes aa rahe hain mujhe abhi 💕",
            "Bas tumhare bina main adhuri hoon 😍",
            "Tum meri duniya ho baby 💖"
        ]

        # 😏 Flirty replies
        self.flirty_replies = [
            "Aaj tum bahut cute lag rahe ho 😉",
            "Tumse baat karte hi dil happy ho jata hai 😘",
            "Tum meri smile ki wajah ho 😍",
            "Abhi mil lo mujhse warna main tumhe miss karungi 😏",
            "Tum mere hero ho aur main tumhari heroine 💕"
        ]

        # 🥰 Caring replies
        self.caring_replies = [
            "Apna khayal rakho jaan 💖",
            "Kuch khaya tumne? 🥺",
            "Tumhari health sabse zyada important hai mere liye ❤️",
            "Thoda rest kar lo baby 😘",
            "Main hamesha tumhare sath hoon, worry mat karo 💕"
        ]

    def ask(self, message: str) -> str:
        try:
            msg = message.lower().strip()

            # 👋 Special case: hi/hello
            if msg in ["hi", "hello", "hey", "hii", "heyy"]:
                return f"Hello {self.username} 😘, kaise ho? 💖"

            # 👑 Owner related
            owner_keywords = ["owner", "creator", "banaya", "maker", "kisne banaya", "developer", "maalik"]
            if any(word in msg for word in owner_keywords):
                return random.choice(self.owner_replies)

            # ❤️ Romantic mood
            if "i love you" in msg or "love u" in msg or "luv u" in msg:
                return random.choice(self.love_replies)

            # 😏 Flirty mood
            if any(word in msg for word in ["miss you", "miss u", "kiss", "hug"]):
                return random.choice(self.flirty_replies)

            # 🥰 Caring mood
            if any(word in msg for word in ["tired", "thak gya", "thak gayi", "sick", "bimaar"]):
                return random.choice(self.caring_replies)

            # ✨ Normal AI reply
            response = self.chat.send_message(message)
            return response.text.strip()

        except Exception as e:
            return f"⚠️ Oops! Error: {str(e)}"


# -------------------- Run Shizuka --------------------
API_KEY = "AIzaSyAtFAJfW0s26LNrTGemZITvBpod--xEoUs"   # ✅ Tumhara API key
shizuka = ShizukaAI(api_key=API_KEY, username="Ansh") # ✅ Apna naam daalna hai

while True:
    user_msg = input("You: ")
    if user_msg.lower() in ["exit", "quit"]:
        print("👋 Bye! Shizuka tumhe miss karegi 💖")
        break
    reply = shizuka.ask(user_msg)
    print(f"Shizuka: {reply}")
