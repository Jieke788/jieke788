---
name: graduate-company-review
description: Evaluate whether a company is worth applying to or joining for a new graduate in China. Use when Codex needs to judge a company's business, role fit, salary signals, city differences, hiring friendliness, growth prospects, and work-risk factors for entry-level candidates, return a Chinese recommendation with evidence, confidence, and a final verdict such as 适合, 谨慎, or 不推荐, and automatically export the assessment as a formal Chinese Word report (.docx).
---

# Graduate Company Evaluator

Use this skill to assess a company for an upcoming graduate with a disciplined, evidence-first workflow. Keep the tone cautious and practical. Do not overstate certainty, and do not turn rumors into facts.

## Workflow

### 1. Confirm the target briefly

Infer the target from the user's request when possible. Collect these inputs if available:

- company name
- target city
- target role or role family
- graduate background, such as major, internship direction, or whether the user is deciding between offer acceptance and投递

If part of the target is missing, proceed with a reasonable default and state the assumption in one line.

### 2. Research live information on the web

Company condition, salary, and hiring signals are time-sensitive. Always verify them online when using this skill.

Gather evidence in this order:

1. 风鸟 or similar company profile source when available
2. company official site, careers page, and campus recruitment page
3. major job platforms and public salary samples
4. reputable news, encyclopedia, or industry materials
5. employee-review or forum-style sources only as weak signals

Read [references/source-policy.md](references/source-policy.md) before making claims.

### 3. Build the assessment from evidence

Summarize the company using only supported observations:

- core business and revenue logic
- market position or industry context
- whether the company appears friendly to new graduates
- common graduate roles and salary signals
- city differences when the city matters
- risk signals around overtime, turnover, management, layoffs, or business instability

Separate statements into:

- facts supported by strong sources
- inferences based on multiple signals
- rumors or weak signals that must stay clearly labeled

### 4. Score with a fixed rubric

Use the rubric in [references/scoring-rubric.md](references/scoring-rubric.md).

Score these dimensions on a 10-point scale:

- salary competitiveness
- growth potential
- business outlook
- stability
- workload risk
- management and reputation risk
- campus hiring friendliness
- role fit

Do not pretend precision when the evidence is thin. Lower confidence when data quality is weak or conflicting.

### 5. Report in a fixed structure

Use the output structure in [references/output-template.md](references/output-template.md).

The final answer in chat should always be in Chinese and should always include:

- company overview
- business and current condition
- role and salary observations
- strengths
- risks
- scorecard
- final verdict: `适合` / `谨慎` / `不推荐`
- sources
- confidence note

### 6. Automatically export a formal Word report

By default, after completing the assessment, also generate a formal Chinese `.docx` report even if the user did not separately repeat the export request.

Treat Word export as part of the standard deliverable unless the user explicitly says they do not want a file.

Use this workflow:

1. finish the company assessment first
2. convert the final Chinese assessment into a report-ready structure
3. generate the document from a UTF-8 script file, not by piping inline non-ASCII source through the terminal
4. save the file with an ASCII filename when the environment is sensitive to non-ASCII paths
5. place the final `.docx` in the current working directory unless the user asked for another location
6. verify the file exists after generation
7. return the clickable file path in the final answer

The default report style should be:

- Chinese cover title
- executive summary
- sectioned findings
- score table
- source list
- confidence note

Use an ASCII filename by default, such as:

- `company_assessment_<normalized-company-name>.docx`

If the company name is Chinese or contains characters that are awkward in filenames, normalize the filename to ASCII but keep the report body fully Chinese.

Read [references/word-report.md](references/word-report.md) before generating a Word file.
Use [scripts/generate_company_report.py](scripts/generate_company_report.py) as the default generator instead of rewriting document code each time.

### 7. Terminal and deployment commands

Use the following commands when you need to deploy the skill into another environment.

#### Deploy to a local terminal workspace

```powershell
git clone https://github.com/Jieke788/jieke788.git
cd jieke788
Get-ChildItem .\skills\graduate-company-review
```

#### Deploy to Codex

```powershell
git clone https://github.com/Jieke788/jieke788.git "$env:TEMP\jieke788"
Remove-Item -Recurse -Force "$env:USERPROFILE\.codex\skills\graduate-company-review" -ErrorAction SilentlyContinue
Copy-Item -Recurse -Force "$env:TEMP\jieke788\skills\graduate-company-review" "$env:USERPROFILE\.codex\skills\graduate-company-review"
```

#### Deploy to CC

```powershell
git clone https://github.com/Jieke788/jieke788.git "$env:TEMP\jieke788"
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\projects\skills" | Out-Null
Remove-Item -Recurse -Force "$env:USERPROFILE\.claude\projects\skills\graduate-company-review" -ErrorAction SilentlyContinue
Copy-Item -Recurse -Force "$env:TEMP\jieke788\skills\graduate-company-review" "$env:USERPROFILE\.claude\projects\skills\graduate-company-review"
```

### 8. End with an actionable suggestion

Close the chat response with the most practical next action for a graduate, such as:

- worth applying now
- apply selectively and keep comparing
- continue only if offer terms are strong
- avoid unless there is a specific reason

## Reporting rules

- Keep the answer structured and concise.
- Prefer explicit uncertainty over overconfident wording.
- Do not use a single employee post or forum thread as a factual basis.
- If sources conflict, say `存在分歧` and explain where the conflict appears.
- If salary samples are sparse, say `样本不足` and provide only a cautious range or directional judgment.
- If the company is small, obscure, or newly formed, reduce confidence and avoid strong conclusions.
- Put major risk signals before minor advantages when the downside is material.
- When exporting Word, keep Chinese text in a UTF-8 script file and avoid inline terminal piping for non-ASCII content.
- Unless the user opts out, do not stop after the chat answer; complete the `.docx` export and return the path.

## Resources

- Use [references/source-policy.md](references/source-policy.md) for evidence ranking and conflict handling.
- Use [references/scoring-rubric.md](references/scoring-rubric.md) for dimension scoring and verdict thresholds.
- Use [references/output-template.md](references/output-template.md) for the response structure.
- Use [references/role-salary-guidance.md](references/role-salary-guidance.md) for role mapping and salary expression rules.
- Use [references/word-report.md](references/word-report.md) for Word export rules and layout expectations.
- Use [scripts/generate_company_report.py](scripts/generate_company_report.py) to export a formal Chinese Word report.
