import time
import random
import json
import requests
import tkinter as tk
from threading import Thread
from datetime import datetime

# Steam API settings
STEAM_API_KEY = "92A7436F7C65CD4748287771D74452A2"
STEAM_USER_ID = "76561199177046862"
SESSION_ID = "38208f2a9761f1208544d865"  # Insert your session ID here
COOKIE = "sessionid=38208f2a9761f1208544d865; steamCountry=DE%7Cbcca10e621b32d39f59f14d491c63a25"  # Insert your cookie here
COMMENT_INTERVAL = 120  # 2 minutes in seconds
COMMENT_LIMIT = 10  # Maximum 10 comments per day

# Friendly comment database
COMMENTS = [
    "May every day of yours be like a blooming flower, filled with beauty and love 💗",
    "You're a star that shines brightly even on the darkest nights! ✨🌙",
    "Just passing by to remind you how amazing you are! 🌟",
    "Your kindness and energy make the world a better place! 💖",
    "Hope today brings you nothing but joy and happiness! ☀️😊",
    "Sending you virtual hugs and lots of good vibes! 🤗💞",
    "May your day be as sweet and wonderful as you are! 🍯🌸",
    "You're like a warm cup of tea on a rainy day—comforting and full of love! ☕💖",
    "You are appreciated, loved, and absolutely awesome! 💙✨",
    "Like the moon needs the stars, the world needs people like you! 🌙⭐",
    "A single smile from you can brighten someone's entire day! 😊💛",
    "Stay strong, stay happy, and always be yourself! You're amazing! 💕",
    "You are the sunshine that makes even cloudy days beautiful! ☀️💖",
    "Just a friendly reminder: You are enough, you are loved, and you are wonderful! 💞",
    "Hope your day is filled with unexpected joys and lovely surprises! 🎁🎉",
    "Your presence makes the world a more beautiful place! 🌍💖",
    "You're a gem, rare and precious! Never stop shining! 💎✨",
    "Wishing you a day full of love, laughter, and magic! ✨💖",
    "The world is a better place just because you're in it! 💫💜",
    "May happiness follow you wherever you go today! 🦋🌼",
    "Life is a beautiful journey, and you're making it even more wonderful! 🚀💖",
    "You bring light to everyone around you—keep shining! 🌟😊",
    "You have a heart as pure as a crystal and a soul as warm as the sun! 💎☀️",
    "Sending you a wave of positivity, love, and good vibes! 🌊💙",
    "You're not just a person, you're a whole vibe of happiness! 🎶💖",
    "Your kindness is like a ripple in a pond—it spreads far and wide! 💞🌊",
    "The world would be a little less bright without you in it! 🌍💡",
    "May today be filled with little moments that make you smile! 😊🌸",
    "Keep being your awesome self—you're an inspiration! 🚀💛",
    "No matter where life takes you, may happiness always follow! 🌎💖",
    "Wishing you a day filled with love, laughter, and all things wonderful! 🎀💗"
]

# Variables for counter and date
comment_count = 0
last_reset_date = datetime.now().date()

# Steam API request for friend list
def get_friends():
    url = f"https://api.steampowered.com/ISteamUser/GetFriendList/v1/?key={STEAM_API_KEY}&steamid={STEAM_USER_ID}&relationship=friend"
    response = requests.get(url)
    if response.status_code == 200:
        friends = response.json().get("friendslist", {}).get("friends", [])
        return [friend["steamid"] for friend in friends]
    return []

# Post a comment on a profile
def post_comment(steam_id, comment):
    global comment_count
    url = f"https://steamcommunity.com/comment/Profile/post/{steam_id}/-1/"
    payload = {
        "comment": comment,
        "count": 6
    }
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": f"https://steamcommunity.com/profiles/{steam_id}",
        "Cookie": f"sessionid={SESSION_ID}; {COOKIE}"
    }
    response = requests.post(url, data=payload, headers=headers)
    if response.status_code == 200:
        comment_count += 1
        print(f"[INFO] Kommentar gepostet für {steam_id}: {comment}")
    else:
        print(f"[FEHLER] Kommentar konnte nicht gepostet werden: {response.status_code}")

# Reset the counter if a new day begins
def reset_counter_if_new_day():
    global comment_count, last_reset_date
    current_date = datetime.now().date()
    if current_date > last_reset_date:
        comment_count = 0
        last_reset_date = current_date
        print("[INFO] Zähler zurückgesetzt für den neuen Tag.")

# Main commenting function
def comment_loop():
    while True:
        reset_counter_if_new_day()  # Reset counter if a new day
        if comment_count < COMMENT_LIMIT:
            friends = get_friends()
            if not friends:
                print("[WARNUNG] Keine Freunde gefunden oder API-Fehler.")
            for friend in friends:
                comment = random.choice(COMMENTS)
                post_comment(friend, comment)
                if comment_count >= COMMENT_LIMIT:
                    print("[INFO] Maximale Kommentaranzahl für den Tag erreicht.")
                    return
                time.sleep(COMMENT_INTERVAL)
        else:
            print("[INFO] Maximale Kommentaranzahl für den Tag erreicht.")
            time.sleep(3600)  # Wait 1 hour before trying again the next day

# GUI function
def start_bot():
    thread = Thread(target=comment_loop, daemon=True)
    thread.start()
    status_label.config(text="Bot läuft...")

# GUI setup
root = tk.Tk()
root.title("Steam Kommentar Bot")
root.geometry("300x200")
status_label = tk.Label(root, text="Bot nicht aktiv", fg="red")
status_label.pack(pady=10)
start_button = tk.Button(root, text="Bot starten", command=start_bot)
start_button.pack(pady=10)
root.mainloop()
