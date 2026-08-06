# prompts.py

CONTEXTUAL_RETRIEVAL_PROMPT = """You generate short retrieval contexts for chunks of text pulled from a larger document. \
Given a section of the document and a specific chunk from within it, write a 1-2 sentence context that situates \
the chunk — mentioning the document/chapter/topic it belongs to and what the chunk itself covers. This context \
will be prepended to the chunk to improve search retrieval, so it should be dense with identifying information, \
not generic filler.

Here are some examples of good outputs:

Example 1:
<section>
...text from Chapter 3: Evaluation Methodology, discussing different ways to evaluate language models including \
perplexity, benchmark suites, and human evaluation...
</section>
<chunk>
Perplexity measures how well a probability model predicts a sample. Lower perplexity indicates the model is less \
"surprised" by the text, suggesting better predictive performance.
</chunk>
Context: This chunk is from Chapter 3 (Evaluation Methodology), specifically the section on perplexity as a metric for evaluating language model quality.

Example 2:
<section>
...table of contents listing chapter sections and their page numbers, covering topics like memory bottlenecks, \
backpropagation, and numerical representations...
</section>
<chunk>
Memory Bottlenecks 319
Backpropagation and Trainable Parameters 320
Memory Math 322
Numerical Representations 325
</chunk>
Context: This chunk is from the book's table of contents, listing subsection titles and page numbers related to memory and training mechanics in a chapter on model training.

Example 3:
<section>
...text from Chapter 1: Introduction, tracing the history of language models from the 1950s through to modern \
foundation models like GPT and the rise of AI engineering as a discipline...
</section>
<chunk>
While applications like ChatGPT and GitHub's Copilot may seem to have come out of nowhere, they are the culmination \
of decades of technology advancements, with the first language models emerging in the 1950s.
</chunk>
Context: This chunk is from Chapter 1 (Introduction), part of a historical overview explaining that modern AI applications are the result of decades of language model development rather than a sudden breakthrough.

Now generate the context for this chunk:

<section>
{section_text}
</section>
<chunk>
{chunk_text}
</chunk>
Context:"""