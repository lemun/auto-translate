import colorama, random, sys

def intro():
    banner = '''
$$$$$$$$\                                     $$\            $$\               
\__$$  __|                                    $$ |           $$ |              
   $$ | $$$$$$\  $$$$$$\  $$$$$$$\   $$$$$$$\ $$ | $$$$$$\ $$$$$$\    $$$$$$\  
   $$ |$$  __$$\ \____$$\ $$  __$$\ $$  _____|$$ | \____$$\\_$$  _|  $$  __$$\ 
   $$ |$$ |  \__|$$$$$$$ |$$ |  $$ |\$$$$$$\  $$ | $$$$$$$ | $$ |    $$$$$$$$ |
   $$ |$$ |     $$  __$$ |$$ |  $$ | \____$$\ $$ |$$  __$$ | $$ |$$\ $$   ____|
   $$ |$$ |     \$$$$$$$ |$$ |  $$ |$$$$$$$  |$$ |\$$$$$$$ | \$$$$  |\$$$$$$$\ 
   \__|\__|      \_______|\__|  \__|\_______/ \__| \_______|  \____/  \_______|
                                                                                                                                                                                                                           
'''

    bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET']
    codes = vars(colorama.Fore)
    colors = [codes[color] for color in codes if color not in bad_colors]
    colored_chars = [random.choice(colors) + char for char in banner]
    

    return ''.join(colored_chars)