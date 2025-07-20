import torch

def enable_gpu(model):
    """
    Enable GPU acceleration for the model.
    Args:
        model (torch.nn.Module): The reasoning model.
    Returns:
        torch.nn.Module: Model moved to GPU.
    """
    if torch.cuda.is_available():
        model = model.to('cuda')
        print("Model moved to GPU")
    else:
        print("GPU not available")
    return model