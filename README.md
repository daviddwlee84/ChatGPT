# ChatGPT

Exploring potential of Large Language Model such as ChatGPT with prompting and end-to-end examples.

## Projects

| Subject                                                     | Purpose                                                     |
| ----------------------------------------------------------- | ----------------------------------------------------------- |
| [GPT3](GPT3/)                                               | Try simple prompts with Azure OpenAI API                    |
| [PaperSummarizer](PaperSummarizer/)                         | Try free ChatGPT (Selenium-based approach; not working now) |
| [ChatWithDocument](LangChain/ChatWithDocument/) (submodule) | Knowledge QA System (LangChain + ANN recall)                |
| [Training](Training/)                                       | Pre-train and Fine-tune the LLM                             |

## Todo

* [ ] Fine-tune GPT2
* [ ] Try RLHF on smaller model (shows before and after)

---

## ChatGPT

* [ChatGPT: Optimizing Language Models for Dialogue](https://openai.com/blog/chatgpt/)
    * [Try ChatGPT](https://chat.openai.com/auth/login)
    * [InstructGPT - Aligning Language Models to Follow Instructions](https://openai.com/blog/instruction-following/)
* [acheong08/ChatGPT: Reverse engineered ChatGPT API](https://github.com/acheong08/ChatGPT)

### News

### Summary / Collections

* [EwingYangs/awesome-open-gpt: Collection of Open Source Projects Related to GPT，GPT相关开源项目合集🚀、精选🔥🔥](https://github.com/EwingYangs/awesome-open-gpt)

### Third-Party API

* [mmabrouk/chatgpt-wrapper: API for interacting with ChatGPT using Python and from Shell.](https://github.com/mmabrouk/chatgpt-wrapper)
* [transitive-bullshit/chatgpt-api: Node.js client for the unofficial ChatGPT API. 🔥](https://github.com/transitive-bullshit/chatgpt-api)

#### Free

* [ztjhz/FreeChatGPT: An amazing open-source web app that allows you to play with OpenAI's ChatGPT API for free!](https://github.com/ztjhz/FreeChatGPT)
  * [Free ChatGPT](https://freechatgpt.chat/)
* [ayaka14732/ChatGPTAPIFree: A simple and open-source proxy API that allows you to access OpenAI's ChatGPT API for free!](https://github.com/ayaka14732/ChatGPTAPIFree)

### ChatGPT Prompt

* [f/awesome-chatgpt-prompts: This repo includes ChatGPT prompt curation to use ChatGPT better.](https://github.com/f/awesome-chatgpt-prompts)
* [PlexPt/awesome-chatgpt-prompts-zh: ChatGPT 中文调教指南。怎么让它听你的话。](https://github.com/PlexPt/awesome-chatgpt-prompts-zh)

### ChatGPT Applications

* [LinXueyuanStdio/chatgpt-review-rebuttal-extension: ChatGPT - Review & Rebuttal: A browser extension for generating reviews and rebuttals, powered by ChatGPT.](https://github.com/LinXueyuanStdio/chatgpt-review-rebuttal-extension)
* [hwchase17/notion-qa](https://github.com/hwchase17/notion-qa)
* [arc53/DocsGPT: GPT-powered chat for documentation search & assistance.](https://github.com/arc53/DocsGPT)

### Open Sourced LLM

* [facebookresearch/llama: Inference code for LLaMA models](https://github.com/facebookresearch/llama)
  * [ggerganov/llama.cpp: Port of Facebook's LLaMA model in C/C++](https://github.com/ggerganov/LLaMA.cpp)
  * [abetlen/llama-cpp-python: Python bindings for llama.cpp](https://github.com/abetlen/llama-cpp-python)
  * [Lightning-AI/lit-llama: Implementation of the LLaMA language model based on nanoGPT. Supports flash attention, Int8 and GPTQ 4bit quantization, LoRA and LLaMA-Adapter fine-tuning, pre-training. Apache 2.0-licensed.](https://github.com/Lightning-AI/lit-llama)
  * [alexrozanski/LlamaChat: Chat with your favourite LLaMA models in a native macOS app](https://github.com/alexrozanski/LlamaChat)
* [Stanford Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html)
  * [tatsu-lab/stanford_alpaca: Code and documentation to train Stanford's Alpaca models, and generate the data.](https://github.com/tatsu-lab/stanford_alpaca)
  * [antimatter15/alpaca.cpp: Locally run an Instruction-Tuned Chat-Style LLM](https://github.com/antimatter15/alpaca.cpp)
  * [ViperX7/Alpaca-Turbo: Web UI to run alpaca model locally](https://github.com/ViperX7/Alpaca-Turbo)
* [BlinkDL/ChatRWKV: ChatRWKV is like ChatGPT but powered by RWKV (100% RNN) language model, and open source.](https://github.com/BlinkDL/ChatRWKV)
* [nomic-ai/gpt4all: gpt4all: an ecosystem of open-source chatbots trained on a massive collections of clean assistant data including code, stories and dialogue](https://github.com/nomic-ai/gpt4all)
* Vicuna
  * [Vicuna: An Open-Source Chatbot Impressing GPT-4 with 90%* ChatGPT Quality | by the Team with members from UC Berkeley, CMU, Stanford, and UC San Diego](https://vicuna.lmsys.org/)
  * [Vicuna Installation Guide | TroubleChute Hub](https://hub.tcno.co/ai/text-ai/vicuna/)
  * [NEW POWERFUL Local ChatGPT 🤯 Mindblowing Unrestricted GPT-4 | Vicuna - YouTube](https://www.youtube.com/watch?v=ByV5w1ES38A)
  * [lm-sys/FastChat: The release repo for "Vicuna: An Open Chatbot Impressing GPT-4"](https://github.com/lm-sys/FastChat)

### ChatBot Framework

* LangChain
* [RasaHQ/rasa: 💬 Open source machine learning framework to automate text- and voice-based conversations: NLU, dialogue management, connect to Slack, Facebook, and more - Create chatbots and voice assistants](https://github.com/RasaHQ/rasa)

### Wrapper / Client / UI

* [dice2o/BingGPT: Desktop application of new Bing's AI-powered chat (Windows, macOS and Linux)](https://github.com/dice2o/BingGPT)

### Helper

* [domeccleston/sharegpt: Easily share permanent links to ChatGPT conversations with your friends](https://github.com/domeccleston/sharegpt)
* [zilliztech/GPTCache: GPTCache is a library for creating semantic cache to store responses from LLM queries.](https://github.com/zilliztech/GPTCache)

### Performance Efficiency

* Jittor
  * [Jittor(计图): 即时编译深度学习框架 — Jittor](https://cg.cs.tsinghua.edu.cn/jittor/)

## [GPT3](GPT3/)

* [karpathy/nanoGPT: The simplest, fastest repository for training/finetuning medium-sized GPTs.](https://github.com/karpathy/nanoGPT)

## Prompt Engineering

* [dair-ai/Prompt-Engineering-Guide: Guide and resources for prompt engineering](https://github.com/dair-ai/Prompt-Engineering-Guide)

## GPT4 / ChatGPT + Image

* [Instruction-Tuning-with-GPT-4/GPT-4-LLM](https://github.com/Instruction-Tuning-with-GPT-4/GPT-4-LLM)
  * [Instruction Tuning with GPT-4](https://instruction-tuning-with-gpt-4.github.io/)
  * [[2304.03277] Instruction Tuning with GPT-4](https://arxiv.org/abs/2304.03277)
* [Vision-CAIR/MiniGPT-4: MiniGPT-4: Enhancing Vision-language Understanding with Advanced Large Language Models](https://github.com/Vision-CAIR/MiniGPT-4)
* [haotian-liu/LLaVA: Large Language-and-Vision Assistant built towards multimodal GPT-4 level capabilities.](https://github.com/haotian-liu/LLaVA)
* [【生成式AI】GPT-4 來了! GPT-4 這次有什麼神奇的能力呢？ - YouTube](https://www.youtube.com/watch?v=kslijcrYizE)

## Todo

Try Projects

* [ ] [jerryjliu/gpt_index: GPT Index is a project consisting of a set of data structures designed to make it easier to use large external knowledge bases with LLMs.](https://github.com/jerryjliu/gpt_index)
* [X] [hwchase17/langchain: ⚡ Building applications with LLMs through composability ⚡](https://github.com/hwchase17/langchain)
  * [ ] [hwchase17/notion-qa](https://github.com/hwchase17/notion-qa)

Read Papers

* [ ] [InstructGPT - Aligning Language Models to Follow Instructions](https://openai.com/blog/instruction-following/)
* Prompts related
  * ...

Tutorials

* [ ] Hung-yi Lee Videos...
* [ ] LangChain Boldhead
