# OATH Frames

## Getting Started
* Install the recommended dependencies via [Anaconda](https://www.anaconda.com/download/)
  ```bash
    conda create -n oath python=3.8
    conda activate oath
    conda install -c conda-forge pip # make sure pip is installed
    python -m pip install -r requirements.txt # make sure the packages are installed in the specific conda environment
    python -m pip install -e .
  ```
## Data
Please refer to `tbd` for our released data
* Train/Test/Eval Splits
* 3M analysis set
* 4K Human Annotations
## Training and Evaluation
Please refer to `src/` for finetuning `Flan-T5-Large` on our data
## Frame Analysis
Please refer to `analysis/` for all our code regarding analysis of our predicted frames
## Citation
```
```
