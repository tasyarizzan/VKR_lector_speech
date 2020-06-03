from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as mb
from sound2vec2 import Sound2VecModel
from pydub import AudioSegment
from audio_classification import is_speech

DEFAULT_FREQUENCY = 223  # frequency in Hz
DEFAULT_DURATION = 5.0   # length of sound stream in seconds
INTERVAL = 100           # plot interval in millisecond
PACKAGE_LENGTH = 1024    # number of samples in sound package
VOLUME_RESOLUTION = 0.02 # resolution in volume scale (0 - 1)
FILE_SEARCH = r'^([a-zA-Z]:)?([/|\\].+[/|\\])*(.+$)'

class TkSetup:
    def __init__(self, root):
        self.root = root
        self.root.geometry('800x500')

        self.root.title("Анализ речи")
        self.root.columnconfigure(0, weight=1)
        self.root["bg"] = "white"

        self.path = ''
        self.one_channel_path = ''
        self.duration = DEFAULT_DURATION
        self.running = False
        self.stopped = True
        self.error_message = ''

        self.hello()
        self.main_menu()

    def main_menu(self):

        self.menubar = Menu(self.root, tearoff=0, font=("Arial Bold", 15), relief=RAISED)
        self.menubar["bg"] = "black"
        self.root.config(menu=self.menubar)
        self.filemenu = Menu(self.menubar, tearoff=0)

        self.menubar.add_command(label='Открыть файл', command=self.openFile)
        self.menubar.add_separator()

        self.menubar.add_command(label='Записать речь')
        self.menubar.add_separator()

        self.menubar.add_command(label='Анализ', command=self.analiz)
        self.menubar.add_separator()

        self.menubar.add_command(label='Расшифровка анализа')
        self.menubar.add_separator()

        self.menubar.add_command(label='О программе', command=self.hello)
        self.menubar.add_separator()

        self.root.config(menu=self.menubar)

    def clear(self):
        self.list = self.root.pack_slaves()
        for l in self.list:
            l.destroy()
        self.root.geometry('800x500')
        self.main_menu()


    def main_buttons(self):
        self.top_frame = Frame(self.root)
        self.top_frame.pack()
        self.middle_frame = Frame(self.root)
        self.middle_frame.pack()
        self.bottom_frame = Frame(self.root)
        self.bottom_frame.pack()

        self.download_button = Button(
            self.middle_frame, text=' Загрузить файл ', command=self.openFile, font=("Arial Bold", 15))
        self.download_button.pack(side=LEFT, padx=5, pady=10)

        self.text_label = Label(self.middle_frame, text='Или', font=("Arial Bold", 15))
        self.text_label.pack(side=LEFT, padx=5, pady=10)

        self.record_button = Button(
            self.middle_frame, text=' Начать запись ', font=("Arial Bold", 15))
        self.record_button.pack(side=LEFT, padx=5, pady=10)

        self.analiz_button = Button(
            self.bottom_frame, text=' Анализ ', command=self.analiz, font=("Arial Bold", 15), padx=40, pady=3)
        self.analiz_button.pack(side=BOTTOM, padx=5, pady=10,  fill=X, expand=TRUE)

        self.more_button = Button(
            self.top_frame, text=' О программе ', font=("Arial Bold", 15))
        self.more_button.pack(side=RIGHT, padx=5, pady=10, fill=X, expand=TRUE)

        self.shifr_button = Button(
            self.top_frame, text=' Расшифровка анализа ', font=("Arial Bold", 15))
        self.shifr_button.pack(side=RIGHT, padx=5, pady=10, fill=X, expand=TRUE)

    def hello(self):
        self.hello_frame = Frame(self.root)
        self.hello_frame.pack(pady=150, padx=30)


        self.text = Text(self.hello_frame, width=50, height=7, font=("Arial Bold", 15), wrap=WORD, bd=5)
        self.text.insert(INSERT, 'Это приложение создано в рамках ВКР. '
                            'Вы можете проанализировать параметры выразительности речи существующей записи или сделать запись.'
                            'Чтобы начать, выберите файл и нажмите Анализ.'
                            ' Или нажмите начать запись, после остановки записи нажмите Анализ')
        self.text.configure(state='disabled')
        self.text.pack(side=LEFT)




    def analiz(self):
        #тут можно сделать вывод всех параметров

        self.one_frame = Frame(self.root)
        self.one_frame.pack()
        self.two_frame = Frame(self.root)
        self.two_frame.pack()
        self.three_frame = Frame(self.root)
        self.three_frame.pack()
        self.four_frame = Frame(self.root)
        self.four_frame.pack()
        self.five_frame = Frame(self.root)
        self.five_frame.pack()
        self.six_frame = Frame(self.root)
        self.six_frame.pack()
        self.seven_frame = Frame(self.root)
        self.seven_frame.pack()
        self.eight_frame = Frame(self.root)
        self.eight_frame.pack()
        #проверка того, что путь не пустой
        if self.path == '':
            mb.showerror("Ошибка", "Сначала выберите файл или начните запись")
            return

        self.hello_frame.pack_forget()

        sound = AudioSegment.from_wav(self.path)
        sound = sound.set_channels(1)
        self.one_channel_path = self.path[:-4] + '_one.wav'
        sound.export(self.one_channel_path, format="wav")

        voice = Sound2VecModel(self.path)
        volume = Label(
            self.one_frame, text=" Громкость: ", font=("Arial Bold", 15), bg='white', width=20, height=2)
        volume.pack(side=LEFT)

        result_v = Label(
            self.one_frame, text=voice.get_volume(self.one_channel_path), font=("Arial Bold", 15), bg='white', width=20, height=2)
        result_v.pack(side=LEFT)

        monoton = Label(
            self.two_frame, text=" Монотонность: ", font=("Arial Bold", 15), bg='white', width=20, height=2)
        monoton.pack(side=LEFT)

        result_m = Label(
            self.two_frame, text=voice.get_monotone(self.one_channel_path), font=("Arial Bold", 15), bg='white', width=20, height=2)
        result_m.pack(side=LEFT)


        otnoshenie = Label(
            self.three_frame, text=" Соотношение тишина/речь: ", font=("Arial Bold", 15), bg='white', width=30, height=2)
        otnoshenie.pack(side=LEFT)

        result_o = Label(
            self.three_frame, text=voice.get_silens_segm(self.one_channel_path), font=("Arial Bold", 15), bg='white', width=15, height=2)
        result_o.pack(side=RIGHT)

        temp = Label(
            self.four_frame, text=" Темп: ", font=("Arial Bold", 15), bg='white', width=20, height=2)
        temp.pack(side=LEFT)

        result_t = Label(
            self.four_frame, text=voice.get_text(self.one_channel_path), font=("Arial Bold", 15), bg='white', width=20, height=2)
        result_t.pack(side=RIGHT)

        akustik = Label(
            self.five_frame, text=" Акустика: ", font=("Arial Bold", 15), bg='white', width=20, height=2)
        akustik.pack(side=LEFT)

        result_ak = Label(
            self.five_frame, text=voice.get_distnt(self.one_channel_path), font=("Arial Bold", 15), bg='white', width=20, height=2)
        result_ak.pack(side=RIGHT)

        prozrach = Label(
            self.six_frame, text=" Прозрачность звука: ", font=("Arial Bold", 15), bg='white', width=20, height=2)
        prozrach.pack(side=LEFT)

        result_pr = Label(
            self.six_frame, text=voice.get_nnoise(self.one_channel_path), font=("Arial Bold", 15), bg='white',
            width=20, height=2)
        result_pr.pack(side=RIGHT)

        balance = Label(
            self.seven_frame, text=" Тональный баланс: ", font=("Arial Bold", 15), bg='white', width=20, height=2)
        balance.pack(side=LEFT)

        result_ba = Label(
            self.seven_frame, text=voice.get_tonebal(self.one_channel_path), font=("Arial Bold", 15), bg='white',
            width=20, height=2)
        result_ba.pack(side=RIGHT)

        pomeh = Label(
            self.eight_frame, text=" Заметность помех и искажений: ", font=("Arial Bold", 15), bg='white', width=26, height=2)
        pomeh.pack(side=LEFT)

        result_po = Label(
            self.eight_frame, text=voice.get_audiointer(self.one_channel_path), font=("Arial Bold", 15), bg='white',
            width=19, height=2)
        result_po.pack(side=RIGHT)

    def openFile(self):
        # file_name = fd.askopenfilename()
        # return(file_name)
        self.path = askopenfilename(filetypes=(('Voice', '*.wav'), ('All Files', '*.*')))



root = Tk()
TkSetup(root)
root.mainloop()


