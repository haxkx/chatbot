from os import getenv

from dotenv import load_dotenv

load_dotenv()

#### ❖ ──────⊱◈◈◈⊰────── ❖
API_ID = int(getenv("API_ID", "6435225"))

#### ❖ ──────⊱◈◈◈⊰────── ❖
API_HASH = getenv("API_HASH", "4e984ea35f854762dcde906dce426c2d")

#### ❖ ──────⊱◈◈◈⊰────── ❖
BOT_TOKEN = getenv("BOT_TOKEN", None)

#### ❖ ──────⊱◈◈◈⊰────── ❖
OWNER_ID = int(getenv("OWNER_ID", "6922271843"))

#### ❖ ──────⊱◈◈◈⊰────── ❖
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Bikash:Bikash@bikash.yl2nhcy.mongodb.net/?retryWrites=true&w=majority")

#### ❖ ──────⊱◈◈◈⊰────── ❖
SUPPORT_GRP = getenv("SUPPORT_GRP", "HAXKX_DISCUSSION")

#### ❖ ──────⊱◈◈◈⊰────── ❖
UPDATE_CHNL = getenv("UPDATE_CHNL", "HAXKX")

#### ❖ ──────⊱◈◈◈⊰────── ❖
OWNER_USERNAME = getenv("OWNER_USERNAME", "TOXIC_TANJJ")

#### ❖ ──────⊱◈◈◈⊰────── ❖
BOT_USERNAME = getenv("BOT_USERNAME", None )


#### ❖ ──────⊱◈◈◈⊰────── ❖

STICKER = [
"CAACAgUAAx0Cd9xEawACEQlmLuvFijxhTZXjFbLPOsZFBoZzYQAC2AUAAkVZsVftrDRpvXZTAAE0BA",
"CAACAgUAAx0Cd9xEawACEQhmLuvFeujHQdaxeDtr3MZThRXa1QACkgcAArZSuVfbJAABQq5pIc80BA",
"CAACAgUAAx0Cd9xEawACEQdmLuvFQdwX-ySKIrmq-JPWItfhhgACwQUAAi9GuVfYV7lLP7xl4zQE",
"CAACAgUAAx0Cd9xEawACEQVmLuuiUNrymw5wWSie-agvZ-_MdgACNAQAAi9GsFf3M2dSfxH-YDQE",
"CAACAgUAAx0Cd9xEawACEQNmLuuKwCEUmunIPFoxUL1Kr2Dp1AAChQgAApAXsFeIwfQvrfbmjjQE",
"CAACAgUAAx0Cd9xEawACEQJmLut22O_5LobAKvCBNlOHbCnQcQAC8gQAAmRQsVdeP26A2AJofzQE",
"CAACAgUAAx0Cd9xEawACEQABZi7rYhnPjPsm_g37JvqoH7qB10gAAsgEAAJWgShXcBbC69nedAY0BA",
"CAACAgUAAx0Cd9xEawACEP9mLutgBdWYCVPqQ_kvUGgYoNVIVwACrAYAAof0IFc6sUwgfJZw6zQE",
"CAACAgEAAx0Cd9xEawACEPtmLusPo3kBvdEigRxbcqGOMSF9cgAC8wMAAqpT6UU55jSF8wAByTc0BA",
"CAACAgEAAx0Cd9xEawACEPpmLusJTIEch-TXN5KsPkvdfnypNgACbwIAAkoY6UUP_O3RGOXeSTQE",
"CAACAgEAAx0Cd9xEawACEPlmLusBSvWNswwz99iOXBMIos0s_QACGAMAAtfI6EX4deIoUongJDQE",
"CAACAgEAAx0Cd9xEawACEPdmLuropCmTrN0Xv4_C7plvS45D3gACrwIAAqyx6EVOdFVb4d8VsDQE",
"CAACAgUAAx0Cd9xEawACEOhmLurMc76ZYy9ZWB0dcuWfNJVSzQACLwUAAk-LuVelZAHYP-pxnTQE",
"CAACAgUAAx0Cd9xEawACEOZmLuq8MMZnoz-txKJ9QEow9qDKxQACKwQAAvbXuVf7GDiuoypXFzQE",
"CAACAgUAAx0Cd9xEawACEORmLuq3Mm3dzamR5W8JZhZHgbPWKwACJwcAAvQcsFefMIzhat8ZtDQE",
"CAACAgUAAx0Cd9xEawACEONmLuqxMsLOLjCsMIf86_QuZH0AAaAAAusMAAIRzNhVUrENdULkjis0BA",
"CAACAgUAAx0Cd9xEawACEOFmLuqryqMN4_7KPq_LLZNIq0OPEgACJAwAAm5mwVXkZ2Ycjy1rRjQE",
"CAACAgUAAx0Cd9xEawACEN9mLuqlG8RAw-L8e1Pv3909WrYMhgACwBUAAh-sOVQ3vSSCUJbSYzQE",
]

#### ❖ ──────⊱◈◈◈⊰────── ❖

IMG = [
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJ7ORcOkqZkBh23HMQw4f44bvoSjwF4M78Oywc1gSNJfOqI8oZtUxNJUM&s=10",
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlMwlBxiHNZjjBWH1g3nDx7jRSJf5hZm6kmg&usqp=CAU",
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTAu1YGPDCfHThB9X1vXwjgEpg3VidBDsna6w&usqp=CAU",
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTi6TDxOZ3aTuracxrNcdaIafStrUUDpji2TA&usqp=CAU",
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTa0RPw8ZfhqHvVD0mF3XDdefYKjtdersHGyA&usqp=CAU",
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmiGjM2hexeyYQED4GOW1T9e5YCZpe2gOrWIU2tuCx5ez6W6MYQ6MBeZs&s=10",
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSu0dZvn4U1JA84tYdhmgJuKhEu-yMQa4b8BA&usqp=CAU",
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6BtCTIFXkcs4V1B4Bz8z3i3UqXW3miFFkMQ&usqp=CAU",
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRQFC1RmpZuoU9LuVzqqQ_CBvmPfzXp9zQpQ&usqp=CAU",
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSTqHhyDLqu307p94Yua7WZ_TCQ8_zFS2CYUQ&usqp=CAU",
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSm1TCsabStxwhN0tgrmDQV1ZWPovg5H2pIbw&usqp=CAU",
"https://graph.org/file/f7f010e1ad4425ed866de.jpg",
]

#### ❖ ──────⊱◈◈◈⊰────── ❖

EMOJIOS = [
    "❤️",
    "🧡",
    "💛",
    "💚",
    "💙",
    "💜",
    "🤎",
    "🖤",
    "🤍",
    "♥️",
]
