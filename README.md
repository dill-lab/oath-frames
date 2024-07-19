# OATH Frames

This repository contains the code and data for our paper: 

[OATH-Frames: Characterizing Online Attitudes Towards Homelessness with LLM Assistants](https://arxiv.org/abs/2406.14883)

<h6> Jaspreet Ranjit, Brihi Joshi, Rebecca Dorn, Laura Petry, Olga Koumoundouros, Jayne Bottarini, Peichen Liu, Eric Rice, Swabha Swayamdipta</h6>

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
Please refer to [Hugging Face](https://huggingface.co/collections/dill-lab/oath-frames-66750459b31a31445bd1d67a) for our released data
* Expert Annotations: oath-frames-expert-annotations
* Expert + GPT-4: oath-frames-expert-plus-gpt-annotations
* Analysis set (Model Predicted): oath-frames-model-predicted-annotations
* Train/Test/Eval Splits: oath-frames-flan-datasets
* [NER](https://huggingface.co/cjber/reddit-ner-place_names) predictions: oath-frames-analysis-ner 
* PEH/Vulnerable population analysis (Section 4.3) in the paper: oath-frames-analysis-vulnerable-populations
  
*Note: Posts labeled with `0`, `[]`, or do not have any labels are those that have been filtered out as irrelevant to our task. Please exclude these during analysis* 
## Training and Evaluation
Please refer to `src/trainer_deepspeed.sh` for finetuning `Flan-T5-Large` on our data

## Frame Analysis
* Please refer to `analysis/` for all our code regarding analysis of our predicted frames
* `analysis/analysis_data/` contains accompanying preprocessed files frame analysis, note that extended NER predictions and accompanying file for analysis 4.3 in the paper is hosted on huggingface

## Citation
```
@article{ranjit2024oath,
  title={OATH-Frames: Characterizing Online Attitudes Towards Homelessness with LLM Assistants},
  author={Ranjit, Jaspreet and Joshi, Brihi and Dorn, Rebecca and Petry, Laura and Koumoundouros, Olga and Bottarini, Jayne and Liu, Peichen and Rice, Eric and Swayamdipta, Swabha},
  journal={arXiv preprint arXiv:2406.14883},
  year={2024}
}
```
