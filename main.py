"""
todo
-use datetime interval to detect how many minutes have passed. don't directly subtract minutes
"""

from tkinter import *
from PIL import ImageTk
from PIL import Image
from pygame import mixer as mi
import datetime
import os

root = Tk()
answer_list = []
edited_answer_list = []
german = ["die Krawatte", "die Jeans", "das Kleid", "der Schal", "die Tasche",
          "der Schuh", "der Anorak", "der Pullover", "die Mütze", "der Mantel",
          "die Jacke", "der Hut", "die Shorts", "der Gürtel", "die Brille",
          "der Stiefel", "das Hemd", "der Rock", "das T-Shirt", "der Anzug"]
edited_german = []
results = []
texts = []
ini = []


class Main:

    def __init__(self):
        answer_list[:] = []
        edited_answer_list[:] = []
        image_names.counter = 0

        l1 = Label(root, text="German clothes quiz with pictures", font=(None, 23), width=30, height=5)
        l1.grid(row=0, column=0, pady=70, padx=15)

        b1 = Button(root, text="Start", font=(None, 16), height=1, width=6, command=(lambda: (
            l1.grid_forget(), b1.grid_forget(), b2.grid_forget(), b3.grid_forget(), self.main_page())))
        b1.grid(row=1, column=0)

        b2 = Button(root, text="Help", font=(None, 14), height=1, width=6, command=(
            lambda: (l1.grid_forget(), b1.grid_forget(), b2.grid_forget(), b3.grid_forget(), self.help_page())))
        b2.grid(row=2, column=0)

        b3 = Button(root, text="Exit'", font=(None, 12), height=0, width=6, command=root.quit)
        b3.grid(row=3, column=0)

        # to prevent errors defined under init
        img = None
        self.sound_pic = ImageTk.PhotoImage(Image.open(self.resource_path("img/sound.png")).resize((25,20)))
        self.number_text = Label(root, text=str(image_names.counter)+"/20")
        self.label_image = Label(root, image=img)
        self.answer = StringVar()
        self.cevk = None

    def help_page(self):
        l1 = Label(root, text="•Ekranda beliren resmin almanca \nkarşılığını artikeliyle birlikte yazınız.", font=(None, 15))
        l1.grid(row=0, column=0, sticky="w", pady=30, padx=80)

        l2 = Label(root, text="•Cevabı yazdıktan sonra kontrol edip diğer \nresme geçmek için 'Tamam' tuşuna basın.", font=(None, 15))
        l2.grid(row=1, column=0, sticky="w", pady=30, padx=80)

        l3 = Label(root, text="•Almanca kelimenin telaffuzunu duymak \niçin hemen yanındaki 'ses' tuşuna basın.", font=(None, 15))
        l3.grid(row=2, column=0, sticky="w", pady=30, padx=80)

        b1 = Button(root, text="< Ana menü", font=(None,15), command=(lambda: (l1.grid_forget(), l2.grid_forget(), l3.grid_forget(), b1.grid_forget(), self.__init__())))
        b1.grid(row=3, column=0,sticky="sw", pady=120)

    def results(self):
        for x in range(0, 20):
            if edited_answer_list[x] == edited_german[x]:
                z = 1
                results.append(z)
            elif edited_answer_list[x] == '':
                z = 10
                results.append(z)
            elif edited_answer_list[x] != edited_german[x]:
                z = 0
                results.append(z)

    def final_text(self):
        for x in range(0, 20):
            if len(answer_list[x]) > 10:
                self.cevk = True
            if len(answer_list[x]) > 12:
                answer_list[x] = answer_list[x][0: 12:] + answer_list[x][len(answer_list[x]) + 1::]
            if results[x] == 1:
                texts.insert(x,str(x+1) + "- '" + answer_list[x] + "' cevabın doğru.")
            if results[x] == 0:
                texts.insert(x,str(x+1) + "- '"+ answer_list[x] + "' cevabın yanlış. Doğru cevap: " + german[x])
            if results[x] == 10:
                texts.insert(x,str(x+1) + "- Boş bıraktın. Doğru cevap: " + german[x])

    def true_false_screen(self):
        current = image_names.counter - 1

        l1 = Label(root, text="", font=(None, 14))
        l1.grid(row=0,column=0,padx=175, pady=80)

        bm = Button(root, image=self.sound_pic, command=so.t_f_screen)
        bm.grid(column=0, row=0, padx=135,sticky="e", ipadx=5,ipady=6)

        b1 = Button(root, text="Sıradaki >", font=(None, 13), command=(lambda: (l1.grid_forget(), b1.grid_forget(), bm.grid_forget(),
                                                                                self.main_page() if current < 19 else (
                                                                                l1.grid_forget(), b1.grid_forget(),
                                                                                self.final_page(), self.stop_time()))))
        b1.grid(row=1, column=0, sticky="s", pady=250,padx=30)

        if edited_answer_list[current] == edited_german[current]:
            l1.configure(text="Cevabın doğru             ")
            b1.grid_configure(padx=60, pady=275)
        elif edited_answer_list[current] == "":
            l1.configure(text="Boş bıraktın. \n Doğru cevap: "+german[current])
        elif edited_answer_list[current] != edited_german[current]:
            l1.configure(text="Cevabın yanlış. \n Doğru cevap: "+german[current])

        if current == 19:
            b1.configure(text="Bitir ✗")

        if current == 0:
            self.start = datetime.datetime.now()

    def stop_time(self):
        self.stop = datetime.datetime.now()
        completion_time = (self.stop - self.start).seconds
        minute = completion_time//60
        second = completion_time%60
        return "{} dakika {} saniyede bitirdin".format(minute,second)

    def answers(self):
        ans = self.answer.get()
        answer_list.append(ans)
        edited_answer_list.append((ans.lower()).replace(" ", ""))
        if len(answer_list) < 2:
            for x in german:
                edited_german.append((x.lower()).replace(" ", ""))

