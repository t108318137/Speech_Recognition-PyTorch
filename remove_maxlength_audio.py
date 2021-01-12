#刪除長度過長的訓練音檔
import librosa
import os
from tqdm import tqdm

path = r'D:\dataset\ntut-ml-2020-spring-taiwanese-e2e\train'
filelist = os.listdir(path)
maxduration = 20    #最大秒數
for filename in (filelist):
    file_path = os.path.join(path, filename)
    y, sr = librosa.load(file_path)
    duration = librosa.get_duration(y, sr)
    if duration > 20:
        maxduration = duration
        filepath = os.path.join(path, filename)
        os.remove(filepath)
        # print(maxduration)
        print(filename)
