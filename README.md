# Beat-Detection
MGTV 音视频节拍检测比赛试用代码

Step1 Dataprocess: 处理训练集、验证集数据，获取Mel Spectrogram

Step2 Train: 训练模型BeatTrackingNet

Step3 Beat_tracker: 输入Mel Spectrogram，得到beat times数据并保存

Step4 Run: 计算beat和step3一样，最后加上downbeat记录和结果提交

注：
1.模型在model.py, 从BeatTrackingNet的前向传播理解调用关系
2.data路径在config.yaml里修改
3.提交入口是opt里内层文件夹的run.sh



