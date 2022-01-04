import random
import playsound
from gtts import gTTS# Подключение модуля
import speech_recognition as sr

# Ожидание голосовой команды
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Скажите команду:")
        audio = r.listen(source)

    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return 'error'
    except sr.RequestError:
        return 'error'

# Озвучивание текста
def say(text):
    voice = gTTS(text, lang = "ru")
    uniq_filename = "audio_" + str(random.randint(0, 100000)) + ".mp3"
    voice.save(uniq_filename)

    playsound.playsound(uniq_filename)

    print("Ассистент: ", text)

# Обработать полученное сообщение
def handle_message(message):
    if "привет" in message:
        say("Привет привет")
    elif "Прощай" in message:
        finish()
    else:
        say("Я такой команды не знаю")

# Закрытие нашей программы
def finish():
    say('Пока')
    exit()

if __name__ == '__main__':
    print("Test")

    while True:
        command = listen()
        handle_message(command)
