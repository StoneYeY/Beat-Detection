import sys
import jams
import os
import string

jam = jams.JAMS()
def func(fname):
    t = ''
    file = fname
    with open(file+".wav.jams","r"):
        contents = jams.load(file+".wav.jams")
        contents = contents.dumps(indent=2)
        for word in contents.split():
            word = word.strip(string.punctuation)
            # debug 1h for that
            if "annotation_type" in word and len(t)>0:
                break
            if word.split(".")[0].isdigit() and word.split(".")[1].isdigit() and len(word.split(".")[1])>3:
                interval = word + "\n"
                t += interval

        # contents.save("temp.jams")
        # reader = open("temp.jams","r")
        # for line in reader:
        #     line = line.rstrip()
        #     if "time" in line:
        #         times = reader.writelines([line])
        #         t += times
    #beat = jam.search(namespace='beat')[0]
    #jams.display.display_multi("time", fig_kw=None, meta=True, **kwargs)
    #beat=float(feats["time"])
    print(t)

    with open("../"+file.split('.wav')[0] + '.beat', 'w') as f:
        f.write(t)

rootDir = "./jams"
for root, dirs, files in os.walk(rootDir):
    os.chdir(rootDir)
    for file in files:
        if ".beat" in file:
            continue
        if ".DS_Store" in file:
            continue
        if "temp.jams" in file:
            continue
        fname = file.split('.wav')[0]
        print(fname)
        # if os.path != rootDir:
        #     os.chdir(rootDir)
        func(fname)


