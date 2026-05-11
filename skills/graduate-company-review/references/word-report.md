# Word Report

Use this file when the skill exports the company assessment as a Word document.

## Goal

Export the final assessment as a formal Chinese `.docx` report that opens correctly in Word or WPS and shows Chinese text without mojibake or `?`.

## Required workflow

1. Finish the assessment in chat first.
2. Convert the assessment into a report structure.
3. Write the document generator as a UTF-8 script file on disk.
4. Run the script from disk.
5. Verify the generated file exists.
6. Return the saved `.docx` path to the user.

Do not send a large inline Python script with Chinese text directly through a terminal pipe when the environment is known to mangle non-ASCII characters.

## Encoding rules

- Keep the script file itself in UTF-8.
- Prefer saving the `.docx` with an ASCII filename if the runtime has trouble writing to non-ASCII paths.
- If needed, save to an ASCII temp path first, then copy the final file to the requested directory.
- If the user reports question marks in the document, inspect `word/document.xml`. If the XML already contains `?`, the text was corrupted before packaging and the document must be regenerated from a proper UTF-8 source file.

## Default layout

Use a clean formal report layout:

- cover title
- company name
- audience line such as `??????????`
- conclusion line
- report date
- executive summary
- business and current condition
- role and salary observations
- strengths and risks
- score table
- final conclusion
- source list
- confidence note

## Formatting defaults

- Font: `Microsoft YaHei`
- Body size: 11pt
- Section headings: stronger contrast than body text
- Use tables for summary and scorecard when helpful
- Keep margins suitable for printing
- Keep the final report concise and readable

## Generator usage

Use [../scripts/generate_company_report.py](../scripts/generate_company_report.py) as the default generator.

Pass it structured JSON with:

- report title
- company name
- audience
- verdict
- scope
- date
- summary
- best-for note
- sections
- score rows
- sources
- confidence
- output path
- optional temp output path

## Default behavior

- Export a Word file by default after each completed company assessment.
- Use the current working directory unless the user requests another destination.
- Prefer an ASCII filename even when the company name is Chinese.
- Keep the document body and headings in Chinese.
