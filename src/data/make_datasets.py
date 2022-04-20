import os
from dataset_functions import get_all, get_subways

if __name__ == "__main__":
    directory = f"{os.path.abspath(os.getcwd())}/data"
    print(directory)
    # Download datasets
    get_all(directory)
    get_subways(directory)