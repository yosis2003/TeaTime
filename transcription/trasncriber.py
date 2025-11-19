import whisper
import os
import torch
# import intel_extension_for_pytorch as ipex



def warmup_xpu():
    dummy = torch.randn(1, 512, device="xpu")
    for _ in range(3):
        _ = dummy * dummy
    torch.xpu.synchronize()

def trancriber():
    directory = "/home/yosis/Music/converted"
    print(torch.__version__)
    # print(torch.xpu.is_available())
    


    # torch.xpu.set_device(0)
    device = torch.device("xpu")
    model = whisper.load_model("large", device = "xpu")

    for root, directories, filenames in os.walk(directory):
        for name in filenames:
            if name.endswith(".mp3"):
                print(name)
                result = model.transcribe(root + "/" + name)
                print(result)
                # with open (root + "/" + name + "_transcript.txt", "w") as f:
                #     f.write(result)


if __name__ == "__main__":
    warmup_xpu()
    trancriber()
