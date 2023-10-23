import speech_recognition as sr
from deep_translator import GoogleTranslator as Trans
import gtts as toSpeech
from playsound import playsound as play


recog = sr.Recognizer()
trans = Trans(source='auto', target='en')
# print(toSpeech.lang.tts_langs())

def convertNow(path, lang = 'en'):
    with sr.AudioFile(path) as src:
        print('reading from the file: ' + path)
        listened = recog.listen(src)
        try:
            print('doing audio to text conversion..')
            text = str(recog.recognize_google(listened, language = lang))
            printNow(text)
            print('\nnow translating the text..')
            translated = trans.translate(text)
            printNow(translated)
            print('\nnow doing text to speech conversion..')
            spoken = toSpeech.gTTS(translated, lang = 'en')
            print('\nnow saving the final audio..')
            spoken.save('text.mp3')
            print('\nnow playing..')
            play('text.mp3')
        except:
            print('failed!')

def printNow(text):
    print('Text:\n\n')
    print('-'*100)
    print(text)
    print('\n\n')
    print('-'*100)

if __name__ == '__main__':
    path = str(input('Path: '))
    if path == '':
        print('no path given!!')
        exit()
    convertNow(path)
    print('\nDone.')
