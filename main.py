import torch

def verify_pytorch():
    print("=========================================")
    print("PyTorch Installation Verification")
    print("=========================================")
    print(f"PyTorch Version: {torch.__version__}")
    
    # Check device
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using Device: {device.upper()}")
    
    # Create tensors and perform a simple operation
    print("\nCreating simple tensors...")
    x = torch.rand(3, 3)
    y = torch.rand(3, 3)
    print(f"Tensor X:\n{x}")
    print(f"Tensor Y:\n{y}")
    
    print("\nPerforming matrix multiplication (X @ Y)...")
    z = torch.matmul(x, y)
    print(f"Result Tensor Z:\n{z}")
    print("=========================================")

if __name__ == "__main__":
    verify_pytorch()
 hello world