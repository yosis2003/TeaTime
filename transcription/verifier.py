import torch

# Check XPU availability and device info
print(f"PyTorch version: {torch.__version__}")
print(f"XPU available: {torch.xpu.is_available()}")
print(f"Device count: {torch.xpu.device_count()}")
print(f"Device name: {torch.xpu.get_device_name(0)}")

# Test actual GPU computation
x = torch.randn(1000, 1000, device='xpu')
y = torch.randn(1000, 1000, device='xpu')
result = torch.mm(x, y)  # Matrix multiplication on Intel GPU
print(f"✅ GPU computation successful on: {result.device}")