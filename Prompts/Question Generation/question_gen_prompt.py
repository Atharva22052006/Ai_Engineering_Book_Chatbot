QUESTION_GEN_PROMPT = """You generate quiz-style questions from a page of a technical book, for evaluating a \
retrieval system. For each question, also provide the exact supporting phrase from the page that answers it — \
this phrase must be copied verbatim (or very close to verbatim) from the page text, so it can be used to \
locate the source passage later.

Generate exactly 5 questions from the page below. Return ONLY a JSON array, no other text, in this exact format:

[
  {{"question": "...", "answer_fact": "..."}},
  {{"question": "...", "answer_fact": "..."}},
  {{"question": "...", "answer_fact": "..."}},
  {{"question": "...", "answer_fact": "..."}},
  {{"question": "...", "answer_fact": "..."}}
]

Rules:
- Questions should be answerable using only this page's content
- "answer_fact" must be a short phrase (10-25 words) copied directly from the page text, not paraphrased
- Skip pages with no real content (e.g. blank pages, pure table of contents) by returning an empty array []
- Do not include any text outside the JSON array

Here is the page:
<page>
{page_text}
</page>"""