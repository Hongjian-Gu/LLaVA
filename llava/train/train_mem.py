import os
from llava.train.train import train

if __name__ == "__main__":
    os.environ["WANDB_DISABLED"] = "true"
    # train(attn_implementation="flash_attention_2")
    train(attn_implementation=None)
