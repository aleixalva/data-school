# data-school

A personal laboratory for learning **statistics, data analysis, and computational fluency** through real datasets.

The aim is not to learn a particular software stack for its own sake. The aim is to become able to take a dataset, ask sensible questions of it, investigate those questions efficiently, and leave a reproducible record of the reasoning and calculations.

## Principles

### 1. Statistics first

The central skill is statistical thinking:

* What is the question?
* What is the observational unit?
* What quantity should be measured?
* How should it be summarised?
* How much uncertainty is there?
* What assumptions are being made?
* What could make the conclusion misleading?

Programming is a means of answering these questions, not a substitute for answering them.

### 2. Use the simplest appropriate tool

Different tools are useful at different stages.

* **Bash and Unix tools** for files, text, streams, inspection and simple transformations.
* **Miller (`mlr`)** for straightforward tabular transformations and grouped aggregations.
* **Python** for numerical work, simulation and statistical analysis.
* **pandas** for general dataframe work.
* **GeoPandas** for spatial data and analysis.
* **NumPy / SciPy / statsmodels** for numerical and statistical computation.
* **DuckDB** when querying large tabular datasets makes more sense than loading everything into a dataframe.
* **Visualisation** when it helps investigate or communicate a specific question.

The goal is not to use all of these on every dataset. A good analysis should use the least complicated tool that adequately solves each part of the problem.

### 3. Explore before analysing

Initial exploration should be deliberately simple.

Typical questions include:

```text
What is in the file?
How many observations are there?
What are the variables?
What values occur?
Are there duplicates?
Are there missing values?
What are the ranges and distributions?
What is the observational unit?
```

The first pass often uses nothing more sophisticated than:

```bash
head
tail
wc
cut
sort
uniq
grep
awk
```

and, where appropriate, Miller.

### 4. Numbers before plots

Plots are useful, but they should not become a substitute for quantitative reasoning.

Before plotting, try to understand the data through:

* counts
* proportions
* quantiles
* means and medians
* standard deviations
* differences
* ratios
* correlations
* uncertainty
* simple statistical models

Then use visualisation to investigate specific questions, inspect structure, identify anomalies, or communicate results.

### 5. Keep the trace

Exploration is allowed to be messy.

The repository should preserve enough of the process to answer:

> What did I do, why did I do it, and what did I learn?

Interactive shell and IPython work can be preserved through command history and session transcripts. Successful explorations can subsequently be turned into clean `.sh`, `.py`, or `.md` files.

Git provides the longer-term history of the investigation.

The objective is not to document every failed command. It is to preserve the useful computational and intellectual trail.

## Exercises

Most exercises use real datasets, including datasets from [TidyTuesday](https://github.com/rfordatascience/tidytuesday).

Each exercise should ideally proceed through something like:

```text
dataset
   ↓
initial inspection
   ↓
questions
   ↓
simple calculations
   ↓
statistical reasoning
   ↓
targeted investigation
   ↓
interpretation
```

A typical exercise directory might contain:

```text
01.the_languages_of_africa/
├── README.md
├── data/
│   └── africa.csv
└── ...
```

The exercise README records questions, commands, results, observations, and conclusions.

## Long-term goal

The goal is to become fluent enough that the computational mechanics become secondary.

Given a dataset, the desired progression is:

```text
question
   ↓
statistical formulation
   ↓
choose the simplest appropriate computational tool
   ↓
calculate
   ↓
inspect
   ↓
challenge the result
   ↓
refine the question or method
   ↓
conclude
```

