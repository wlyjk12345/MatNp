import wave
import matplotlib.pyplot as plt
import numpy as np
for _ in range(1,6):
    fil = "E:\w\w"+str(_)+".wav"
    f = wave.open(fil,'rb')
    params = f.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
    print('channel:', nchannels, 'sampwidth:', sampwidth, 'framerate:', framerate, 'numframes:', nframes)
    strData = f.readframes(nframes)#读取音频，字符串格式
    #waveData = np.frombuffer(strData, dtype='S1', offset=0)
    waveData = np.fromstring(strData, dtype=np.short)  # 将字符串转化为int
    waveData = waveData*1.0/(max(abs(waveData)))#wave幅值归一化
    # plot the wave
    waveData.shape = -1, 2
    #将其转置得到：
    waveData = waveData.T
    time = np.arange(0,nframes)*(1.0 / framerate)
    Max = max(waveData[0])


    plt.figure(_)
    plt.subplot(2,1,1)
    plt.plot(time, waveData[0])
    plt.title(fil+'         MAX = '+str(Max) ,verticalalignment="bottom",loc ="left")
    plt.subplot(2,1,2)
    plt.plot(time, waveData[1],'r')
    plt.xlabel("Time(s)")
    #plt.show()
    plt.savefig('w'+str(_))