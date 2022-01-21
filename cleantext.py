import re

class clean_text():
    a = "Michael Harvey, The Nuts and Bolts of College Writing, Second Edition (Indianapolis, IN: Hackett Publishing, 2013), 70. ↵Etiology is the cause of a disease—what’s actually happening in cells and tissues—while epidemiology is the incidence of a disease in a population. ↵Joseph M. Williams.and Joseph Bizup. Style: Lessons in Clarity and Grace 11th edition (New York: Longman, 2014), 68. Joseph M. Williams and Joseph Bizup. Style: Lessons in Clarity and Grace 11th edition (New York: Longman, 2014), 68. ↵Ibid., 71. ↵The quote uses a version of an ASA-style in-text citation for Mark S. Granovetter, “The Strength of Weak Ties,” American Journal of Sociology 78 (1973): 1360-80. ↵Guiffre. Communities and Networks, 98. ↵Harry Collins and Trevor Pinch, The Golem: What You Should Know About Science 2nd ed. (Cambridge: Canto, 1998), 58. ↵Ibid., 74. ↵"

    def calling(self):
        print(
            '''  1 = Only Alphabetical          ,   2 = Without Alphabetical
                 3 = Only Numeric               ,   4 = Without Numeric
                 5 = Only special Characters    ,   6 = Without special Characters''')
        inp = int(input("Which data u wantfrom paragraph : "))
        if inp == 1 :
            cd.wialp()
            print("--------------------------------------------------------")
            cd.calling()
            
        elif inp == 2 :
            cd.woalp()  
            print("--------------------------------------------------------")
            cd.calling()
        elif inp == 3 :
            cd.winu()  
            print("--------------------------------------------------------")
            cd.calling()  
        elif inp == 4 :
            cd.wonu()  
            print("--------------------------------------------------------")
            cd.calling()
        elif inp == 5 :
            cd.wispch()
            print("--------------------------------------------------------")
            cd.calling()  
        elif inp == 6 :
            cd.wospch()  
            print("--------------------------------------------------------")
            cd.calling()
        else:
            print("Please Enter Correct Input : ")
            cd.calling()

    def wospch(self):
        pat1 = re.sub("\W\s","",self.a)
        print(pat1)

    def wispch(self):
        pat2 = re.sub("\w","",self.a)
        print(pat2)

    def wonu(self):
        pat3 = re.sub("\d","",self.a)
        print(pat3)

    def winu(self):
        pat4 = re.sub("\D","",self.a)
        print(pat4)

    def woalp(self):
        pat5 = re.sub("[a-zA-Z]","",self.a)
        print(pat5)

    def wialp(self):
        pat6 = re.sub("[^a-zA-Z]","",self.a)
        print(pat6)

cd = clean_text()  
cd.calling()    