#!/usr/bin/python3

# aboutUS
#print()runkahranseur
def intro(intro_string):
        if len(intro_string) % 2 != 0:
            intro_string = intro_string + " "
            
        space = int((36 - len(intro_string)) / 2) * " "

        tds = "%%%"

        long_line = "\t" + "%" * 42 + "\n"

        mid_line = "\t" + tds + (" " * 36) + tds + "\n"

        title_line = "\t%s%s%s%s%s\n"  % (tds, space, intro_string, space, tds)

        showme = long_line + mid_line + title_line + mid_line + long_line
        print(showme)


intro("RUNKAH")

AoO=[]

bio = "\n\t\tRunkah\n"
