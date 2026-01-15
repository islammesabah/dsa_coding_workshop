# Gemini CLI Project Context

This project uses a multi-agent review system powered by Gemini CLI Skills.

## Available Skills

The following skills are available to assist with code reviews and improvements:

1.  **bugs** (`.gemini/skills/bugs`): Senior Logic & Correctness Reviewer.
2.  **security** (`.gemini/skills/security`): Senior Security Auditor (OWASP Top 10).
3.  **best-practices** (`.gemini/skills/best-practices`): Principal Engineer (SOLID, Clean Code).
4.  **testing** (`.gemini/skills/testing`): SDET (Test Strategy & Cases).
5.  **ethics** (`.gemini/skills/ethics`): Ethics & Compliance Officer.
6.  **code-fixer** (`.gemini/skills/code-fixer`): Senior Code Fixer. **(Only use when explicitly requested)**

## Workflow

When asked to review a file (e.g., `tweeter.py`), follow this process by activating the relevant skills:

### 1. Analysis Phase
Activate the following skills in sequence or parallel to analyze the target file:
- `bugs`
- `security`
- `best-practices`
- `testing`
- `ethics`

Each skill should output its findings to a dedicated file in a review directory (e.g., `reviews/[filename]_review_v[N]/`).

### 2. Consolidation Phase
After all analyses are complete, synthesize the findings into a `MASTER_ANALYSIS.md` file in the review directory.

### 3. Remediation Phase (On Request Only)
If the user explicitly requests to fix the code, activate the `code-fixer` skill.
- The `code-fixer` will read the reviews and the target file.
- It will create a backup.
- It will write the fixed file.

## Usage
Simply ask: "Review [filename]" to start the analysis phase.
Ask "Fix [filename]" or "Apply fixes" to start the remediation phase.
