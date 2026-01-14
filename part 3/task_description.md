# Engineering with Gemini CLI: Beyond "Vibe Coding" 🚀

Welcome to the **DSA coding Workshop part 3**. In an era where AI coding tools are everywhere, we often fall into the "Paradox of Choice." This repository is dedicated to moving beyond the hype and using engineering principles to build more secure, transparent, and productive workflows using Google's **Gemini CLI**.

## 📌 The Paradox of Choice

Today, every major player has a CLI tool (OpenAI, AWS, Google). More tools often lead to more decision fatigue.

**Why Gemini CLI?**

* **Transparent:** It’s open-source; you can see how it's built, not just use it as a "black box."
* **Accessible:** Free to use and easy to integrate into existing terminal workflows.
* **Context-Aware:** Designed to handle complex engineering tasks like autonomous code reviews, not just simple snippets.

---

## 🛡️ The Security Landscape (2025 Trends)

We are currently facing a shift in cybersecurity:

* **Shadow AI Breaches:** 20% of breaches are linked to employees using unauthorized AI tools.
* **Supply Chain Fragility:** Credential leakage (like API keys in code) remains a top vulnerability.
* **The Goal:** We don't just "vibe code"—we use AI to find vulnerabilities, analyze logic, and enforce best practices.

---

## 💻 Workshop: The Password Strength Checker

In this workshop, we analyze a `password_strength_checker.py` script to identify flaws.

### 1. Baseline Run

Run the script manually to observe behavior:

```bash
python3 password_strength_checker.py

```

### 2. Enter Interactive Mode

Launch Gemini CLI to begin the review process:

```bash
gemini

```

### 3. The Review Workflow

Once in interactive mode (`>`), follow these steps:

1. **Context Loading:** `We are reviewing this file: @./password_strength_checker.py. Explain what this program does.`
2. **Challenge the AI:** `Re-read your explanation. List 3 places where you might be incomplete or too confident.`
3. **Edge Case Discovery:** `List edge cases this program does NOT handle well. Do not propose fixes yet.`
4. **Prioritization:** `Classify issues into P0 (must fix), P1 (should fix), and P2 (nice to have).`
5. **Testing:** `Propose 8 tests to verify correct behavior before we change any code.`
6. **The Minimal Fix:** `Propose the smallest possible code changes to fix P0 issues as a diff.`

---

## 🤖 Advanced: Multi-Agent Orchestration

We can go beyond a single chat by creating a **Team of Specialists**.

* **Agent A (The Security Specialist):** Focuses on vulnerabilities and exploits.
* **Agent B (The Logic Auditor):** Focuses on edge cases and business logic.
* **The Orchestrator:** Manages collaboration and synthesizes the final report.

This modular approach automates the "human-in-the-loop" review process, making it repeatable and scalable.

---

## 🔌 Giving AI Superpowers: MCP Servers

The **Model Context Protocol (MCP)** is the "USB port for AI." It allows Gemini CLI to do more than just talk—it allows it to **act**.

* **Prompt = Intention**
* **MCP = The Hands**
* **Tools = The Actions** (Reading GitHub, querying databases, taking notes in Obsidian, or summarizing Coursera videos).

### Best Practices for MCP

* ✅ **Do:** Sandbox actions and limit tool access.
* ✅ **Do:** Keep a human in the loop for critical writes.
* ❌ **Don't:** Give AI full disk access or production credentials.

---

## 🎓 Closing Thought

> **Responsible AI is not weaker — it’s safer and more useful.**
> Engineering with Generative AI is about defining boundaries. As engineers, we define the boundaries for AI so it remains a tool, not a liability.
