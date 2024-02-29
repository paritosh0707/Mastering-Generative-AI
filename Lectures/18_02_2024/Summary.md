# Transformer In Depth

Transformers bought revolution in the filed of AI
## Impacts of Transformers
1. Revolution in the field of NLP
2. Introduction of **Transfer Learning** and **finetuning**
3. Multimodels Capability
4. Arise of new field of Generative AI


Encoder and Decoder Architecture with Attention layer solves the problem of asynchronous challenge in language translation.

Here we also dicuss about the different techniques of converting Words -> Vectors (**Word Embeddings**):
* Broadly, we can classified word embeddings into the following two categories:

        1.Frequency-based or Statistical based Word Embedding - OHE, BOW, N-grams, Tf-Idf
        2.Prediction based Word Embedding - Word2Vec (CBOW and Skip Grams)
    References: https://www.turing.com/kb/guide-on-word-embeddings-in-nlp



## Limitations before the invention of concept of self attention

Before the advent of self-attention mechanisms in transformer architectures, traditional word embeddings, such as word2vec or GloVe, faced several limitations in capturing complex semantic relationships and contextual information in language:

1. **Fixed Representation**: Word embeddings typically provide fixed-size vector representations for words, regardless of their context within a sentence. This means that the same word will have the same embedding regardless of its meaning or usage in different contexts, leading to limitations in capturing nuances and polysemy.

2. **Context Blindness**: Traditional word embeddings treat each word as independent of its context, resulting in a lack of contextual information. This can be problematic for tasks where word meaning heavily depends on the surrounding words or context, such as disambiguation or sentiment analysis.

3. **Sparse Context**: Traditional word embeddings usually consider only a limited context window around each word during training, which may not be sufficient to capture long-range dependencies or complex syntactic and semantic relationships in language.

4. **Out-of-Vocabulary Words**: Word embeddings often struggle with out-of-vocabulary (OOV) words, i.e., words not seen during training. This limits the generalizability of the embeddings and may result in poor performance on tasks involving rare or unseen words.

5. **Pretrained Embeddings**: While pretrained word embeddings alleviate some of the limitations by capturing general semantic information from large text corpora, they may not be optimal for specific domains or tasks, requiring fine-tuning or domain-specific embeddings.

The introduction of self-attention mechanisms in transformer architectures addressed many of these limitations by enabling models to dynamically capture contextual information and dependencies between words across the entire sequence. Self-attention allows transformers to attend to different parts of the input sequence with varying degrees of importance, effectively capturing long-range dependencies and contextual information, thereby improving the quality of word representations and the performance of NLP tasks.