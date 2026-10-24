# Requirements and source record

Checked: 24 October 2026. Authority: supplied `CW1_2627-v-beta.pdf` (9 pages), with the module's Moodle announcements checked for a later release. This file distinguishes confirmed requirements from our organisational choices.

## Confirmed in the beta

- Work individually or in groups of two or three; group members receive the same grade (page 1).
- Answer every task in a PDF; submit well-commented source code separately in a ZIP on Moodle. Do not print program code in the PDF (page 1).
- Assessment includes correctness/quality and clarity of presentation (page 1).
- Implement regression, with bases and kernels, directly via matrix algebra and k-NN directly. Other libraries are generally allowed (page 1).
- Parts I, II and III carry 50%, 20% and 30%, respectively (pages 1, 6, 7).
- Q2(d) and Q3 average 100 runs; use ln(mean error), not mean(log error) (page 3).
- Q4 uses 20 random two-thirds/one-third splits. Q5 uses training-only five-fold cross-validation and repeats tuning for each of the 20 outer splits; report mean MSE and SD across runs (pages 4–5).
- Q6 uses 100 sampled centres and generating hypothesis v=3 (page 6).
- Q7 follows Protocol A: k=1,...,49, 100 runs per k, 4000 training examples and 1000 test examples; roughly five explanation sentences (pages 6–7).
- Q8 follows Protocol B: m in {100,500,1000,1500,...,4000}, 100 runs, k=1,...,49 and 1000 test examples; average run-level optimal k; roughly four explanation sentences (page 7).
- Resolve undefined labels/predictions uniformly at random (page 7). The noisy-label process in Part II uses the hypothesis with probability 0.8 and otherwise a uniform binary label; do not substitute a deterministic flip (page 6).
- Q9 and Q10 request justified arguments, with proofs preferred (pages 7–8).
- Q11 needs a polynomial-in-n algorithm and correctness argument; no implementation required (page 9).

## Not specified in the supplied beta

GitHub submission, repository naming, GitHub Classroom, grader usernames, notebook format/count, dependency format, a source-code ZIP filename, font/margins, or a page/word limit. Our repo name and three-notebook grouping are choices, not UCL requirements. Individual questions do specify approximate explanation lengths as noted above.

## Release status

The [23 October announcement](https://moodle.ucl.ac.uk/mod/forum/discuss.php?d=1328571) attaches the beta and plans v1 for Monday, 26 October 2026. The announcements list still showed the beta as the latest coursework announcement when checked on 24 October. Reconcile every protocol and submission rule against v1 and subsequent staff clarification before final delivery. The beta's due date is 18 November 2026; the final time is unverified.

## UCL guidance and our recommendations

[UCL anonymous-submission guidance](https://ucldata.atlassian.net/wiki/spaces/ELearningStudentSupport/pages/63471883): where marking is anonymous, use candidate numbers and follow the assignment-specific instructions. Confirm this before sharing a repository identified by names or exporting the named Overleaf title page.

[UCL software sustainability guidance](https://www.ucl.ac.uk/library/open-science-research-support/research-data-management/best-practices/how-guides/software-sustainability-preservation-and-sharing): preserve the software version needed to verify results. Our recommendations are a clear README, dependency record, fixed seeds, question/output mapping and a final commit identifier. These are reproducibility practices, not additional marking criteria announced by COMP0078.

[UCL GitHub service guidance](https://www.ucl.ac.uk/research-innovation/advanced-research-computing/platforms-and-services/research-software-development/research-software-development-tools/support-ucl-researchers-use-github) describes GitHub access and service options; it does not establish a COMP0078 naming convention. Do not adopt another module's Classroom or naming rules without instructions from this module.
