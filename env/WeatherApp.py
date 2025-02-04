#Author: Levi-Tech @Umeskia-Levi
import requests
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext, Application, MessageHandler, filters
#End of Import Section

# API KEYS AND BOT TOKEN SECTION #
API_KEY = '701b74a40aaa9be6d6d3e0129cbbd54b'
TELEGARAM_BOT_TOKEN ='7751378175:AAFm0AJMGE6H4TUD_52D9Cnam0n_UGhH8FM'
# END OF API & TOKEN SECTION #

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Rada Boss !! Send me a city name to get weather Updates on Real-Time.')
#Get Weather Data
def get_weather(city: str) -> dict:
    base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_KEY + "&q=" + city #API URL
    weather_data_response = requests.get(base_url).json()
    return weather_data_response


#Send Weather Updates Real-Time
async def weather(update: Update, context: CallbackContext) -> None:
    city = update.message.text
    weather_data = get_weather(city)
    if weather_data.get('cod') == 200:
        main = weather_data['main']
        weather = weather_data['weather'][0]
        #start of message
        message = ("Thank you For Checking Weather Updates\n"
            f"Weather in {city}:\n"
            f"Temperature: {main['temp']}K\n"
            f"Humidity: {main['humidity']}%\n"
            f"Condition: {weather['description']}"
        )
    else: #Display Error Message
        message = f"City {city} not found."
    await update.message.reply_text(message)

def main():
    application = Application.builder().token(TELEGARAM_BOT_TOKEN).build()
        # Add Handlers
    application.add_handler(CommandHandler("start", start))
        # Add Message Handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, weather))

    application.run_polling()

if __name__ == '__main__':
    main()