# Daily Resource Map

This file tells the mentor how to choose **exact places to learn and practice** each day. The mentor should give direct links for today's topic, not a giant reading list.

## Resource priority
1. Official documentation/tutorial for the tool being learned.
2. One beginner-friendly interactive course or guided lab.
3. The learner's own Colab/notebook exercise.
4. Optional video/article only when it adds something the first resources do not.

Before giving a link for a fast-changing AI API/framework, verify that it is current. Never invent a URL.

## Foundation resources

### Days 1–10 · Python
- Python official tutorial: https://docs.python.org/3/tutorial/
- Kaggle Learn Python: https://www.kaggle.com/learn/python
- Google Colab: https://colab.research.google.com/
Use Kaggle for short guided practice and Colab for the learner's own notebook.

### Days 11–18 · Data
- NumPy Learn: https://numpy.org/learn/
- pandas getting started: https://pandas.pydata.org/docs/getting_started/
- Matplotlib tutorials: https://matplotlib.org/stable/tutorials/
- Kaggle Learn: https://www.kaggle.com/learn

### Days 19–28 · Machine Learning
- scikit-learn getting started: https://scikit-learn.org/stable/getting_started.html
- Kaggle Intro to Machine Learning: https://www.kaggle.com/learn/intro-to-machine-learning
Use small datasets and require evaluation, not only training.

### Days 29–44 · Generative AI foundations, prompting & evaluation
Use current educational material from major model providers and high-quality open educational sources. Teach vendor-neutral concepts first. Verify current documentation before assigning provider-specific exercises.

### Days 45–53 · LLM APIs
Use the current official API documentation for whichever provider is being practiced. Teach secrets via environment variables, request/response structure, streaming, structured outputs, tools, retries, cost and evaluation. Compare at least two providers over this stage.

### Days 54–62 · Embeddings & RAG
Use current official model/provider embedding docs plus primary docs for the retrieval/vector technology selected that day. Teach retrieval quality and evaluation before adding orchestration frameworks.

### Days 63–72 · Agents & tools
Use current official docs for tool/function calling and the selected agent framework. Teach deterministic workflows before open-ended agents; include human approval, permissions and failure handling.

### Days 73–80 · Automation
Use official docs for REST/webhooks and the selected automation platform. Prefer a real workflow useful to the learner. Never put credentials in notebooks or Git.

### Days 81–90 · Capstone
Resources depend on the selected project. Prefer official docs and the learner's existing project requirements. Every capstone week includes testing, evaluation, privacy/security, documentation and a demo.

## After Day 90
At the start of each advanced module, the mentor must create/update a resource map from current official sources because AI tooling changes quickly.