#    def resource_path(self, relative_path):
#        if hasattr(sys, '_MEIPASS'):
#            return os.path.join(sys._MEIPASS, relative_path)
#        return os.path.join(os.path.abspath("."), relative_path)

    def resource_path(self, relative_path):
        try: 
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def name_counter(self):
        image_names.counter += 1
        img = ImageTk.PhotoImage(Image.open(self.resource_path("img/{}.png".format(image_names.counter))).resize((500, 400)))

        self.label_image.configure(image=img)
        self.label_image.image = img

        self.number_text.configure(text=str(image_names.counter)+"/20")

        return int(image_names.counter)

    def are_you_sure(self):
        l1 = Label(root, text="Emin misin? İlerlemen kaybolacaktır.", font=(None, 15))
        l1.grid(row=1, column=2, pady=30)

        b1 = Button(root, font=(None, 20), text="✓", command=(lambda: (l1.grid_forget(), b1.grid_forget(),b2.grid_forget(), self.__init__())))
        b1.grid(row=2, column=1, ipadx=10)

        b2 = Button(root, font=(None, 20), text="✗", command=(lambda: (l1.grid_forget(), b1.grid_forget(),b2.grid_forget(), self.main_page())))
        b2.grid(row=2, column=3, ipadx=10)

        image_names.counter -= 1

    def main_page(self):
        buttonframe = Frame(root)
        buttonframe.grid(row=2, column=1,sticky="w")

        img = ImageTk.PhotoImage(Image.open(self.resource_path("img/{}.png".format(self.name_counter()))).resize((500, 400)))

        self.label_image = Label(root, image=img)
        self.label_image.image = img  # keep a reference
        self.label_image.grid(row=0, column=1, padx=50)

        e1 = Entry(root, bd=4, textvariable=self.answer)
        e1.grid(row=1, column=1, ipady=3, pady=5)

        b1 = Button(root, text="Tamam ✓", font=(None, 13), command=(lambda: (self.answers(), buttonframe.grid_forget(), self.true_false_screen(), e1.delete(0, END),self.label_image.grid_forget(),e1.grid_forget(),b1.grid_forget(),b2.grid_forget(),self.number_text.grid_forget(),buttonframe.grid_forget())))
        b1.grid(row=2, column=1, pady=15)

        b2 = Button(buttonframe, text="< Ana menü", font=(None, 13), command=(lambda: (self.label_image.grid_forget(),self.number_text.grid_forget(),
                                                                                       e1.grid_forget(), b1.grid_forget(), b2.grid_forget(), self.are_you_sure())))
        b2.grid(row=0, column=0)

        self.number_text.grid(row=0,column=1,sticky="ne",padx=15)

        # useless feature
        #b3 = Button(eastframe, text="Bitir ✗", font=(None, 13))
        #b3.grid(column=0, row=0)

    def final_page(self):
        if len(ini) < 1:
            ini.append("")
            self.results()
            self.final_text()

        root.geometry('{}x{}'.format(650, 600))

        a0 = Label(root, text=(texts[0]))
        a0.grid(column=0,row=0,pady=6,sticky="w")

        a1 = Label(root, text=(texts[1]))
        a1.grid(column=0, row=1, pady=2, sticky="w")

        a2 = Label(root, text=(texts[2]))
        a2.grid(column=0, row=2, pady=4, sticky="w")

        a3 = Label(root, text=(texts[3]))
        a3.grid(column=0, row=3, pady=4, sticky="w")

        a4 = Label(root, text=(texts[4]))
        a4.grid(column=0, row=4, pady=4, sticky="w")

        a5 = Label(root, text=(texts[5]))
        a5.grid(column=0, row=5, pady=4, sticky="w")

        a6 = Label(root, text=(texts[6]))
        a6.grid(column=0, row=6, pady=4, sticky="w")

        a7 = Label(root, text=(texts[7]))
        a7.grid(column=0, row=7, pady=4, sticky="w")

        a8 = Label(root, text=(texts[8]))
        a8.grid(column=0, row=8, pady=4, sticky="w")

        a9 = Label(root, text=(texts[9]))
        a9.grid(column=0, row=9, pady=4, sticky="w")

        a10 = Label(root, text=(texts[10]))
        a10.grid(column=0, row=10, pady=4, sticky="w")

        a11 = Label(root, text=(texts[11]))
        a11.grid(column=0, row=11, pady=4, sticky="w")

        a12 = Label(root, text=(texts[12]))
        a12.grid(column=0, row=12, pady=4, sticky="w")

        a13 = Label(root, text=(texts[13]))
        a13.grid(column=0, row=13, pady=4, sticky="w")

        a14 = Label(root, text=(texts[14]))
        a14.grid(column=0, row=14, pady=4, sticky="w")

        a15 = Label(root, text=(texts[15]))
        a15.grid(column=0, row=15, pady=4, sticky="w")

        a16 = Label(root, text=(texts[16]))
        a16.grid(column=0, row=16, pady=4, sticky="w")

        a17 = Label(root, text=(texts[17]))
        a17.grid(column=0, row=17, pady=4, sticky="w")

        a18 = Label(root, text=(texts[18]))
        a18.grid(column=0, row=18, pady=4, sticky="w")

        a19 = Label(root, text=(texts[19]))
        a19.grid(column=0, row=19, pady=4, sticky="w")

        s1 = Button(root, image=self.sound_pic, command=so.s0)
        s1.grid(column=1,row=0)

        s2 = Button(root, image=self.sound_pic, command=so.s1)
        s2.grid(column=1, row=1)

        s3 = Button(root, image=self.sound_pic, command=so.s2)
        s3.grid(column=1, row=2)

        s4 = Button(root, image=self.sound_pic, command=so.s3)
        s4.grid(column=1, row=3)

        s5 = Button(root, image=self.sound_pic, command=so.s4)
        s5.grid(column=1, row=4)

        s6 = Button(root, image=self.sound_pic, command=so.s5)
        s6.grid(column=1, row=5)

        s7 = Button(root, image=self.sound_pic, command=so.s6)
        s7.grid(column=1, row=6)

        s8 = Button(root, image=self.sound_pic, command=so.s7)
        s8.grid(column=1, row=7)

        s9 = Button(root, image=self.sound_pic, command=so.s8)
        s9.grid(column=1, row=8)

        s10 = Button(root, image=self.sound_pic, command=so.s9)
        s10.grid(column=1, row=9)

        s11 = Button(root, image=self.sound_pic, command=so.s10)
        s11.grid(column=1, row=10)

        s12 = Button(root, image=self.sound_pic, command=so.s11)
        s12.grid(column=1, row=11)

        s13 = Button(root, image=self.sound_pic, command=so.s12)
        s13.grid(column=1, row=12)

        s14 = Button(root, image=self.sound_pic, command=so.s13)
        s14.grid(column=1, row=13)

        s15 = Button(root, image=self.sound_pic, command=so.s14)
        s15.grid(column=1, row=14)

        s16 = Button(root, image=self.sound_pic, command=so.s15)
        s16.grid(column=1, row=15)

        s17 = Button(root, image=self.sound_pic, command=so.s16)
        s17.grid(column=1, row=16)

        s18 = Button(root, image=self.sound_pic, command=so.s17)
        s18.grid(column=1, row=17)

        s19 = Button(root, image=self.sound_pic, command=so.s18)
        s19.grid(column=1, row=18)

        s20 = Button(root, image=self.sound_pic, command=so.s19)
        s20.grid(column=1, row=19)

        plus_button = Button(root, text="Sonraki sayfa >", font=(None,15), command=(lambda: (a0.grid_forget(),a1.grid_forget(),a2.grid_forget(),a3.grid_forget(),a4.grid_forget(),a5.grid_forget(),
                                                                               a6.grid_forget(),a7.grid_forget(),a8.grid_forget(),a9.grid_forget(),a10.grid_forget(),a11.grid_forget(),
                                                                               a12.grid_forget(),a13.grid_forget(),a14.grid_forget(),a15.grid_forget(),a16.grid_forget(),a17.grid_forget(),a18.grid_forget(),
                                                                               a19.grid_forget(),s1.grid_forget(),s2.grid_forget(),s3.grid_forget(),s4.grid_forget(),s5.grid_forget(),s6.grid_forget(),
                                                                               s7.grid_forget(),s8.grid_forget(),s9.grid_forget(),s10.grid_forget(),s11.grid_forget(),s12.grid_forget(),s13.grid_forget(),
                                                                               s14.grid_forget(),s15.grid_forget(),s16.grid_forget(),s17.grid_forget(),s18.grid_forget(),s19.grid_forget(),s20.grid_forget(),
                                                                               plus_button.grid_forget(),self.final_page_plus())))
        plus_button.grid(column=2,row=19, padx=80, rowspan=5, sticky="se")

        if self.cevk == True:
            plus_button.configure(font=(None,13))
            plus_button.grid_configure(padx=10)

    def final_page_plus(self):
        root.geometry('{}x{}'.format(600, 500))
        crono = self.stop_time()

        true = 0
        false = 0
        empty = 0

        for x in results:
            if x == 1:
                true += 1
            elif x == 0:
                false += 1
            elif x == 10:
                empty += 1

        l1 = Label(root, text="Tebrikler! Quizi;", font=(None, 15))
        l1.grid(row=0, column=1,pady=30,padx=0)

        tf_ratio = Label(root, text=("• " + str(true) + " doğru, " + str(false) + " yanlış, " + str(empty) + " boş cevap ile "), font=(None, 13))
        tf_ratio.grid(row=1,column=1)

        tme = Label(root, text=crono, font=(None, 13))
        tme.grid(row=2,column=1)

        b1 = Button(root,text="< Önceki sayfa", font=(None,13), command=(lambda: (l1.grid_forget(), tf_ratio.grid_forget(), tme.grid_forget(), b1.grid_forget(),b2.grid_forget(),b3.grid_forget(), sign_text.grid_forget(), self.final_page())))
        b1.grid(row=3, column=0, rowspan=5, sticky="sw", pady=320)

        b2 = Button(root,text="Ana menü ↺", font=(None,14),command=(lambda: (l1.grid_forget(), tf_ratio.grid_forget(), tme.grid_forget(), b1.grid_forget(),b2.grid_forget(),b3.grid_forget(), sign_text.grid_forget(),self.__init__())))
        b2.grid(row=3,column=1,pady=320, padx=60)

        b3 = Button(root,text="Çıkış ✗", font=(None,14), command=root.quit)
        b3.grid(row=3,column=2,pady=120)

        sign_text = Label(root, text="2019-07 @ Onur Alp Akın")
        sign_text.grid(row=0, column=0, rowspan=5, sticky="nw")


