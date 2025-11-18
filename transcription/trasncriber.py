import whisper
import os
import torch
# import intel_extension_for_pytorch as ipex


def trancriber():
    directory = "/home/yosis/Music/converted"
    print(torch.__version__)
    print(torch.xpu.is_available())
    



    device = torch.device("xpu")
    model = whisper.load_model("turbo")

    for root, directories, filenames in os.walk(directory):
        for name in filenames:
            if name.endswith(".mp3"):
                result = model.transcribe(root + "/" + name)
                with open (root + "/" + name + "_transcript.txt", "w") as f:
                    f.write(result)


if __name__ == "__main__":
    trancriber()
