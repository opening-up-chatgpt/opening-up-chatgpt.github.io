# [![logo](docs/logos/openchatgpt-logo-favicon-red-on-transparent.png)](https:///opening-up-chatgpt.github.io/) Opening up ChatGPT — [view live table](https://opening-up-chatgpt.github.io/) 

Liesenfeld, Andreas, Alianda Lopez, and Mark Dingemanse. 2023. “Opening up ChatGPT: Tracking Openness, Transparency, and Accountability in Instruction-Tuned Text Generators.” In _Proceedings of the 5th Conference on Conversational User Interfaces (CUI ’23)_. Eindhoven. doi:10.1145/3571884.3604316.

> Large language models that exhibit instruction-following behaviour represent one of the biggest recent upheavals in conversational interfaces, a trend in large part fuelled by the release of OpenAI's ChatGPT, a proprietary large language model for text generation fine-tuned through reinforcement learning from human feedback (LLM+RLHF). We review the risks of relying on proprietary software and survey the first crop of open-source projects of comparable architecture and functionality. The main contribution of this paper is to show that openness is differentiated, and to offer scientific documentation of degrees of openness in this fast-moving field. We evaluate projects in terms of openness of code, training data, model weights, reinforcement learning data, licensing, scientific documentation, and access methods. We find that while there is a fast-growing list of projects billing themselves as 'open source', many inherit undocumented data of dubious legality, few share the all-important RLHF components (a key site where human annotation labour is involved), and careful scientific documentation is exceedingly rare. Degrees of openness are relevant to fairness and accountability at all points, from data collection and curation to model architecture, and from training and fine-tuning to release and deployment. 

## Contents

- [Overview](#overview)
- [How to contribute](#how-to-contribute)
- [List of Projects](#list-of-projects--)

## Overview
We classify projects for their degrees of openness across **a predefined set of criteria** in the areas of Availability, Documentation and Access. The criteria are described in detail [here](https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/tree/main/projects#criteria).

| Availability                                                          | Documentation                                                      | Access          |
|-----------------------------------------------------------------------|--------------------------------------------------------------------|-----------------|
| <ul><li>Open code</li><li>LLM data</li><li>LLM weights</li><li>RL data</li><li>RL weights</li><li>License</li></ul> | <ul><li>Code</li><li>Architecture</li><li>Preprint</li><li>Paper</li><li>Model card</li><li>Data sheet</li></ul> | <ul><li>Package</li><li>API</li></ul> |


## How to contribute
You can contribute in (at least) two ways: either by updating the awesomelist [below](#list-of-projects--), or by editing specific data points in the table (which means editing project-specific yaml files). Our goal is to have both elements roughly in sync, but awesomelists are by nature more free-form and text-driven, and we anticipate using them also for discovering new projects.

How to contribute to the awesomelist below:
1. Add entry to list of projects: 
2. Describe the project in terms of its openness, mentioning particular areas of focus (e.g., remarkably detailed documentation; murky licensing; relevant preprints). Use links liberally.
3. If there is a yaml file for the project already (see below), transclude it

How to contribute to the [live table](https://opening-up-chatgpt.github.io):
1. Fork the repo and edit an existing yaml file or create a new one based on the sample `yaml` file in [/projects](/projects)
2. File a pull request to have your changes reviewed and, hopefully, merged into main.

The live table is updated whenever there is a change to the files in the /projects/  folder.

## List of projects  [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Overview of available open text generators with links to evidence for the evaluation criteria. The target breed of models in focus here is characterized by the following two features: its architecture is at base a large language model instruction-tuned by reinforcement learning with human feedback (LLM + RLHF) and it aims for openness and transparency (along degrees we quantify).


### Alpaca
https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/blob/fd1abe2db7172d3d4fea3ba3c07c407832501b06/projects/alpaca.yaml#L3-L70

### Belle
https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/blob/a1af1c56e8faa82a9225942767eb42c573c7275c/projects/BELLE.yaml#L3-L70

### CerebrasGPT
https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/blob/e4fe656fe852ad5ba4aa9ebcaa0191c6a5c875d1/projects/Cerebras-GPT-111m.yaml#L3-L70

### ChatGPT
https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/blob/e4fe656fe852ad5ba4aa9ebcaa0191c6a5c875d1/projects/chatgpt.yaml#L3-L70

### ChatRWKV
https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/blob/61e3929ec9e14842258f76243884aaf490a282ea/projects/ChatRWKV.yaml#L3-L70

### Falcon
https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/blob/61e3929ec9e14842258f76243884aaf490a282ea/projects/Falcon-40B-instruct.yaml#L3-L70

### minChatGPT
https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/blob/fd1abe2db7172d3d4fea3ba3c07c407832501b06/projects/minChatGPT.yaml#L3-L70

### MPT-7b-instruct
https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/blob/910cd0bff3e8490d2f4ab1909126650ad5ee424d/projects/MPT-7b-instruct.yaml#L3-L70

### Open Assistant
https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/blob/910cd0bff3e8490d2f4ab1909126650ad5ee424d/projects/Open-Assistant.yaml#L3-L70

### OpenChatKit
https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/blob/910cd0bff3e8490d2f4ab1909126650ad5ee424d/projects/OpenChatKit.yaml#L3-L70

### Stable Vicuna
https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/blob/910cd0bff3e8490d2f4ab1909126650ad5ee424d/projects/stablevicuna.yaml#L3-L70

### Text generation webui
https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/blob/910cd0bff3e8490d2f4ab1909126650ad5ee424d/projects/text-generation-webui.yaml#L3-L70

### trlx
https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/blob/910cd0bff3e8490d2f4ab1909126650ad5ee424d/projects/trlx.yaml#L3-L70

### Vicuna13b-lmsys
https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/blob/910cd0bff3e8490d2f4ab1909126650ad5ee424d/projects/vicuna13B-lmsys.yaml#L3-L70

### XMTF
https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/blob/910cd0bff3e8490d2f4ab1909126650ad5ee424d/projects/xmtf.yaml#L3-L70

## Contribute

Contributions welcome! Read the [contribution guidelines](contributing.md) first.

List of contributors:

<a href="https://github.com/liesenf/awesome-open-chatgpt/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=liesenf/awesome-open-chatgpt" />
</a>

Made with [contrib.rocks](https://contrib.rocks).
