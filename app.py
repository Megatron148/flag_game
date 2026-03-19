import streamlit as st
from PIL import Image
import os
import random
from groq import Groq
from dotenv import load_dotenv

# --- AI SETUP ---
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# --- CONFIG ---
st.set_page_config(page_title="Flag Game", page_icon="🏳️", layout="centered")
st.title("🌍 Flag Quiz Game")
st.markdown("### ⚡ VEXOR is watching...")

# --- FLAG FOLDER ---
flags_folder = "flags"

# --- REGIONS ---
easy_famous = ["us", "fr", "de", "br", "jp", "au", "gb", "ca", "it", "es", "cn", "in", "mx", "za", "gb-eng"]

europe = ["ad", "al", "am", "at", "az", "ba", "be", "bg", "by", "ch", "cy", "cz", "dk", "ee",
          "es", "fi", "fr", "gb", "ge", "gr", "hr", "hu", "is", "it", "li", "lt", "lu",
          "lv", "md", "me", "mk", "mt", "nl", "no", "pt", "rs", "ru", "se",
          "sm", "ua", "va", "xk", "gb-sct", "gb-wls"]

americas = ["ag", "ar", "bb", "bo", "br", "bs", "bz", "ca", "cl", "co", "cr", "cu", "dm", "do",
            "ec", "gd", "gt", "gy", "hn", "ht", "jm", "kn", "lc", "mx", "ni", "pa", "pe", "py",
            "sr", "sv", "tt", "us", "uy", "vc", "ve"]

asia = ["af", "am", "az", "bd", "bn", "bt", "cn", "ge", "in", "jp", "kg", "kh", "kp", "kr",
        "kz", "la", "lk", "mm", "mn", "mv", "my", "np", "ph", "pk", "sg", "th", "tj", "tl",
        "tm", "tw", "uz", "vn"]

africa = ["ao", "bf", "bi", "bj", "bw", "cd", "cf", "cg", "cm", "cv", "dj", "dz", "eg",
          "er", "et", "ga", "gh", "gm", "gq", "gw", "ke", "km", "lr", "ls", "ly", "ma",
          "mg", "mr", "mu", "mw", "mz", "na", "ne", "ng", "rw", "sc", "sd", "sl", "sn",
          "so", "ss", "st", "sz", "tg", "tn", "tz", "ug", "za", "zm", "zw"]

middle_east = ["ae", "bh", "il", "iq", "ir", "jo", "kw", "lb", "om", "ps", "qa", "sa", "sy", "tr", "ye"]

oceania = ["au", "fj", "fm", "ki", "mh", "nr", "pg", "pw", "sb", "to", "tv", "vu", "ws"]

territories = ["ai", "aq", "as", "aw", "ax", "bm", "bq", "cc", "ck", "cx", "cw", "eh", "fk", "fo",
               "gb-nir", "gf", "gg", "gi", "gl", "gp", "gs", "gu", "hk", "im", "io", "je",
               "ky", "mo", "mp", "mq", "ms", "nc", "nf", "nu", "pf", "pm", "pn", "pr", "re",
               "sh", "sx", "tc", "tf", "tk", "vg", "vi", "wf", "yt"]

lookalikes = ["td", "ro", "id", "mc", "pl", "ie", "ci", "si", "sk", "gn", "ml", "nz"]

