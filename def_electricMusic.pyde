add_library('sound')

attackTime=0.02
sustainTime=0.04
sustainLevel=0.5
releaseTime=0.3

bands = 128
barWidth=0

def setup():
    global attackTime,sustainTime,sustainLevel,releaseTime
    global sine,saw,sqr,triOsc,env
    global inn,fft,bands,barWidth
    size(640,360)
    background(255)
    sine=SinOsc(this)
    saw=SawOsc(this)
    sqr=SqrOsc(this)
    triOsc=TriOsc(this)
    env=Env(this)
    
    barWidth = width/float(bands)
    inn=AudioIn(this,0)
    fft =  FFT(this, bands)
    fft.input(inn)
def draw():
    global inn,fft,bands,barWidth
    background(255)
    fft.analyze()
    fill(0,155)
    for i in range(bands):
        rectMode(CENTER)
        rect(width/2+i*barWidth, height/2, barWidth/2, fft.spectrum[i]*height)
        rect(width/2-i*barWidth, height/2, barWidth/2, fft.spectrum[i]*height)


def keyReleased():
    global attackTime,sustainTime,sustainLevel,releaseTime
    global sine,saw,sqr,triOsc,env
    
    if key=='q':   
        triOsc.set(200,1,0,0)
        triOsc.play()
        env.play(triOsc,attackTime,sustainTime,sustainLevel,releaseTime)
    elif key=='w': 
        triOsc.set(400,1,0,0)
        triOsc.play()
        env.play(triOsc,attackTime,sustainTime,sustainLevel,releaseTime)
    elif key=='e':  
        sine.set(500,1,0,0)
        sine.play()
        env.play(sine,attackTime,sustainTime,sustainLevel,releaseTime)
    elif key=='r':  
        sine.set(800,1,0,0)
        sine.play()
        env.play(sine,attackTime,sustainTime,sustainLevel,releaseTime)
    elif key=='t':  
        saw.set(1000,1,0,0)
        saw.play()
        env.play(saw,attackTime,sustainTime,sustainLevel,releaseTime)
    elif key=='y':  
        saw.set(2000,1,0,0)
        saw.play()
        env.play(saw,attackTime,sustainTime,sustainLevel,releaseTime)
    elif key=='u':  
        sqr.set(4000,1,0,0)
        sqr.play()
        env.play(sqr,attackTime,sustainTime,sustainLevel,releaseTime)
    elif key=='i':  
        sqr.set(5000,1,0,0)
        sqr.play()
        env.play(sqr,attackTime,sustainTime,sustainLevel,releaseTime)    
