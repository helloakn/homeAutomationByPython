#!/usr/local/bin/python3.6
import sys
from optparse import OptionParser #for command line arguments

import pyttsx3 #speaker
from langdetect import detect  #detect language
from googletrans import Translator

LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',
    'fil': 'Filipino',
    'he': 'Hebrew'
}

engine = pyttsx3.init() #engine start

parser = OptionParser()
parser.set_defaults(outputLanguage='en')
try:
	parser.add_option('-o','--outputLanguage',type="string", action='store', dest='outputLanguage')
	parser.add_option('-t','--text',type="string", action='store', dest='inputText')
	#parser.add_argument('-i','--inputLanguage',type="string", action='store', dest='ilanguage')
except Exception:
	pass

(options, args) = parser.parse_args()
#print(options.inputText )	
if( (options.inputText is None) or options.outputLanguage is None):
	print("need more arguments, pls type -h");
	exit()

shortLanguage = {}

voices = engine.getProperty('voices')
for v in voices:
	slng = v.languages[0].split('_')[0]
	if( slng not in shortLanguage):
		shortLanguage[v.languages[0].split('_')[0]] = v.id
	
translator = Translator()
word = options.inputText
inputLanguage = detect(word)
print("your input language is " ,LANGUAGES[inputLanguage])

if( options.outputLanguage not in shortLanguage):
	print ("language supports only the following : ")
	for key, value in shortLanguage.items():
		if( key in LANGUAGES):
			print (key," : ",LANGUAGES[key])
	exit()

tran = translator.translate(word, src=inputLanguage,dest=options.outputLanguage)
word = tran.text
print("I would speak in ",LANGUAGES[options.outputLanguage],".");

#speak
engine.setProperty('voice',shortLanguage[options.outputLanguage])
engine.say(word);
engine.runAndWait()

exit()