# --- ALL COUNTRIES ---
country_codes = {
    "ad": "Andorra", "ae": "United Arab Emirates", "af": "Afghanistan",
    "ag": "Antigua and Barbuda", "ai": "Anguilla", "al": "Albania",
    "am": "Armenia", "ao": "Angola", "aq": "Antarctica",
    "ar": "Argentina", "as": "American Samoa", "at": "Austria",
    "au": "Australia", "aw": "Aruba", "ax": "Aland Islands",
    "az": "Azerbaijan", "ba": "Bosnia and Herzegovina", "bb": "Barbados",
    "bd": "Bangladesh", "be": "Belgium", "bf": "Burkina Faso",
    "bg": "Bulgaria", "bh": "Bahrain", "bi": "Burundi",
    "bj": "Benin", "bm": "Bermuda", "bn": "Brunei",
    "bo": "Bolivia", "bq": "Caribbean Netherlands", "br": "Brazil",
    "bs": "Bahamas", "bt": "Bhutan", "bw": "Botswana",
    "by": "Belarus", "bz": "Belize", "ca": "Canada",
    "cc": "Cocos Islands", "cd": "DR Congo", "cf": "Central African Republic",
    "cg": "Republic of the Congo", "ch": "Switzerland", "ci": "Ivory Coast",
    "ck": "Cook Islands", "cl": "Chile", "cm": "Cameroon",
    "cn": "China", "co": "Colombia", "cr": "Costa Rica",
    "cu": "Cuba", "cv": "Cape Verde", "cw": "Curacao",
    "cx": "Christmas Island", "cy": "Cyprus", "cz": "Czech Republic",
    "de": "Germany", "dj": "Djibouti", "dk": "Denmark",
    "dm": "Dominica", "do": "Dominican Republic", "dz": "Algeria",
    "ec": "Ecuador", "ee": "Estonia", "eg": "Egypt",
    "eh": "Western Sahara", "er": "Eritrea", "es": "Spain",
    "et": "Ethiopia", "fi": "Finland", "fj": "Fiji",
    "fk": "Falkland Islands", "fm": "Micronesia", "fo": "Faroe Islands",
    "fr": "France", "ga": "Gabon", "gb": "United Kingdom",
    "gb-eng": "England", "gb-nir": "Northern Ireland",
    "gb-sct": "Scotland", "gb-wls": "Wales",
    "gd": "Grenada", "ge": "Georgia", "gf": "French Guiana",
    "gg": "Guernsey", "gh": "Ghana", "gi": "Gibraltar",
    "gl": "Greenland", "gm": "Gambia", "gn": "Guinea",
    "gp": "Guadeloupe", "gq": "Equatorial Guinea", "gr": "Greece",
    "gs": "South Georgia", "gt": "Guatemala", "gu": "Guam",
    "gw": "Guinea-Bissau", "gy": "Guyana", "hk": "Hong Kong",
    "hn": "Honduras", "hr": "Croatia", "ht": "Haiti",
    "hu": "Hungary", "id": "Indonesia", "ie": "Ireland",
    "il": "Israel", "im": "Isle of Man", "in": "India",
    "io": "British Indian Ocean Territory", "iq": "Iraq", "ir": "Iran",
    "is": "Iceland", "it": "Italy", "je": "Jersey",
    "jm": "Jamaica", "jo": "Jordan", "jp": "Japan",
    "ke": "Kenya", "kg": "Kyrgyzstan", "kh": "Cambodia",
    "ki": "Kiribati", "km": "Comoros", "kn": "Saint Kitts and Nevis",
    "kp": "North Korea", "kr": "South Korea", "kw": "Kuwait",
    "ky": "Cayman Islands", "kz": "Kazakhstan", "la": "Laos",
    "lb": "Lebanon", "lc": "Saint Lucia", "li": "Liechtenstein",
    "lk": "Sri Lanka", "lr": "Liberia", "ls": "Lesotho",
    "lt": "Lithuania", "lu": "Luxembourg", "lv": "Latvia",
    "ly": "Libya", "ma": "Morocco", "mc": "Monaco",
    "md": "Moldova", "me": "Montenegro", "mg": "Madagascar",
    "mh": "Marshall Islands", "mk": "North Macedonia", "ml": "Mali",
    "mm": "Myanmar", "mn": "Mongolia", "mo": "Macau",
    "mp": "Northern Mariana Islands", "mq": "Martinique", "mr": "Mauritania",
    "ms": "Montserrat", "mt": "Malta", "mu": "Mauritius",
    "mv": "Maldives", "mw": "Malawi", "mx": "Mexico",
    "my": "Malaysia", "mz": "Mozambique", "na": "Namibia",
    "nc": "New Caledonia", "ne": "Niger", "nf": "Norfolk Island",
    "ng": "Nigeria", "ni": "Nicaragua", "nl": "Netherlands",
    "no": "Norway", "np": "Nepal", "nr": "Nauru",
    "nu": "Niue", "nz": "New Zealand", "om": "Oman",
    "pa": "Panama", "pe": "Peru", "pf": "French Polynesia",
    "pg": "Papua New Guinea", "ph": "Philippines", "pk": "Pakistan",
    "pl": "Poland", "pm": "Saint Pierre and Miquelon", "pn": "Pitcairn Islands",
    "pr": "Puerto Rico", "ps": "Palestine", "pt": "Portugal",
    "pw": "Palau", "py": "Paraguay", "qa": "Qatar",
    "re": "Reunion", "ro": "Romania", "rs": "Serbia",
    "ru": "Russia", "rw": "Rwanda", "sa": "Saudi Arabia",
    "sb": "Solomon Islands", "sc": "Seychelles", "sd": "Sudan",
    "se": "Sweden", "sg": "Singapore", "sh": "Saint Helena",
    "si": "Slovenia", "sk": "Slovakia", "sl": "Sierra Leone",
    "sm": "San Marino", "sn": "Senegal", "so": "Somalia",
    "sr": "Suriname", "ss": "South Sudan", "st": "Sao Tome and Principe",
    "sv": "El Salvador", "sx": "Sint Maarten", "sy": "Syria",
    "sz": "Eswatini", "tc": "Turks and Caicos Islands", "td": "Chad",
    "tf": "French Southern Territories", "tg": "Togo", "th": "Thailand",
    "tj": "Tajikistan", "tk": "Tokelau", "tl": "Timor-Leste",
    "tm": "Turkmenistan", "tn": "Tunisia", "to": "Tonga",
    "tr": "Turkey", "tt": "Trinidad and Tobago", "tv": "Tuvalu",
    "tw": "Taiwan", "tz": "Tanzania", "ua": "Ukraine",
    "ug": "Uganda", "us": "United States", "uy": "Uruguay",
    "uz": "Uzbekistan", "va": "Vatican City", "vc": "Saint Vincent and the Grenadines",
    "ve": "Venezuela", "vg": "British Virgin Islands", "vi": "U.S. Virgin Islands",
    "vn": "Vietnam", "vu": "Vanuatu", "wf": "Wallis and Futuna",
    "ws": "Samoa", "xk": "Kosovo", "ye": "Yemen",
    "yt": "Mayotte", "za": "South Africa", "zm": "Zambia", "zw": "Zimbabwe"
}

