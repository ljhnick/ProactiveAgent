import torch
from PIL import Image
from lavis.models import load_model_and_preprocess
import time


def main():
    device = torch.device("cuda") if torch.cuda.is_available() else "cpu"
    raw_image = Image.open("/home/nick/Research/ProactiveAgent/data/test/IMG_3635.jpg").convert("RGB")

    model, vis_processors, _ = load_model_and_preprocess(
        name='blip2_vicuna_instruct',
        model_type='vicuna7b',
        is_eval=True,
        device=device,
    )

    image = vis_processors["eval"](raw_image).unsqueeze(0).to(device)
    start_time = time.time()
    output = model.generate({"image": image, "prompt": "Write a short description for the image."})
    print(output)
    print(time.time() - start_time)

    start_time = time.time()
    output = model.generate({"image": image, "prompt": "Write a detailed description for the image."})
    print(output)
    print(time.time() - start_time)
    

    print(1)
    


if __name__ == '__main__':
    main()