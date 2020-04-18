          #'''Autor:杨昊'''
#    '''运用minim库实现了音频关于时域，频域和音量的可视化
#      同时实现了声音的记录以及播放与暂停'''
add_library('minim')

player=None
recorded=False
ps=False
bands = 128

def setup():
    global inn,recorder,recorded,out,player,ps
    global colors,fft,bands,barWidth
    size(1024, 400)
#    '''为取随机颜色而建的列表'''
    colors=[color(175,113,174),color(146,113,175),color(117,113,175),color(113,152,175)
            ,color(113,175,172),color(122,188,155),color(188,122,157)]
#    '''创建minim子类getLineIn的对象,设置立体声道和采样缓冲区的大小
#       创建FFT类的对象，设置和inn对象相同的缓冲区大小和相同的采样频率
#       创建minim子类creatRecorder的对象，指定inn为其输入源，存放在data目录下的
#       myrecording.wav文件下
#       创建minim子类getLineOut的对象，指定输出为立体声'''
    minim =  Minim(this)
    inn = minim.getLineIn(Minim.STEREO, 2048)
    fft =  FFT(inn.bufferSize(), inn.sampleRate())
    recorder = minim.createRecorder(inn, "data/myrecording.wav")
    out = minim.getLineOut( Minim.STEREO );
    #画频域图设置的每个矩形的宽度
    barWidth=width/float(bands)
    #设置字体格式与大小
    textFont(createFont("Arial", 20));

def draw():
    global inn,recorder,recorded,out,player,ps
    global colors,fft,barWidth,bands
    background(50); 
    text("r to start or stop record",5,15)
    text("s to listen or stop audio",5,30 )
#    '''设置局域变量c为随机变量：为后面上色做准备'''
    c=int(random(6))
    
    rectMode(CENTER)
#    '''画出左右声道的振幅大小，用来表示音量'''
    for i in range(inn.bufferSize()-1):        
        fill(206,184,167)
        noStroke()
        rect( 0, 100, inn.left.level()*width, 100 );
        rect( 0, 290, inn.right.level()*width, 100 )
     
#    '''用minim的get左右声道的方法，画出用波形表示的时域图((注意：用get方法获得的是时域数据)'''       
    strokeWeight(3)
    stroke(colors[c]);
    for i in range(inn.bufferSize()-1):
#       '''这里只采用了左声道的数据，右声道被注释了'''
        line(i, 100 + inn.left.get(i)*50, i+1, 100 + inn.left.get(i+1)*50);
        #line(i, 300 + inn.right.get(i)*50, i+1, 300 + inn.right.get(i+1)*50);
    
#    '''用FFT傅里叶变换获取频域图，利用for循环遍历每一个采样带的长度并作为矩形阵的高画出频域图'''
    fft.forward( inn.mix )
    fill(colors[c])
    for i in range(fft.specSize()):
        h=map(fft.getBand(i),0,10,0,20)
        rect(width/2+i*barWidth,280,barWidth/2,h)
        rect(width/2-i*barWidth,280,barWidth/2,h)
#    '''为字体上色，并设置条件来决定显示什么文字'''
    fill(255)
    if ( recorded==True ):    
        text("Now recording", 850, 15);
    elif ( recorded==False ):
        text("No recording", 850, 15);
    
    if ( ps==True ):    
        text("Now playing", 850, 30);
    elif ( ps==False ):
        text("No playing", 850, 30);

def keyReleased():
    global inn,recorder,recorded,out,player,ps
#    '''当按下的按钮是‘r’时，判断recorded的布尔值，决定是否开启录音'''
    if  key == 'r'  :
        if  (recorded==False) :
            recorder.beginRecord()
            recorded = True
    
        else :   
            recorder.endRecord();
            recorded =False
#    '''当按下的按钮是‘s’时，判断ps的布尔值并反转其值，若ps=False则播放录音'''
    if  key == 's':
        if ( player != None ):    
            player.unpatch( out );
            player.close();
        if ps==True:
            ps=False
            pass
        else:
            ps=True
            player = FilePlayer( recorder.save() );
            player.patch( out );
            player.play();