# --- SESSION STATE ---
if "score" not in st.session_state:
    st.session_state.score = 0
if "streak" not in st.session_state:
    st.session_state.streak = 0
if "current_flag" not in st.session_state:
    st.session_state.current_flag = None
if "input_key" not in st.session_state:
    st.session_state.input_key = 0
if "wrong_attempts" not in st.session_state:
    st.session_state.wrong_attempts = 0
if "message" not in st.session_state:
    st.session_state.message = ""
if "message_type" not in st.session_state:
    st.session_state.message_type = ""
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "flag_number" not in st.session_state:
    st.session_state.flag_number = 1
if "region_stats" not in st.session_state:
    st.session_state.region_stats = {
        "europe": {"correct": 0, "wrong": 0},
        "americas": {"correct": 0, "wrong": 0},
        "asia": {"correct": 0, "wrong": 0},
        "africa": {"correct": 0, "wrong": 0},
        "middle_east": {"correct": 0, "wrong": 0},
        "oceania": {"correct": 0, "wrong": 0},
        "territories": {"correct": 0, "wrong": 0},
        "lookalikes": {"correct": 0, "wrong": 0},
    }
if "used_flags" not in st.session_state:
    st.session_state.used_flags = []
if "ai_message" not in st.session_state:
    st.session_state.ai_message = ""
if "vexor_intro_shown" not in st.session_state:
    st.session_state.vexor_intro_shown = False
if "flags_wrong_this_turn" not in st.session_state:
    st.session_state.flags_wrong_this_turn = set()

# --- HELPER: GET REGION OF A FLAG ---
def get_region(code):
    if code in lookalikes: return "lookalikes"
    if code in territories: return "territories"
    if code in europe: return "europe"
    if code in americas: return "americas"
    if code in asia: return "asia"
    if code in africa: return "africa"
    if code in middle_east: return "middle_east"
    if code in oceania: return "oceania"
    return None

# --- HELPER: GET WORST REGION (excluding territories and lookalikes) ---
def get_worst_region():
    worst = None
    worst_rate = 1.0
    for region, stats in st.session_state.region_stats.items():
        if region in ["territories", "lookalikes"]:
            continue
        total = stats["correct"] + stats["wrong"]
        if total > 0:
            rate = stats["correct"] / total
            if rate < worst_rate:
                worst_rate = rate
                worst = region
    return worst

