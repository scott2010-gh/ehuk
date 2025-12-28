class 에흑:
    def __init__(self,mem=32768):
        self.ms = mem
        self.memory=[0]*mem
        self.p = 0
        self.pc = 0
        self.pm=1
        self.im=1
        self.code=[]
        self.jumpto = {}
    
    def load(self,path):
        a=open(path,mode='r',encoding='utf-8')
        self.code=a.read().replace('\n','').split(" ")
        a.close()

    def ip(self):
        if self.p>=len(self.memory)-1:
            print("에#흑") #오버플로우
        else:
            self.p+=1

    def dp(self):
        if self.p<=0:
            print("에##흑") #언더플로우
        else:
            self.p-=1


    def iv(self):
        self.memory[self.p]+=1

    def dv(self):
        self.memory[self.p]-=1

    def ws(self):
        print(' ',end='')

    def pv(self):
        if self.pm==1:
            print( chr(self.memory[self.p]),end='')
        elif self.pm==0:
            print(self.memory[self.p],end='')

    def sv(self):
        if self.im==1:
            try:
                self.memory[self.p] = int(input())
            except:
                print("에#####흑") #입력 오류
        elif self.im==0:
            try:
                self.memory[self.p] = ord(str(input()))
            except:
                print("에######흑")

    def memory(self):
        print(self.memory)

    def reset(self):
        self.memory=[0]*self.ms
        self.jumpto={}
        self.p=0
        self.pc=0

    def preprocessing(self):
        stack = []
        for i in range(len(self.code)):
            if self.code[i]in ["에@흑[","에;흑{"]:
                stack.append(i)
            elif self.code[i]in ["에@흑]","에;흑}"]:
                if len(stack)==0:
                    print("에###흑") #괄호 문법 오류
                else:
                    self.jumpto[i]=stack.pop() #초기위치
                    self.jumpto[self.jumpto[i]]=i #끝나는 위치
        if len(stack)>0:
            print("에####흑") #스택에 괄호가 아직 남음

    def loop_comment(self,c):
        if c=="에@흑[" and self.memory[self.p]==0:
            self.pc=self.jumpto[self.pc]
        elif c=="에@흑]" and self.memory[self.p]!=0:
            self.pc=self.jumpto[self.pc]
        elif c=="에;흑{" :
            self.pc=self.jumpto[self.pc]
            
        
    def code(self):
        return self.code

    def run(self):
        self.preprocessing()
        while self.pc<len(self.code):
            cmd = self.code[self.pc]

            if cmd=="에>흑": self.ip()
            elif cmd=="에<흑": self.dp()
            elif cmd=="에에흑": self.iv()
            elif cmd=="에흑": self.dv()
            elif cmd=="에!흑": self.pv()
            elif cmd=="에?흑": self.sv()
            elif cmd=="에_흑": self.ws()
            elif cmd in ["에@흑[","에@흑]","에;흑{"]: self.loop_comment(cmd)

            self.pc+=1
    
    def hw(self,text,num):
        print(text*num)
