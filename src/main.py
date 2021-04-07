import sys
from googletrans import Translator

from .color import *
from .intro import intro

class Main:
    def app():
        # intro
        sys.stdout.write(intro())
        print('    Github Profile - https://github.com/lemun \n\n\n')

        # program start here

        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Choose a language to translate: ')
        print(fc + sd + '[' + fm + sb + '1' + fc + sd + '] ' + fg + 'From: ' + fw + 'English     ' + fg + 'To: ' + fw + 'Hebrew')
        print(fc + sd + '[' + fm + sb + '2' + fc + sd + '] ' + fg + 'From: ' + fw + 'Hebrew     ' + fg + 'To: ' + fw + 'English')
        
        choose_language = 'Number(1/2): '
        choosen_language = input(choose_language)

        if choosen_language == '1':
            instruction = 'Word / Sentence: '
            txt = input(instruction)

            t = Translator(service_urls=['translate.googleapis.com'])
            result = t.translate(txt, src='en', dest='he')
            print(result.text)

        elif choosen_language == '2':
            instruction = 'Word / Sentence: '
            txt = input(instruction)

            t = Translator(service_urls=['translate.googleapis.com'])
            result = t.translate(txt, src='he', dest='en')
            print(result.text)
            
        elif choosen_language != '1':
            print('Exit()')
        
