# [![logo](docs/logos/openchatgpt-logo-favicon-red-on-transparent.png)](https:///opening-up-chatgpt.github.io/) Opening up ChatGPT — [view live table](https://opening-up-chatgpt.github.io/) 

Liesenfeld, Andreas, Alianda Lopez, and Mark Dingemanse. 2023. “Opening up ChatGPT: Tracking Openness, Transparency, and Accountability in Instruction-Tuned Text Generators.” In Proceedings of CUI’23. Eindhoven. doi:10.1145/3571884.3604316.

> Large language models that exhibit instruction-following behaviour represent one of the biggest recent upheavals in conversational interfaces, a trend in large part fuelled by the release of OpenAI's ChatGPT, a proprietary large language model for text generation fine-tuned through reinforcement learning from human feedback (LLM+RLHF). We review the risks of relying on proprietary software and survey the first crop of open-source projects of comparable architecture and functionality. The main contribution of this paper is to show that openness is differentiated, and to offer scientific documentation of degrees of openness in this fast-moving field. We evaluate projects in terms of openness of code, training data, model weights, reinforcement learning data, licensing, scientific documentation, and access methods. We find that while there is a fast-growing list of projects billing themselves as 'open source', many inherit undocumented data of dubious legality, few share the all-important RLHF components (a key site where human annotation labour is involved), and careful scientific documentation is exceedingly rare. Degrees of openness are relevant to fairness and accountability at all points, from data collection and curation to model architecture, and from training and fine-tuning to release and deployment. 

## Contents

- [Overview](#overview)
- [How to contribute](#how-to-contribute)
- [List of Projects](##opening-up-chatgpt-a-curated-list-to-track-openness-transparency-and-accountability-in-instruction-following-text-generators-)

## Overview
We classify projects for their degrees of openness across **a predefined set of criteria** in the areas of Availability, Documentation and Access. The criteria are detailed [here](https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/tree/main/projects#criteria).

| Availability                                                          | Documentation                                                      | Access          |
|-----------------------------------------------------------------------|--------------------------------------------------------------------|-----------------|
| <ul><li>Open code</li><li>LLM data</li><li>LLM weights</li><li>RL data</li><li>RL weights</li><li>License</li></ul> | <ul><li>Code</li><li>Architecture</li><li>Preprint</li><li>Paper</li><li>Model card</li><li>Data sheet</li></ul> | <ul><li>Package</li><li>API</li></ul> |


## How to contribute
You can contribute in (at least) two ways: either by editing specific data points for particular projects in individual yaml files; or by updating the awesomelist below. Our goal is to have the awesomelist and the more detailed database of openness features by project roughly in sync, but awesomelists are by nature more free-form and text-driven.


1. Add entry to list of projects: 
```markdown
## [{owner}/{project-name}]{https://github.com/link/to/project}
```
2. Describe the project in terms of its openness, mentioning particular areas of focus (e.g., remarkably detailed documentation; murky licensing; relevant preprints. Use links liberally.


How to contribute to the live table:
1. Fork the repo and edit an existing yaml file or create a new one based on /projects/_sample.yaml
2. File a pull request to have your changes reviewed and, hopefully, merged into main.

The live table is updated whenever there is a change to the files in the /projects/  folder.

## Opening up ChatGPT: a curated list to track openness, transparency, and accountability in instruction-following text generators [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Overview of available open text generators with links to evidence of all above evaluation criteria.

### Alpaca
https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/blob/fd1abe2db7172d3d4fea3ba3c07c407832501b06/projects/alpaca.yaml#L3-L70

### Belle
https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/blob/a1af1c56e8faa82a9225942767eb42c573c7275c/projects/BELLE.yaml#L3-L70

### CerebrasGPT
https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/blob/e4fe656fe852ad5ba4aa9ebcaa0191c6a5c875d1/projects/Cerebras-GPT-111m.yaml#L3-L70

### chatGPT
https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/blob/e4fe656fe852ad5ba4aa9ebcaa0191c6a5c875d1/projects/chatgpt.yaml#L3-L70

### ChatRWKV
https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/blob/61e3929ec9e14842258f76243884aaf490a282ea/projects/ChatRWKV.yaml#L3-L70

### Falcon
https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/blob/61e3929ec9e14842258f76243884aaf490a282ea/projects/Falcon-40B-instruct.yaml#L3-L70

### minChatGPT
https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/blob/fd1abe2db7172d3d4fea3ba3c07c407832501b06/projects/minChatGPT.yaml#L3-L70

https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/blob/4c6730ddef6a5501d64380227f3beba6afa0391a/projects/MPT-7b-instruct.yaml#L3-L70

https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/blob/4c6730ddef6a5501d64380227f3beba6afa0391a/projects/Open-Assistant.yaml#L3-L70

https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/blob/4c6730ddef6a5501d64380227f3beba6afa0391a/projects/OpenChatKit.yaml#L3-L70

https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/blob/4c6730ddef6a5501d64380227f3beba6afa0391a/projects/stablevicuna.yaml#L3-L70

https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/blob/4c6730ddef6a5501d64380227f3beba6afa0391a/projects/text-generation-webui.yaml#L3-L70

https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/blob/4c6730ddef6a5501d64380227f3beba6afa0391a/projects/trlx.yaml#L3-L70

https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/blob/4c6730ddef6a5501d64380227f3beba6afa0391a/projects/vicuna13B-lmsys.yaml#L3-L70

https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/blob/4c6730ddef6a5501d64380227f3beba6afa0391a/projects/xmtf.yaml#L3-L70

## Contribute

Contributions welcome! Read the [contribution guidelines](contributing.md) first.

List of contributors:

<a href="https://github.com/liesenf/awesome-open-chatgpt/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=liesenf/awesome-open-chatgpt" />
</a>

Made with [contrib.rocks](https://contrib.rocks).
