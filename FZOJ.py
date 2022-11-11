from time import time,sleep
from flask import Flask,render_template,request,current_app
from random import shuffle
from subprocess import Popen,PIPE

from os import getcwd,path

class Judge:
    def __init__(self,text,lang):
        self.t=int(time())
        r=open('Judgege/MinGW64/bin/JudgeData/'+str(self.t)+'.'+lang,'w',encoding='utf-8')
        self.path=str(self.t)
        self.lang=lang
        r.write(text)
        r.close()
        
    def compile(self):
        if self.lang=='cpp':
            pass
        elif self.lang=='py':
            pass
        
    def run(self):
        if self.lang=='cpp':
            pass
        elif self.lang=='py':
            pass
        

rand_texts=['青青子衿，悠悠我心。',
'天行健，君子以自强不息。',
'志当存高远。',
'会当凌绝顶，一览众山小。',
'有志者事竟成。',
'锲而不舍，金石可镂。',
'精诚所加，金石为开。',
'路曼曼其修远兮，吾将上下而求索。',
'长风破浪会有时，直挂云帆济沧海。',
'生当作人杰，死亦为鬼雄。']

app=Flask(__name__)

@app.route('/')
def main():
    shuffle(rand_texts)
    return render_template('/main.html/',rand_text=rand_texts[0])

@app.route('/problems/<op>/')
def problems(op):
    if op=='create':
        return 'create'
    elif op=='list':
        return render_template('open_problem.html',method=['GET','POST'])
        
    else:
        return render_template(str(op)+'.html')

if __name__=='__main__':
    app.run('0.0.0.0')

