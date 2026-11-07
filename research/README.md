# Research Papers and Literature Surveys
Hey everyone!

We need to complete the Research Paper Collection and Literature Survey task for our Capstone project: **Incident Response and Resilient Recovery**.

Each person has been assigned a separate GitHub Issue. Please follow the instructions below carefully so that everyone's work gets submitted properly through GitHub Pull Requests.

# 1. Understand what you need to submit

Each person must:

1. Find relevant research papers related to our project.
2. Read and analyse the selected papers.
3. Prepare a detailed Literature Survey.
4. Convert the Literature Survey into a PDF.
5. Download and include the original research paper PDFs.
6. Upload everything to our GitHub repository through a Pull Request.

**Your submission must contain both the original research papers and your Literature Survey PDF.**

# 2. Clone the GitHub repository

First, open our GitHub repository:

[INSERT GITHUB REPOSITORY LINK]

Open the repository and click the green **Code** button.

Copy the HTTPS URL.

Open VS Code or PowerShell and execute:

```bash
git clone YOUR_REPOSITORY_URL
```

For example:

```bash
git clone https://github.com/USERNAME/Incident-Response-and-Resilient-Recovery.git
```

Enter the project directory:

```bash
cd Incident-Response-and-Resilient-Recovery
```

This downloads the project onto your computer.

# 3. Create your own branch

IMPORTANT: Do not work directly on the main branch.

Each person must create a separate branch.

Use the following naming convention:

Member 1:
```bash
git checkout -b research/member-1
```

Member 2:
```bash
git checkout -b research/member-2
```

Member 3:
```bash
git checkout -b research/member-3
```

Member 4:
```bash
git checkout -b research/member-4
```

Make sure you create the branch corresponding to your assigned issue.

# 4. Create your folder structure

Inside the project directory, create a folder named `research`.

Inside it, create your own folder.

For example, Member 1 should have:

```text
research/
└── member-1/
    ├── literature_survey.pdf
    └── papers/
        ├── paper-1.pdf
        ├── paper-2.pdf
        ├── paper-3.pdf
        └── paper-4.pdf
```

Similarly, other members should use:

```text
research/
├── member-1/
├── member-2/
├── member-3/
└── member-4/
```

Do not upload your files into another member's folder.

# 5. Prepare your Literature Survey

Your Literature Survey PDF should be properly structured.

For every research paper, include:

1. Paper title.
2. Author names.
3. Publication year.
4. Journal/conference name.
5. Problem statement.
6. Proposed methodology.
7. Algorithms or technologies used.
8. Key findings and results.
9. Limitations.
10. Research gaps and relevance to our project.

At the end, include:
- Comparative analysis of the selected papers.
- Identified research gaps.
- References with DOI or original publication links wherever available.

Please don't just copy abstracts from research papers. Read, understand and write the survey in your own words.

# 6. Add your files to Git

Once your PDFs are ready, place them inside your assigned folder.

For example, Member 1:

```text
research/member-1/
```

Open the terminal inside the repository and execute:

```bash
git status
```

This displays the files you have added.

Now stage your files:

```bash
git add research/member-1/
```

Commit your changes:

```bash
git commit -m "Add research papers and literature survey - Member 1"
```

Replace Member 1 with your own member number.

# 7. Push your branch to GitHub

Execute:

```bash
git push -u origin research/member-1
```

Replace the branch name with your own.

Your files are now uploaded to GitHub, but they are not yet merged into the main branch.

# 8. Create a Pull Request (VERY IMPORTANT)

Now go to our GitHub repository.

1. Open the **Pull Requests** tab.
2. Click **New Pull Request**.
3. Select `main` as the base branch.
4. Select your research branch as the compare branch.
5. Check that only your files are included.
6. Click **Create Pull Request**.

Use the following PR title:

`Add research papers and literature survey - Member 1`

In the PR description, mention your assigned issue:

```text
Closes #ISSUE_NUMBER

Added:
- Literature survey PDF
- Original research paper PDFs
- Comparative analysis
- Research gaps and references
```

Replace `ISSUE_NUMBER` with the number of your assigned GitHub Issue.

# 9. What happens after submitting the PR?

Once you create the Pull Request:

- I will review the submitted PDFs.
- I'll check the folder structure and completeness.
- If changes are required, I'll request modifications.
- Once everything is approved, the PR will be merged into `main`.
- Your assigned issue will automatically close after merging because of the `Closes #ISSUE_NUMBER` reference.

# 10. Important rules

1. Do not push directly to `main`.
2. Each person must use their own branch.
3. Do not modify another member's folder.
4. Submit original research paper PDFs along with your Literature Survey PDF.
5. Use proper file names.
6. Ensure the PDFs open correctly.
7. Do not create multiple PRs for the same task unless requested.
8. Link your assigned issue in the PR.

**Final submission checklist:**

- [ ] Relevant research papers collected.
- [ ] Original research paper PDFs downloaded.
- [ ] Literature Survey completed.
- [ ] Comparative analysis included.
- [ ] Research gaps identified.
- [ ] All PDFs placed in your assigned folder.
- [ ] Changes committed and pushed to your branch.
- [ ] Pull Request created.
- [ ] Assigned issue linked in the PR.

Please follow this workflow so that we maintain a clean GitHub repository and can track everyone's contribution properly.

If you face any Git errors while cloning, creating branches, pushing or creating PRs, share a screenshot in the group instead of making random changes to the repository.

Thanks everyone!
