# COMP0078 — Coursework 1 (2026/27)

**Authors**
- Juan Pablo Baron Sandoval — juan.sandoval.26@ucl.ac.uk — [juanpablob11](https://github.com/juanpablob11)
- Juan Antonio Rodriguez Rubio — juan.rubio.26@ucl.ac.uk — [jrodriguezru](https://github.com/jrodriguezru)

## Notebooks

| File | Questions | Topic |
| --- | --- | --- |
| [01_part1_q01_q03_basis_regression.ipynb](notebooks/01_part1_q01_q03_basis_regression.ipynb) | 1–3 | Polynomial and sinusoidal regression |
| [02_part1_q04_q05_housing_krr.ipynb](notebooks/02_part1_q04_q05_housing_krr.ipynb) | 4–5 | Housing data, linear regression and kernel ridge regression |
| [03_part2_q06_q08_knn.ipynb](notebooks/03_part2_q06_q08_knn.ipynb) | 6–8 | k-NN and experimental Protocols A/B |

The notebooks are empty templates with question/subpart headings. Each should run independently from a fresh kernel once implemented. Questions 9–11 belong in the [Overleaf report](https://www.overleaf.com/project/6adcf4bd4fea8d07d42c0cec); Question 11 requires no implementation.

## Setup

Use Python 3.11 or 3.12:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m jupyter lab
```

On Windows, activate with `.venv\Scripts\activate`. Dependencies are a starter list; record validated versions and seeds with the final results. Use **Restart Kernel and Run All** to check each completed notebook.

## Data and results

For Questions 4–5, obtain the course-supplied [filtered Boston housing CSV](http://www.cs.ucl.ac.uk/staff/M.Herbster/boston-filter) and save it as `data/boston-filter.csv`. This source is from the beta brief; availability is not yet verified. Use the specified 12-attribute version, not the original unfiltered dataset. Save report plots in `results/figures/` and numerical summaries in `results/tables/`. Raw data and generated outputs are ignored by default.

## Coursework and access

Implement regression, bases and kernels directly with matrix algebra, and implement k-NN directly. The beta requires PDF answers and a separate ZIP of well-commented source code on Moodle; a GitHub link does not replace them. Do not print program source code in the PDF.

The repository is public; only the owner and authorised collaborators can push. An invitation has been sent to `jrodriguezru` and is awaiting acceptance.

Structure follows `CW1_2627-v-beta.pdf`. Check the [module's updated instructions](https://moodle.ucl.ac.uk/mod/forum/discuss.php?d=1328571) and applicable anonymous-marking/candidate-number rules before submission. No repository naming convention is specified in the beta.
