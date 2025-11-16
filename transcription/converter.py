import os
import ffmpeg




def converter(dirpath, newDirectory, name):
    newName = name[:-4] + ".mp3"
    ffmpeg.input(dirpath + "/" + name).output(newDirectory + "/" + newName).run(overwrite_output=True)


def traverser():
    startingDirectory = "/home/yosis/Videos/trainingvids"
    newOne = "/home/yosis/Music/converted"
    for root, directories, filenames in os.walk(startingDirectory):
        for name in filenames:
            if name.endswith(".mp4"):
                converter(root, newOne, name)

if __name__ == "__main__":
    traverser()
