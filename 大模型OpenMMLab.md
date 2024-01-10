#llm 

# D1 开源体系
![image.png](https://img-1306232697.cos.ap-chongqing.myqcloud.com/obsidian_img/20240107192227.png)

![image.png](https://img-1306232697.cos.ap-chongqing.myqcloud.com/obsidian_img/20240107193458.png)

评测
![image.png](https://img-1306232697.cos.ap-chongqing.myqcloud.com/obsidian_img/20240107193656.png)
![image.png](https://img-1306232697.cos.ap-chongqing.myqcloud.com/obsidian_img/20240107193811.png)

![image.png](https://img-1306232697.cos.ap-chongqing.myqcloud.com/obsidian_img/20240107193930.png)

![image.png](https://img-1306232697.cos.ap-chongqing.myqcloud.com/obsidian_img/20240107194136.png)
![image.png](https://img-1306232697.cos.ap-chongqing.myqcloud.com/obsidian_img/20240107194503.png)

![image.png](https://img-1306232697.cos.ap-chongqing.myqcloud.com/obsidian_img/20240107194646.png)


# D2 趣味Demo

> 1.大模型及InternLM模型介

什么是大模型？
人工智能领域中参数数量巨大、拥有庞大计算能力和参数规模的模型

特点及应用
- 利用大量数据进行训练
- 拥有数十亿基至数于亿个参数
- 模型在各种任务中展现出惊人的性能

InternLM模型全链条开源
InternLM是一个开源的轻量级训练框架，旨在支持大模型训练而无需大量的依赖。基于InternLM
训练框架，上海人工智能实验室已经发布了两个开源的预训练模型：InternLM-7B和InternLM-20B

==Lagent==是一个轻量级、开源的基于大语言模型的==智能体（agent）框架==，用户可以快速地将一个大语言模型转变为多种类型的智能体。通过Lagent框架可以更好的发挥InternLM模型的全部性能

浦语·灵笔是基于书生·浦语大语言模型研发的视觉·语言大模型，有着出色的图文理解和创作能力，使用浦语·灵笔大模型可以轻松的创作一篇图文推文

> 2.InternLM-Chat-7B 智能对话Demo

模型介绍

通过单一的代码库，InternLM支持在拥有数干个GPU的大型集群上进行预训练，并在单个GPU上进
行微调，同时实现了卓越的性能优化。在1024个GPU上训练时，InternLM可以实现近90%的加速效率

InternLM-7B包含了一个拥有70亿参数的基础模型和一个为实际场景量身定制的对话模型。该模型
具有以下特点：
1. 利用数万亿的高质量token进行训练，建立了一个强大的知识库。
2. 支持8k token的上下文窗口长度，使得输入序列更长并增强了推理能力。

> 3.Lagent 智能体工具调用 Demo

Lagent是一个轻量级、开源的基于大语言模型的智能体（agent）框架，用户可以快速地将一个大语言模型转变为多种类型的智能体，并提供了一些典型工具为大语言模型赋能
架构如图所示：
![image.png](https://img-1306232697.cos.ap-chongqing.myqcloud.com/Obsidian-winCQ/202401092242224.png)

> 4.浦语·灵笔图文创作理解 Demo

浦语·灵笔是基于书生·浦语大语言模型研发的视觉-语言大模型，提供出色的图文理解和创作能力
具有多项优势：
1.为用户打造图文并貌的专属文章
2.设计了高效的训练策略，为模型注入海量的多模态概念和知识数据，赋予其强大的图文理解和
对话能力。

> 5.通用环境配置