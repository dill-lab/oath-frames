# OATH Frames
## About
We introduce a novel framework to understand, synthesize and characterize large-scale public attitudes towards societal issues through a collaboration between social work experts and LLMs. Specifically, we introduce a framing typology: OATH-Frames, (Online Attitudes Towards Homelessness): nine hierarchical frames capturing public attitudes towards homelessness as expressed on Twitter. We provide three kinds of annotations for posts from Twitter: expert-only, LLM-assisted expert and predicted annotations from a multilabel classification model.
## Getting Started
* Install the recommended dependencies via [Anaconda](https://www.anaconda.com/download/)
  ```bash
    conda create -n oath python=3.9.12
    conda activate oath
    conda install -c conda-forge pip # make sure pip is installed
    python -m pip install -r requirements.txt # make sure the packages are installed in the specific conda environment
    python -m pip install -e .
  ```
## Data
Please refer to `TODO` for our released data
* Human Annotations
* Expert + GPT-4
* Analysis set (Model Predicted) 
* Train/Test/Eval Splits
  
*Note: Posts labeled with `0`, `[]`, or do not have any labels are those that have been filtered out as irrelevant to our task. Please exclude these during analysis* 
## Training and Evaluation
Please refer to `src/` for finetuning `Flan-T5-Large` on our data
(`TODO`: add link to script)
## Frame Analysis
Please refer to `analysis/` for all our code regarding analysis of our predicted frames
## Citation
```
```
