# COMP0078 — Coursework 1 (2026/27)

**Status: empty notebook templates. No coursework solutions or experimental results have been implemented.**

Collaboration repository for UCL Supervised Learning Coursework 1.

| Group member | UCL email | Current allocation |
| --- | --- | --- |
| Juan Pablo Baron Sandoval | juan.sandoval.26@ucl.ac.uk | Parts II and III, Questions 6–11 |
| Juan Antonio Rodriguez Rubio | juan.rubio.26@ucl.ac.uk | Allocation to be confirmed |

## Submission requirements

The supplied **CW1_2627-v-beta.pdf** requires **PDF answers and a separate ZIP of well-commented source code, submitted on Moodle**. A GitHub link does not replace these files. The beta specifies no repository name, notebook count, or GitHub submission requirement.

The [23 October Moodle announcement](https://moodle.ucl.ac.uk/mod/forum/discuss.php?d=1328571) plans version 1 for Monday, 26 October 2026. Recheck the final brief and submission activity. The beta states 18 November 2026 as the due date; the final submission time has not been verified.

Implement regression (including basis functions and kernels) directly with matrix algebra, and implement k-NN directly. Do not use ready-made model-fitting or k-NN classifier functions. Other libraries are generally permitted by the beta. The PDF must not contain program source-code listings. Question 11 requires an algorithm, correctness argument and polynomial running-time bound, with no implementation required.

## Where each question lives

| Notebook / report | Questions | Purpose |
| --- | --- | --- |
| `notebooks/01_part1_q01_q03_basis_regression.ipynb` | 1–3 | Polynomial fits, overfitting and sinusoidal bases |
| `notebooks/02_part1_q04_q05_housing_krr.ipynb` | 4–5 | Shared filtered housing data, baselines, cross-validation and comparison |
| `notebooks/03_part2_q06_q08_knn.ipynb` | 6–8 | Voted-centre visualisation and Protocols A and B |
| Overleaf `part3.tex` | 9–11 | Kernel proofs and Whack-A-Mole algorithm analysis |

Questions 4 and 5 share one notebook so dataset handling, the outer splits and the comparison table stay together. Questions 6–8 share the hypothesis generator and k-NN implementation. **Each notebook should run independently from a restarted kernel, top to bottom.** Do not rely on variables from another notebook.

## Setup and running

Recommended starting point: Python 3.11 or 3.12. The final experimental environment is not yet validated or locked.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m jupyter lab
```

On Windows, activate with `.venv\Scripts\activate` instead. Open one of the notebooks above. Implement its empty cells, then use **Restart Kernel and Run All Cells**. The three notebooks need not be run in a particular order.

`requirements.txt` is a starter dependency list, not a tested environment lock. Once the implementation works in a clean environment, record the exact Python version and validated dependency versions with the final submission. Do not claim results are reproducible until a fresh run has verified them.

## Project layout

```text
notebooks/       Three empty notebooks with question/subpart headings
src/             Optional shared implementation modules, added as needed
data/            Data source and placement instructions; raw CSV stays local
results/figures/ Plot exports for the report
results/tables/  Numerical summaries for the report
results/README.md  Run metadata and output naming conventions
scripts/         Notebook structure check and source ZIP exporter
docs/            Requirements, provenance and collaboration guidance
```

See `data/README.md` before Question 4. Save readable vector PDF figures for Overleaf where possible. Use repository-relative paths and document seed(s), split sizes, parameter grids, repetitions, tie handling and output filenames. Full protocols are computationally substantial: document any exploratory reduced run separately and generate the required full results before submission.

## Quality checks and submission export

```sh
python scripts/check_notebooks.py
python scripts/build_submission.py
```

The first command checks structural consistency without executing experiments. It reports empty code cells as template status. The exporter deliberately refuses notebooks with no implemented Python code. It is a packaging guard, not a proof of correctness or completeness. Manually review all work and the final brief before submission.

When ready, the exporter creates `dist/comp0078-cw1-code.zip` with code, notebooks, documentation and declared requirements. It excludes Git history, virtual environments, caches, generated results and raw data. Include the correct dataset in the ZIP only if the final instructions and its redistribution permissions allow this; otherwise provide verified acquisition instructions. Submit the PDF separately.

## Collaboration and grading access

The repository is currently private. Public visibility has been requested but remains pending explicit approval. If made public, anyone can read and fork all current and future contents; direct pushes remain limited to the owner and authorised collaborators. Recheck the course rules before adding assessed solutions. Work in small commits; separate branches for Part I and Parts II/III can reduce conflicts. Shared methods can move into `src/` once they exist. No open-source licence has been assigned.

[Overleaf report](https://www.overleaf.com/project/6adcf4bd4fea8d07d42c0cec).

No collaborators or graders have been invited yet. Juan Antonio's suggested account is `jrodriguezru`, pending verification; marker accounts and the course's access procedure are not known. Grant access only to the intended group member and authorised markers, following the module's instructions.

**Identification for final submission:** names and emails above identify the collaboration group. UCL's [anonymous-submission guidance](https://ucldata.atlassian.net/wiki/spaces/ELearningStudentSupport/pages/63471883) says work marked anonymously should use candidate numbers rather than names, user IDs or UPI. Confirm the applicable module rules before sharing a named repository for grading or exporting the report; the beta does not resolve this. Do not invent candidate numbers.

Further details: `docs/coursework-requirements.md` and `docs/collaboration.md`.
