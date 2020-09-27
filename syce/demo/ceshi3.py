# 用Pyaudio库录制音频
#   out_file:输出音频文件名
#   rec_time:音频录制时间(秒)
import pyaudio
import wave
from aip import AipSpeech
import time
""" 你的 APPID AK SK """
APP_ID = '22752470'
API_KEY = 'jmXnMqbFRHqLtyHkms9p9jcG'
SECRET_KEY = 'gG58DUOlh8j1bb7cff3KxVkWuX30VE6v'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def audio_record(out_file, rec_time):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16 #16bit编码格式
    CHANNELS = 1 #单声道
    RATE = 16000 #16000采样频率
    p = pyaudio.PyAudio()
    # 创建音频流
    stream = p.open(format=FORMAT, # 音频流wav格式
                    channels=CHANNELS, # 单声道
                    rate=RATE, # 采样率16000
                    input=True,
                    frames_per_buffer=CHUNK)
    print("Start Recording...")
    frames = [] # 录制的音频流
    # 录制音频数据
    for i in range(0, int(RATE / CHUNK * rec_time)):
        data = stream.read(CHUNK)
        frames.append(data)
    # 录制完成
    stream.stop_stream()
    stream.close()
    p.terminate()
    print("Recording Done...")
    # 保存音频文件
    wf = wave.open(out_file, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    audio_record('C:\\Users\\zhao\\PycharmProjects\\aaa.wav',12)

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

#识别本地文件
s = client.asr(get_file_content('C:\\Users\\zhao\\PycharmProjects\\aaa.wav'), 'wav', 16000, {
        'dev_pid': 1537,})
a = ' '.join(s['result'])
#############################
#文字转语音
result  = client.synthesis('曹尼玛', 'zh', 1, {
    'vol': 5,
    'per': 4,
})
# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('audio.wav', 'wb') as f:
        f.write(result)
        print('ch')
######################################
#读取本地语音文件播放出来
CHUNK = 1024
FILENAME = 'audio.wav'

def play(filename = FILENAME):
    wf = wave.open(filename, 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while data != b'':
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()
play()
####################