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

## Deployment

### Deploy to a local terminal workspace

```powershell
git clone https://github.com/Jieke788/jieke788.git
cd jieke788
Get-ChildItem .\skills\graduate-company-review
```

### Deploy to Codex

```powershell
git clone https://github.com/Jieke788/jieke788.git "$env:TEMP\jieke788"
Remove-Item -Recurse -Force "$env:USERPROFILE\.codex\skills\graduate-company-review" -ErrorAction SilentlyContinue
Copy-Item -Recurse -Force "$env:TEMP\jieke788\skills\graduate-company-review" "$env:USERPROFILE\.codex\skills\graduate-company-review"
```

### Deploy to CC

```powershell
git clone https://github.com/Jieke788/jieke788.git "$env:TEMP\jieke788"
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\projects\skills" | Out-Null
Remove-Item -Recurse -Force "$env:USERPROFILE\.claude\projects\skills\graduate-company-review" -ErrorAction SilentlyContinue
Copy-Item -Recurse -Force "$env:TEMP\jieke788\skills\graduate-company-review" "$env:USERPROFILE\.claude\projects\skills\graduate-company-review"
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
