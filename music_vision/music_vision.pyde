add_library('sound')
bands = 128
smoothingFactor = 0.2
sum=[0.0 for _ in range(bands)]
ballr=0.0
barWidth=0
scale = 2

def setup():
    global fft,ampl,sum,bands,barWidth,sample,colors,ballr
    size(1280, 500)
    background(255)
    colors=[color(114,247,255),color(252,140,140),color(252,233,169),color(147,248,251),color(182,144,240),color(195,245,250)]
    
    barWidth = width/float(bands)
    
    sample = SoundFile(this, "dongcidaci.mp3")
    sample.loop()
    
    ampl=Amplitude(this)
    ampl.input(sample)
    fft =  FFT(this, bands)
    fft.input(sample)
    

def draw():
    global fft,ampl,sum,soothingFactor,bands,barWidth,sample,colors,ballr
    background(255)
    #fill(255, 0, 150)
    noStroke()
    
    fft.analyze()
    
    ballr += (ampl.analyze()- ballr)
    r=map(ballr,0,1,0,250)
    fill(colors[2])
    ellipse(150,150,r*2,r*2)
    fill(colors[1])
    ellipse(450,350,r*1.5,r*1.5)
    fill(colors[5])
    ellipse(1050,150,r*1.5,r*1.5)
    fill(colors[0])
    ellipse(1050,150,r,r)
    
    c=int(random(5))
    fill(colors[c])
    for i in range(bands):
        #c=int(random(4))
        #fill(colors[c])
    
        sum[i] += (fft.spectrum[i] - sum[i]) * smoothingFactor
        rectMode(CENTER)
        rect(width/2+i*barWidth, height/2, barWidth/2, sum[i]*height*scale)
        rect(width/2-i*barWidth, height/2, barWidth/2, sum[i]*height*scale)
    