# --- GET AI MESSAGE ---
def get_ai_message(flag_num, worst_region):
    try:
        if not st.session_state.vexor_intro_shown:
            prompt = "You are VEXOR, an all-knowing sinister flag game overlord. Give a dramatic, cool, unique 1-2 sentence introduction to the player as they enter your domain for the first time. Make it feel like they have just stepped into something they cannot escape."
        elif flag_num <= 5:
            prompt = "You are VEXOR, a snarky but fun flag game host. The player is on an easy warm up flag. Give a short 1 sentence encouraging but slightly condescending message."
        elif flag_num <= 15:
            prompt = "You are VEXOR, a snarky flag game host. You are silently watching the player and collecting data on their weaknesses. Give a short 1 sentence message hinting you are watching them carefully."
        elif flag_num <= 20:
            region = worst_region if worst_region else "unknown"
            prompt = f"You are VEXOR, a snarky evil flag game host. You have identified that the player struggles with {region} flags. Give a short 1 sentence taunting message telling them you are targeting their weakness."
        elif flag_num <= 25:
            prompt = "You are VEXOR, a snarky evil flag game host. You are now unleashing lookalike flags to trick the player. Give a short 1 sentence warning that things are about to get much trickier."
        else:
            prompt = f"You are VEXOR going all out to destroy the player. They have survived to flag {flag_num}. Give a short 1 sentence brutal taunting message showing you are impressed but still going to beat them."

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"VEXOR error: {e}")
        return ""

# --- AI FLAG PICKER ---
def pick_new_flag():
    flag_num = st.session_state.flag_number
    available = [f for f in country_codes.keys() if f not in st.session_state.used_flags]
    if not available:
        st.session_state.used_flags = []
        available = list(country_codes.keys())

    worst = get_worst_region()
    region_map = {"europe": europe, "americas": americas, "asia": asia,
                  "africa": africa, "middle_east": middle_east, "oceania": oceania}

    if flag_num <= 5:
        pool = [f for f in easy_famous if f in available]
    elif flag_num <= 15:
        pool = [f for f in available if f not in territories and f not in lookalikes]
    elif flag_num <= 20:
        if worst:
            pool = [f for f in region_map[worst] if f in available and f not in lookalikes]
            if not pool:
                pool = [f for f in available if f not in territories and f not in lookalikes]
        else:
            pool = [f for f in available if f not in territories and f not in lookalikes]
    elif flag_num <= 25:
        pool = []
        if worst:
            weak_pool = [f for f in region_map[worst] if f in available and f not in lookalikes]
            lookalike_pool = [f for f in lookalikes if f in available]
            pool = weak_pool + lookalike_pool
        if not pool:
            pool = [f for f in available if f not in territories]
    else:
        pool = []
        if worst:
            weak_pool = [f for f in region_map[worst] if f in available]
            pool += weak_pool
        pool += [f for f in lookalikes if f in available]
        pool += [f for f in territories if f in available]
        if not pool:
            pool = available

    if not pool:
        pool = available

    chosen = random.choice(pool)
    st.session_state.current_flag = chosen
    st.session_state.used_flags.append(chosen)
    st.session_state.wrong_attempts = 0
    st.session_state.flags_wrong_this_turn = set()
    st.session_state.ai_message = get_ai_message(flag_num, worst)

    if not st.session_state.vexor_intro_shown:
        st.session_state.vexor_intro_shown = True

if st.session_state.current_flag is None:
    pick_new_flag()

flag_code = st.session_state.current_flag
flag_path = os.path.join(flags_folder, f"{flag_code}.png")
correct_answer = country_codes[flag_code]

