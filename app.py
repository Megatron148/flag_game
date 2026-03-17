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

# --- FLAG FOLDER ---
flags_folder = "flags"

# --- ALL COUNTRIES / TERRITORIES ---
country_codes = {
    "ad": "Andorra",
    "ae": "United Arab Emirates",
    "af": "Afghanistan",
    "ag": "Antigua and Barbuda",
    "ai": "Anguilla",
    "al": "Albania",
    "am": "Armenia",
    "ao": "Angola",
    "aq": "Antarctica",
    "ar": "Argentina",
    "as": "American Samoa",
    "at": "Austria",
    "au": "Australia",
    "aw": "Aruba",
    "ax": "Aland Islands",
    "az": "Azerbaijan",
    "ba": "Bosnia and Herzegovina",
    "bb": "Barbados",
    "bd": "Bangladesh",
    "be": "Belgium",
    "bf": "Burkina Faso",
    "bg": "Bulgaria",
    "bh": "Bahrain",
    "bi": "Burundi",
    "bj": "Benin",
    "bl": "Saint Barthelemy",
    "bm": "Bermuda",
    "bn": "Brunei",
    "bo": "Bolivia",
    "bq": "Caribbean Netherlands",
    "br": "Brazil",
    "bs": "Bahamas",
    "bt": "Bhutan",
    "bw": "Botswana",
    "by": "Belarus",
    "bz": "Belize",
    "ca": "Canada",
    "cc": "Cocos Islands",
    "cd": "DR Congo",
    "cf": "Central African Republic",
    "cg": "Republic of the Congo",
    "ch": "Switzerland",
    "ci": "Ivory Coast",
    "ck": "Cook Islands",
    "cl": "Chile",
    "cm": "Cameroon",
    "cn": "China",
    "co": "Colombia",
    "cr": "Costa Rica",
    "cu": "Cuba",
    "cv": "Cape Verde",
    "cw": "Curacao",
    "cx": "Christmas Island",
    "cy": "Cyprus",
    "cz": "Czech Republic",
    "de": "Germany",
    "dj": "Djibouti",
    "dk": "Denmark",
    "dm": "Dominica",
    "do": "Dominican Republic",
    "dz": "Algeria",
    "ec": "Ecuador",
    "ee": "Estonia",
    "eg": "Egypt",
    "eh": "Western Sahara",
    "er": "Eritrea",
    "es": "Spain",
    "et": "Ethiopia",
    "fi": "Finland",
    "fj": "Fiji",
    "fk": "Falkland Islands",
    "fm": "Micronesia",
    "fo": "Faroe Islands",
    "fr": "France",
    "ga": "Gabon",
    "gb": "United Kingdom",
    "gb-eng": "England",
    "gb-nir": "Northern Ireland",
    "gb-sct": "Scotland",
    "gb-wls": "Wales",
    "gd": "Grenada",
    "ge": "Georgia",
    "gf": "French Guiana",
    "gg": "Guernsey",
    "gh": "Ghana",
    "gi": "Gibraltar",
    "gl": "Greenland",
    "gm": "Gambia",
    "gn": "Guinea",
    "gp": "Guadeloupe",
    "gq": "Equatorial Guinea",
    "gr": "Greece",
    "gs": "South Georgia",
    "gt": "Guatemala",
    "gu": "Guam",
    "gw": "Guinea-Bissau",
    "gy": "Guyana",
    "hk": "Hong Kong",
    "hm": "Heard Island",
    "hn": "Honduras",
    "hr": "Croatia",
    "ht": "Haiti",
    "hu": "Hungary",
    "id": "Indonesia",
    "ie": "Ireland",
    "il": "Israel",
    "im": "Isle of Man",
    "in": "India",
    "io": "British Indian Ocean Territory",
    "iq": "Iraq",
    "ir": "Iran",
    "is": "Iceland",
    "it": "Italy",
    "je": "Jersey",
    "jm": "Jamaica",
    "jo": "Jordan",
    "jp": "Japan",
    "ke": "Kenya",
    "kg": "Kyrgyzstan",
    "kh": "Cambodia",
    "ki": "Kiribati",
    "km": "Comoros",
    "kn": "Saint Kitts and Nevis",
    "kp": "North Korea",
    "kr": "South Korea",
    "kw": "Kuwait",
    "ky": "Cayman Islands",
    "kz": "Kazakhstan",
    "la": "Laos",
    "lb": "Lebanon",
    "lc": "Saint Lucia",
    "li": "Liechtenstein",
    "lk": "Sri Lanka",
    "lr": "Liberia",
    "ls": "Lesotho",
    "lt": "Lithuania",
    "lu": "Luxembourg",
    "lv": "Latvia",
    "ly": "Libya",
    "ma": "Morocco",
    "mc": "Monaco",
    "md": "Moldova",
    "me": "Montenegro",
    "mg": "Madagascar",
    "mh": "Marshall Islands",
    "mk": "North Macedonia",
    "ml": "Mali",
    "mm": "Myanmar",
    "mn": "Mongolia",
    "mo": "Macau",
    "mp": "Northern Mariana Islands",
    "mq": "Martinique",
    "mr": "Mauritania",
    "ms": "Montserrat",
    "mt": "Malta",
    "mu": "Mauritius",
    "mv": "Maldives",
    "mw": "Malawi",
    "mx": "Mexico",
    "my": "Malaysia",
    "mz": "Mozambique",
    "na": "Namibia",
    "nc": "New Caledonia",
    "ne": "Niger",
    "nf": "Norfolk Island",
    "ng": "Nigeria",
    "ni": "Nicaragua",
    "nl": "Netherlands",
    "no": "Norway",
    "np": "Nepal",
    "nr": "Nauru",
    "nu": "Niue",
    "nz": "New Zealand",
    "om": "Oman",
    "pa": "Panama",
    "pe": "Peru",
    "pf": "French Polynesia",
    "pg": "Papua New Guinea",
    "ph": "Philippines",
    "pk": "Pakistan",
    "pl": "Poland",
    "pm": "Saint Pierre and Miquelon",
    "pn": "Pitcairn Islands",
    "pr": "Puerto Rico",
    "ps": "Palestine",
    "pt": "Portugal",
    "pw": "Palau",
    "py": "Paraguay",
    "qa": "Qatar",
    "re": "Reunion",
    "ro": "Romania",
    "rs": "Serbia",
    "ru": "Russia",
    "rw": "Rwanda",
    "sa": "Saudi Arabia",
    "sb": "Solomon Islands",
    "sc": "Seychelles",
    "sd": "Sudan",
    "se": "Sweden",
    "sg": "Singapore",
    "sh": "Saint Helena",
    "si": "Slovenia",
    "sk": "Slovakia",
    "sl": "Sierra Leone",
    "sm": "San Marino",
    "sn": "Senegal",
    "so": "Somalia",
    "sr": "Suriname",
    "ss": "South Sudan",
    "st": "Sao Tome and Principe",
    "sv": "El Salvador",
    "sx": "Sint Maarten",
    "sy": "Syria",
    "sz": "Eswatini",
    "tc": "Turks and Caicos Islands",
    "td": "Chad",
    "tf": "French Southern Territories",
    "tg": "Togo",
    "th": "Thailand",
    "tj": "Tajikistan",
    "tk": "Tokelau",
    "tl": "Timor-Leste",
    "tm": "Turkmenistan",
    "tn": "Tunisia",
    "to": "Tonga",
    "tr": "Turkey",
    "tt": "Trinidad and Tobago",
    "tv": "Tuvalu",
    "tw": "Taiwan",
    "tz": "Tanzania",
    "ua": "Ukraine",
    "ug": "Uganda",
    "us": "United States",
    "uy": "Uruguay",
    "uz": "Uzbekistan",
    "va": "Vatican City",
    "vc": "Saint Vincent and the Grenadines",
    "ve": "Venezuela",
    "vg": "British Virgin Islands",
    "vi": "U.S. Virgin Islands",
    "vn": "Vietnam",
    "vu": "Vanuatu",
    "wf": "Wallis and Futuna",
    "ws": "Samoa",
    "xk": "Kosovo",
    "ye": "Yemen",
    "yt": "Mayotte",
    "za": "South Africa",
    "zm": "Zambia",
    "zw": "Zimbabwe"
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

# --- FLAG SELECTION ---
def pick_new_flag():
    st.session_state.current_flag = random.choice(list(country_codes.keys()))
    st.session_state.wrong_attempts = 0
    st.session_state.message = ""
    st.session_state.message_type = ""

if st.session_state.current_flag is None:
    pick_new_flag()

flag_code = st.session_state.current_flag
flag_path = os.path.join(flags_folder, f"{flag_code}.png")
correct_answer = country_codes[flag_code]

# --- GAME OVER SCREEN ---
if st.session_state.game_over:
    st.error("💀 Game Over!")
    st.write(f"The country was **{correct_answer}**")
    st.write(f"Final Score: **{st.session_state.score}**")
    if st.button("Play Again"):
        st.session_state.score = 0
        st.session_state.streak = 0
        st.session_state.wrong_attempts = 0
        st.session_state.game_over = False
        st.session_state.message = ""
        st.session_state.message_type = ""
        st.session_state.input_key += 1
        pick_new_flag()
        st.rerun()
    st.stop()

# --- DISPLAY FLAG ---
if os.path.exists(flag_path):
    st.image(flag_path, width=300)
else:
    st.error(f"Flag image not found: {flag_path}")

# --- SCORE / STREAK DISPLAY ---
st.write(f"Score: **{st.session_state.score}** | Streak: **{st.session_state.streak}**")

# --- HINTS ---
if st.session_state.wrong_attempts >= 1:
    letter_count = len(correct_answer.replace(" ", ""))
    st.info(f"💡 Hint: The country name has **{letter_count}** letters")
if st.session_state.wrong_attempts >= 2:
    st.info(f"💡 Hint: The first letter is **{correct_answer[0]}**")

# --- MESSAGE FROM LAST ATTEMPT ---
if st.session_state.message:
    if st.session_state.message_type == "success":
        st.success(st.session_state.message)
    else:
        st.error(st.session_state.message)

# --- INPUT ---
guess = st.text_input("Type the country name:", key=f"guess_{st.session_state.input_key}")

# --- CHECK ANSWER ---
if st.button("Submit"):
    if guess.strip().lower() == correct_answer.lower():
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": f"Give me one very weird and obscure fun fact about {correct_answer}. Keep it to one sentence and make it surprising and funny."}]
            )
            fun_fact = response.choices[0].message.content
            st.session_state.message = f"⚔️ Sliced it! Well done!\n\n💡 Fun fact: {fun_fact}"
        except Exception as e:
            st.session_state.message = f"⚔️ Sliced it! Well done! (AI error: {e})"
        st.session_state.message_type = "success"
        st.session_state.score += 1
        st.session_state.streak += 1
        st.session_state.input_key += 1
        st.session_state.current_flag = random.choice(list(country_codes.keys()))
        st.session_state.wrong_attempts = 0
    else:
        st.session_state.wrong_attempts += 1
        st.session_state.streak = 0
        st.session_state.input_key += 1
        if st.session_state.wrong_attempts >= 3:
            st.session_state.game_over = True
        else:
            st.session_state.message = "❌ Try again!"
            st.session_state.message_type = "error"
    st.rerun()
