import requests
import asyncio
from telegram import Bot
from telegram.error import TelegramError

BOT_TOKEN = "8749703702:AAgsIFEXk6HfbcGCdLfHyqsdfcISvTNIq64"
CHAT_ID = "8467386285"  # ← ID LU UDAH GUE MASUKIN

bot = Bot(token=BOT_TOKEN)

def get_eth_price():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
        data = requests.get(url, timeout=10).json()
        return data['ethereum']['usd']
    except:
        return None

async def main():
    await bot.send_message(chat_id=CHAT_ID, text="Bot ETH Nurdi udah ON bro! 🚀\nBakal ngabarin kalo harga naik/turun $10")
    last_price = get_eth_price()
    
    while True:
        try:
            price = get_eth_price()
            if price and last_price:
                selisih = abs(price - last_price)
                if selisih >= 10:  # Notif kalo berubah $10
                    arah = "NAIK 📈" if price > last_price else "TURUN 📉"
                    await bot.send_message(
                        chat_id=CHAT_ID, 
                        text=f"ETH {arah} ${selisih:.0f}\nHarga: ${price:,.2f}"
                    )
                    last_price = price
            await asyncio.sleep(60)  # Cek tiap 1 menit
        except TelegramError:
            await asyncio.sleep(60)
        except:
            await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())