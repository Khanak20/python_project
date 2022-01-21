import random
def ques2():
    len1 = int(input("Enter length of password : "))
    def QUES():
        if len1 == 1 or len1 == 2:
            pass2()
        elif len1 == 0:
            ques2()
        elif len1 > 2:
            pass3()
        else:
            QUES()

    def pass3():
        a = "1234567890"
        b = 'qwertyuiopasdfghjklzxcvbnm'
        c = "!@#$%^&*()"
        t = random.randrange(20,50)
        x = int((len1*t)/100)
        # y = int((len1*40)/100)
        z = int((len1*t)/100)
        d = []
        e = []
        f = []
        d = random.sample(a,x)
        e = random.sample(b,len(b))
        f = random.sample(c,z)
        all = []
        all1 = []
        all1.extend(e)

        all.extend(d)
        all.extend(f)
        # print(all)
        len2 = len1 - len(all)

        p = random.sample(all , len(all))
        q = random.sample(all1 , len2)
        r = p + q
        print(random.sample(r , len(r)))
        ques2()

    def pass2():
        all2 = '1234567890qwertyuiopasdfghjklzxcvbnm,!@#$%^&*()_+'
        if len1 == 2 or len1 == 1:
            print(random.sample(all2,len1))
        ques2()

    QUES()
    pass3()
    pass2()
ques2()