class Sounds:
    def __init__(self):
        mi.init()

    def t_f_screen(self):
        mi.music.load(main.resource_path("sound/{}.ogg".format(image_names.counter)))
        mi.music.play()

    def s0(self):
        mi.music.load(main.resource_path("sound/1.ogg"))
        mi.music.play()

    def s1(self):
        mi.music.load(main.resource_path("sound/2.ogg"))
        mi.music.play()

    def s2(self):
        mi.music.load(main.resource_path("sound/3.ogg"))
        mi.music.play()

    def s3(self):
        mi.music.load(main.resource_path("sound/4.ogg"))
        mi.music.play()

    def s4(self):
        mi.music.load(main.resource_path("sound/5.ogg"))
        mi.music.play()

    def s5(self):
        mi.music.load(main.resource_path("sound/6.ogg"))
        mi.music.play()

    def s6(self):
        mi.music.load(main.resource_path("sound/7.ogg"))
        mi.music.play()

    def s7(self):
        mi.music.load(main.resource_path("sound/8.ogg"))
        mi.music.play()

    def s8(self):
        mi.music.load(main.resource_path("sound/9.ogg"))
        mi.music.play()

    def s9(self):
        mi.music.load(main.resource_path("sound/10.ogg"))
        mi.music.play()

    def s10(self):
        mi.music.load(main.resource_path("sound/11.ogg"))
        mi.music.play()

    def s11(self):
        mi.music.load(main.resource_path("sound/12.ogg"))
        mi.music.play()

    def s12(self):
        mi.music.load(main.resource_path("sound/13.ogg"))
        mi.music.play()

    def s13(self):
        mi.music.load(main.resource_path("sound/14.ogg"))
        mi.music.play()

    def s14(self):
        mi.music.load(main.resource_path("sound/15.ogg"))
        mi.music.play()

    def s15(self):
        mi.music.load(main.resource_path("sound/16.ogg"))
        mi.music.play()

    def s16(self):
        mi.music.load(main.resource_path("sound/17.ogg"))
        mi.music.play()

    def s17(self):
        mi.music.load(main.resource_path("sound/18.ogg"))
        mi.music.play()

    def s18(self):
        mi.music.load(main.resource_path("sound/19.ogg"))
        mi.music.play()

    def s19(self):
        mi.music.load(main.resource_path("sound/20.ogg"))
        mi.music.play()


so = Sounds()
main = Main()

root.geometry('{}x{}'.format(600, 500))
root.resizable(width=False, height=False)
root.title("Almanca Kıyafetler")
root.mainloop()
