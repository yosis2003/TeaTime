import torch
import time

device = "xpu"

# Large FP32 tensors (≈ 244 MB each)
a = torch.randn(9000, 9000, device=device)
b = torch.randn(9000, 9000, device=device)

print("Starting 3-minute GPU burn...")

start = time.time()
duration = 180  # seconds

i = 0
while time.time() - start < duration:
    # Heavy matrix multiply (main GPU load)
    c = a @ b
    
    # Fill compute units with nonlinear ops
    c = torch.sin(c) + torch.cos(c) + torch.relu(c)
    
    # Small reduction to keep data flowing
    c.sum().item()
    
    if i % 10 == 0:
        elapsed = time.time() - start
        print(f"Iteration {i}, time elapsed: {elapsed:.1f}s")
    i += 1

print("Done! Total iterations:", i)
