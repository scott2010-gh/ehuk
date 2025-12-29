import tkinter as t
import tkinter.filedialog as tf
import tkinter.messagebox as tm
import interpreter as ip
from tkinter import simpledialog as s

global i
global saved
saved=False
version=1.0
main = t.Tk()
main.title('에흑 IDE')
main.geometry('800x500')

def clear_p():
    global p
    p.delete("1.0",tf.END)
    
def run(option):
    global i
    global p
    if option==1:
        runner = ip.에흑()
        runner.reset()
        runner.loadt(i.get("1.0",tf.END))
        import sys
        from io import StringIO
        a = sys.stdout
        b = StringIO()
        sys.stdout=b
        runner.idem=1
        runner.run()
        sys.stdout=a
        p.insert(tf.END,b.getvalue()+"\n")

    if option==2:
        main.lift()
        memsize = s.askstring("메모리 크기","메모리 사이즈를 입력하세요",parent=main)
        input_mode = s.askstring("입력모드","입력 모드를 설정하세요\n0 : 입력된 문자열이 아스키 코드로 변환되어 저장됨\n1 : 숫자 입력모드",parent=main)
        output_mode = s.askstring("출력모드","출력 모드를 설정하세요\n0 : 숫자 출력모드\n1 : 문자 출력모드",parent=main)
        runner = ip.에흑(int(memsize))
        runner.reset()
        runner.loadt(i.get("1.0",tf.END))
        import sys
        from io import StringIO
        a = sys.stdout
        b = StringIO()
        sys.stdout=b
        runner.idem=1
        runner.im=int(input_mode)
        runner.pm=int(output_mode)
        runner.run()
        sys.stdout=a
        p.insert(tf.END,b.getvalue()+"\n")
        
def ex(num):
    global i
    global saved
    if saved:
        if num==1:
            i.delete("1.0",tf.END)
            i.insert("1.0","에;흑{ 예제 : 피보나치 수열 출력하기 에;흑} \n에?흑 \n에흑 에흑 에흑 에>흑 \n에!흑 에_흑 에에흑 에!흑 에_흑 \n에>흑 에에흑 에!흑 에_흑 \n에<흑 에<흑 \n에@흑[ \n에>흑 에@흑[ 에흑 에>흑 에에흑 에>흑 에에흑 에<흑 에<흑 에@흑] \n에>흑 \n에@흑[ 에흑 에<흑 에에흑 에>흑 에@흑] \n에>흑 \n에@흑[ 에흑 에<흑 에에흑 에>흑 에@흑] \n에<흑 에<흑 에!흑 에_흑 에<흑 에흑 \n에@흑] \n에>흑")

        if num==2:
            i.delete("1.0",tf.END)
            i.insert("1.0","에;흑{ 예제 : HELLO WORLD 출력하기 에;흑} \n\n에에흑 에에흑 에에흑 에에흑 에에흑 에에흑 에에흑 에에흑 에에흑 에에흑 \n\n에@흑[ \n에>흑 에에흑 에에흑 에에흑 에에흑 에에흑 에에흑 에에흑 \n에>흑 에에흑 에에흑 에에흑 에에흑 에에흑 에에흑 에에흑 에에흑 에에흑 에에흑 \n에>흑 에에흑 에에흑 에에흑 \n에<흑 에<흑 에<흑 에흑 \n에@흑] \n\n에>흑 \n에에흑 에에흑 \n에!흑 \n에>흑 \n에에흑 \n에!흑 \n에에흑 에에흑 에에흑 에에흑 에에흑 에에흑 에에흑 \n에!흑 \n에!흑 \n에에흑 에에흑 에에흑 \n에!흑 \n에>흑 \n에에흑 에에흑 \n에!흑 \n에<흑 에<흑 \n에에흑 에에흑 에에흑 에에흑 에에흑 에에흑 에에흑 에에흑 에에흑 에에흑 에에흑 에에흑 에에흑 에에흑 에에흑 \n에!흑 \n에>흑 \n에!흑 \n에에흑 에에흑 에에흑 \n에!흑 \n에흑 에흑 에흑 에흑 에흑 에흑 \n에!흑 \n에흑 에흑 에흑 에흑 에흑 에흑 에흑 에흑 \n에!흑 에>흑 에에흑 에!흑")


        saved=False
    else:
        tm.showwarning("당신을 위한 친절한 경고","예제를 불러오면 기존 프로그램이 사라집니다.\n 계속하려면 다시한번 시도하세요")
        saved=True

def open_file():
    global i
    global p
    global saved
    if not saved:
        ask = tm.askyesno("경고","작성된 프로그램이 저장되지 않았습니다.\n계속할까요")
        if ask:
            i.delete("1.0",tf.END)
            path = tf.askopenfilename(defaultextension='.에흑',filetypes=[('에흑 파일','.에흑')],title="에흑 파일 불러오기 창 입니다")
            opener=open(path,'r',encoding='utf-8')
            i.insert("1.0",opener.read()+'\n')
            p.insert(tf.END,"에@흑 파일을 불러왔습니다 : "+path)
            opener.close()
        else:
            pass
    else:
        i.delete("1.0",tf.END)
        path = tf.askopenfilename(defaultextension='.에흑',filetypes=[('에흑 파일','.에흑')],title="에흑 파일 불러오기 창 입니다")
        opener=open(path,'r',encoding='utf-8')
        i.insert("1.0",opener.read()+'\n')
        opener.close()
        saved=False
def new_file():
    global i
    global saved
    if not saved:
        ask = tm.askyesno("경고","작성된 프로그램이 저장되지 않았습니다.\n정말 초기화할까요")
        if ask:
            i.delete("1.0",tf.END)
        else:
            pass
    else:
        i.delete("1.0",tf.END)
        saved=False
def save_file():
    global i
    global saved
    try:
        save = tf.asksaveasfile(mode='w',defaultextension='.에흑',filetypes=[('에흑 파일','.에흑')],title="에흑 파일 다른이름으로 저장하기 창 입니다")
        save.write(i.get("1.0",tf.END))
        saved=True
        save.close()
    except:
        tm.showwarning("오류","프로그램 저장에 실패하였습니다")

i=t.Text(main,width=111,height=26)
i.place(x=10,y=10)

p=t.Text(main,width=111,height=8)
p.place(x=10,y=385)
menu_bar=t.Menu(main)

text = t.Label(main,text="출력 :").place(x=7,y=360)
clear_prints = t.Button(main,text="clear",command=clear_p).place(x=750,y=355)

p.insert("1.0","에흑IDE version "+str(version)+"\n")

file=t.Menu(menu_bar,tearoff=0)
file.add_command(label = '새 파일', command=new_file)
file.add_command(label = '저장', command = save_file)
file.add_command(label = '열기', command = open_file)
menu_bar.add_cascade(label="파일",menu=file)

run_m=t.Menu(menu_bar,tearoff=0)
run_m.add_command(label = '실행', command=lambda x=2:run(x))
run_m.add_command(label = '기본 메모리(32768)로 실행', command=lambda x=1:run(x))
menu_bar.add_cascade(label="실행",menu=run_m)

examples = t.Menu(menu_bar,tearoff=0)
examples.add_command(label="hello world 출력",command=lambda x=2:ex(x))
examples.add_command(label="피보나치 수열 출력",command=lambda x=1:ex(x))
menu_bar.add_cascade(label="예제",menu=examples)
main.config(menu=menu_bar)
main.mainloop()
