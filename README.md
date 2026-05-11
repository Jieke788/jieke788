# auto_restructure_agent

This repository contains agent utilities and a reusable Codex skill for evaluating companies from a new-graduate job-seeking perspective.

## Included skill

### `graduate-company-review`

Location:

- `skills/graduate-company-review/`

Use this skill when you want Codex to:

- assess whether a company is worth applying to or joining for a new graduate
- review business quality, salary signals, city differences, hiring friendliness, growth prospects, and work-risk factors
- return a Chinese recommendation with a verdict such as `适合` / `谨慎` / `不推荐`
- automatically export a formal Chinese Word report (`.docx`)

## Skill invocation

Use the skill by name:

```text
$graduate-company-review
```

Example:

```text
用 $graduate-company-review 评估深圳某公司
```

## Output behavior

By default, the skill will:

1. produce a structured Chinese assessment in chat
2. generate a formatted Chinese Word report in the working directory

The Word export includes:

- cover title
- executive summary
- sectioned findings
- score table
- source list
- confidence note