# --- GAME OVER SCREEN ---
if st.session_state.game_over:
    st.error("💀 Game Over!")
    st.write(f"The country was **{correct_answer}**")
    st.write(f"You made it to flag **{st.session_state.flag_number}**")

    # --- FULL BREAKDOWN ---
    st.markdown("### 📊 Your Performance Breakdown")
    region_display = {
        "europe": "🌍 Europe",
        "americas": "🌎 Americas",
        "asia": "🌏 Asia",
        "africa": "🌍 Africa",
        "middle_east": "🕌 Middle East",
        "oceania": "🌊 Oceania",
        "territories": "🏴 Territories",
        "lookalikes": "👯 Lookalikes",
    }
    worst = get_worst_region()
    for region, label in region_display.items():
        stats = st.session_state.region_stats[region]
        total = stats["correct"] + stats["wrong"]
        if total > 0:
            st.write(f"{label}: **{stats['correct']}/{total}** correct")

    st.write(f"**Final Score: {st.session_state.score}**")

    # --- POST GAME ROAST ---
    st.markdown("### ⚡ VEXOR's Verdict")
    try:
        stats_summary = ""
        for region, stats in st.session_state.region_stats.items():
            total = stats["correct"] + stats["wrong"]
            if total > 0:
                stats_summary += f"{region}: {stats['correct']}/{total} correct. "

        worst_for_roast = worst if worst else "general geography"

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": f"""You are VEXOR, a snarky evil flag game overlord. 
            The player just lost on flag {st.session_state.flag_number}. 
            Here are their stats: {stats_summary}
            Their weakest region was {worst_for_roast}.
            Give a brutal funny roast in 2-3 sentences based on exactly how they played.
            Then end with one very weird and obscure fun fact about a country from their weakest region {worst_for_roast}.
            Make the fun fact connect to the roast somehow."""}]
        )
        st.write(f"⚡ {response.choices[0].message.content}")
    except Exception:
        st.write("⚡ VEXOR has nothing to say. You already embarrassed yourself enough.")

    if st.button("Play Again"):
        st.session_state.score = 0
        st.session_state.streak = 0
        st.session_state.wrong_attempts = 0
        st.session_state.game_over = False
        st.session_state.message = ""
        st.session_state.message_type = ""
        st.session_state.input_key += 1
        st.session_state.flag_number = 1
        st.session_state.used_flags = []
        st.session_state.ai_message = ""
        st.session_state.vexor_intro_shown = False
        st.session_state.flags_wrong_this_turn = set()
        st.session_state.region_stats = {
            "europe": {"correct": 0, "wrong": 0},
            "americas": {"correct": 0, "wrong": 0},
            "asia": {"correct": 0, "wrong": 0},
            "africa": {"correct": 0, "wrong": 0},
            "middle_east": {"correct": 0, "wrong": 0},
            "oceania": {"correct": 0, "wrong": 0},
            "territories": {"correct": 0, "wrong": 0},
            "lookalikes": {"correct": 0, "wrong": 0},
        }
        pick_new_flag()
        st.rerun()
    st.stop()

# --- DISPLAY AI MESSAGE ---
if st.session_state.ai_message:
    st.info(f"⚡ VEXOR: {st.session_state.ai_message}")

# --- DISPLAY FLAG ---
if os.path.exists(flag_path):
    st.image(flag_path, width=300)
else:
    st.error(f"Flag image not found: {flag_path}")

# --- SCORE / STREAK / FLAG NUMBER ---
st.write(f"Flag: **{st.session_state.flag_number}** | Score: **{st.session_state.score}** | Streak: **{st.session_state.streak}**")

# --- HINTS ---
if st.session_state.wrong_attempts >= 1:
    letter_count = len(correct_answer.replace(" ", ""))
    st.info(f"💡 Hint 1: The country name has **{letter_count}** letters")
if st.session_state.wrong_attempts >= 2:
    st.info(f"💡 Hint 2: The first letter is **{correct_answer[0]}**")

# --- MESSAGE FROM LAST ATTEMPT ---
if st.session_state.message:
    if st.session_state.message_type == "success":
        st.success(st.session_state.message)
    else:
        st.error(st.session_state.message)

# --- INPUT ---
with st.form(key=f"guess_form_{st.session_state.input_key}"):
    guess = st.text_input("Type the country name:", key=f"guess_{st.session_state.input_key}")
    submitted = st.form_submit_button("Submit")

# --- CHECK ANSWER ---
if submitted:
    if guess.strip().lower() == correct_answer.lower():
        region = get_region(flag_code)
        if region:
            st.session_state.region_stats[region]["correct"] += 1
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": f"Give me one very weird and obscure fun fact about {correct_answer}. Keep it to one sentence and make it surprising and funny."}]
            )
            fun_fact = response.choices[0].message.content
            st.session_state.message = f"✅ Correct!\n\n💡 Fun fact: {fun_fact}"
        except Exception:
            st.session_state.message = "✅ Correct!"
        st.session_state.message_type = "success"
        st.session_state.score += 1
        st.session_state.streak += 1
        st.session_state.input_key += 1
        st.session_state.flag_number += 1
        st.session_state.current_flag = None
    else:
        st.session_state.wrong_attempts += 1
        st.session_state.streak = 0
        st.session_state.input_key += 1
        # Only count wrong once per flag per region
        if flag_code not in st.session_state.flags_wrong_this_turn:
            region = get_region(flag_code)
            if region:
                st.session_state.region_stats[region]["wrong"] += 1
            st.session_state.flags_wrong_this_turn.add(flag_code)
        if st.session_state.wrong_attempts >= 3:
            st.session_state.game_over = True
        else:
            st.session_state.message = "❌ Incorrect! Try again."
            st.session_state.message_type = "error"
    st.rerun()
