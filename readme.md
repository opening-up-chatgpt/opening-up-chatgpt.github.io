# [![](/openchatgpt-logo-favicon-red-on-transparent.png)](https://osai-index.eu/) Opening up ChatGPT

**Please note:** The original "Opening up ChatGPT" project (active 2023-2024) is superseded by the [European Open Source AI Index](https://osai-index.eu). We preserve this repository for historical purposes, but it is no longer updated. For the latest on openness and generative AI, check out the [osai-index.eu](https://osai-index.eu).

## Original publication

Liesenfeld, Andreas, Alianda Lopez, and Mark Dingemanse. 2023. “Opening up ChatGPT: Tracking Openness, Transparency, and Accountability in Instruction-Tuned Text Generators.” In _Proceedings of the 5th International Conference on Conversational User Interfaces_. Eindhoven. doi:[10.1145/3571884.3604316](https://doi.org/10.1145/3571884.3604316). ([PDF](https://pure.mpg.de/pubman/item/item_3526897_1/component/file_3526898/Liesenfeld%20et%20al_2023_Opening%20up%20ChatGPT.pdf))

> Large language models that exhibit instruction-following behaviour represent one of the biggest recent upheavals in conversational interfaces, a trend in large part fuelled by the release of OpenAI's ChatGPT, a proprietary large language model for text generation fine-tuned through reinforcement learning from human feedback (LLM+RLHF). We review the risks of relying on proprietary software and survey the first crop of open-source projects of comparable architecture and functionality. The main contribution of this paper is to show that openness is differentiated, and to offer scientific documentation of degrees of openness in this fast-moving field. We evaluate projects in terms of openness of code, training data, model weights, reinforcement learning data, licensing, scientific documentation, and access methods. We find that while there is a fast-growing list of projects billing themselves as 'open source', many inherit undocumented data of dubious legality, few share the all-important RLHF components (a key site where human labour is involved), and careful scientific documentation is exceedingly rare. Degrees of openness are relevant to fairness and accountability at all points, from data collection and curation to model architecture, and from training and fine-tuning to release and deployment. 

## Overview
We classify projects for their degrees of openness across **a predefined set of criteria** in the areas of Availability, Documentation and Access. The criteria are described in detail [here](https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/tree/main/projects#criteria).

| Availability                                                          | Documentation                                                      | Access          |
|-----------------------------------------------------------------------|--------------------------------------------------------------------|-----------------|
| <ul><li>Open code</li><li>LLM data</li><li>LLM weights</li><li>RL data</li><li>RL weights</li><li>License</li></ul> | <ul><li>Code</li><li>Architecture</li><li>Preprint</li><li>Paper</li><li>Model card</li><li>Data sheet</li></ul> | <ul><li>Package</li><li>API</li></ul> |

If you find any of this useful, please cite our work:

```bibtex

@inproceedings{liesenfeld_dingemanse_2024,
	author = {Liesenfeld, Andreas and Dingemanse, Mark},
	title = {Rethinking open source generative AI: open washing and the EU AI Act},
	year = {2024},
	isbn = {9798400704505},
	publisher = {Association for Computing Machinery},
	address = {New York, NY, USA},
	url = {https://doi.org/10.1145/3630106.3659005},
	doi = {10.1145/3630106.3659005},
	pages = {1774–1787},
	numpages = {14},
	keywords = {Technology assessment, large language models, text generators, text-to-image generators},
	location = {, Rio de Janeiro, Brazil, },
	series = {FAccT '24}
}

@inproceedings{liesenfeld_opening_2023,
	address = {Eindhoven},
	title = {Opening up {ChatGPT}: tracking openness, transparency, and accountability in instruction-tuned text generators},
	url = {https://opening-up-chatgpt.github.io},
	doi = {10.1145/3571884.3604316},
	booktitle = {Proceedings of the 5th {International} {Conference} on {Conversational} {User} {Interfaces}},
	publisher = {Association for Computing Machinery},
	author = {Liesenfeld, Andreas and Lopez, Alianda and Dingemanse, Mark},
	year = {2023},
	pages = {1--6},
}

```

## Related resources

We try to be fairly systematic in our coverage of LLM+RLHF models, documenting degrees of openness for >10 features. There are many other resources that provide more free-form listings of relevant stuff or that offer ways to interact with (open) LLMs:

* [Awesome Totally Open ChatGPT](https://github.com/nichtdax/awesome-totally-open-chatgpt/) — a free-form awesomelist of ChatGPT alternatives.
* [gpt4free: other models](https://github.com/xtekky/gpt4free#other-models) — another list of alternatives to GTP3.5/GPT4
* [Jetstream's Awesome free and open sources alternatives to ChatGPT](https://github.com/JetstreamAIVisionary/Awesome-free-and-open-source-alternatives-to-ChatGPT-and-pilot-training-courseware.-) — a free-form listing "dedicated to showcasing a collection of awesome free and open-source alternatives to ChatGPT"
* [LLMZoo](https://github.com/FreedomIntelligence/LLMZoo) — Motivation: "Break "AI supremacy" and democratize ChatGPT"
* [text generation webui](https://github.com/oobabooga/text-generation-webui) — provides gradio web app framework for interacting with a range of open LLMs 

Here are some background readings on why openness matters, why closed models make bad baselines, and why some of us call for more counterfoil research in times of hype:

* [The gradient of generative AI release](https://dl.acm.org/doi/10.1145/3593013.3593981) — FACCT '23 paper by Irene Solaiman on degrees of openness in generative AI
* [Closed AI models make bad baselines](https://hackingsemantics.xyz/2023/closed-baselines/), by Anna Rogers. Proposes a simple principle: "That which is not open and reasonably reproducible cannot be considered a requisite baseline."
* [Why ChatGPT is bad for open psycholinguistics](https://cxjacobs.notion.site/Why-ChatGPT-is-bad-for-open-psycholinguistics-6accb832bb4d414aa2fa8e648af95d7f) — by Cassandra Jacobs. Quote: "The downsides of ChatGPT are specific to it—not intrinsic to language modeling as a whole. Using ChatGPT [in] one’s work undermines open science, reproducibility & lacks the flexibility of previous systems that could be manipulated & changed to suit one’s scientific needs."
* [Stop feeding the hype and start resisting](https://irisvanrooijcogsci.com/2023/01/14/stop-feeding-the-hype-and-start-resisting/), by Iris van Rooij. Quote: "It’s almost as if academics are eager to do the PR work for OpenAI (the company that created ChatGPT; as well as its predecessor GPT-3 and its anticipated successor GPT-4). Why?"
* [AI is a lot of work](https://www.theverge.com/features/23764584/ai-artificial-intelligence-data-notation-labor-scale-surge-remotasks-openai-chatbots) — by Josh Dzieza for _The Verge_. Quote: "ChatGPT seems so human because it was trained by an AI that was mimicking humans who were rating an AI that was mimicking humans who were pretending to be a better version of an AI that was trained on human writing."  

## Contributors (historical)

List of contributors:

<a href="https://github.com/liesenf/awesome-open-chatgpt/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=liesenf/awesome-open-chatgpt" />
</a>

Made with [contrib.rocks](https://contrib.rocks).
