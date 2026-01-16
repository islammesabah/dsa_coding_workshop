# Cursor AI Installation Guide for Debian

This guide provides a step-by-step walkthrough for installing **Cursor AI** on Debian-based distributions. While there are multiple ways to get started, the AppImage method is the most reliable for stability and dependency management.

---

## 🚀 Quick Start (One-Liner)

If you already have the file, run this in your terminal to get started immediately:

```bash
chmod +x Cursor.AppImage && ./Cursor.AppImage

```

---

## ✅ Method 1: AppImage (Recommended)

This is the preferred option for Debian users. It avoids potential dependency conflicts and works seamlessly across different versions of the OS.

### 1. Download Cursor

Visit the [official website](https://cursor.sh) and download the Linux AppImage, or use `wget` in your terminal:

```bash
cd ~/Downloads
wget https://download.cursor.sh/linux/Cursor.AppImage

```

### 2. Make it Executable

You must give the file permission to run as a program:

```bash
chmod +x Cursor.AppImage

```

### 3. Run Cursor

```bash
./Cursor.AppImage

```

### 4. Integrate with System Menu (Optional)

To make Cursor appear in your applications list rather than running it from the terminal every time:

1. **Install FUSE support:** ```bash
sudo apt install libfuse2
```

```


2. **Integrate:** Right-click the `.AppImage` file in your file manager and select **"Integrate and run"** (if using an AppImage launcher) or create a desktop entry.

---

## 🛠️ Method 2: Manual .deb Install

If a `.deb` package is specifically provided or preferred for your workflow:

1. **Install the package:**
```bash
sudo apt install ./cursor_*.deb

```


2. **Fix missing dependencies:**
If the installation fails due to missing packages, run:
```bash
sudo apt --fix-broken install

```



> [!IMPORTANT]
> **Why AppImage?** On Linux, many modern AI tools ship as AppImages because they bundle all necessary libraries, ensuring they work across various distributions without manual dependency hunting.

---

## 🔍 Verification & Setup

Once the application opens, follow these steps to finalize your setup:

* **Settings:** Navigate to `Cursor` → `Settings`.
* **AI Configuration:** Check your AI Model and Copilot settings.
* **Authentication:** Sign in via GitHub or Email to sync your preferences.

---

## ❌ Common Issues & Fixes

| Issue | Solution |
| --- | --- |
| **Cursor won't start** | Ensure FUSE is installed: `sudo apt install libfuse2` |
| **Permission Denied** | Run `chmod +x Cursor.AppImage` to enable execution. |
| **Sandboxing issues** | If it fails to launch, try: `./Cursor.AppImage --no-sandbox` |

---

> **Summary:** On Debian, Cursor AI is best installed as an AppImage: **Download, make executable, and run.**
