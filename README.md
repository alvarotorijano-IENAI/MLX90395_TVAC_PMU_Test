## 🚀 Setup

Follow these steps to set up the repository after cloning:

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```

2. **Run the setup script**  
   This will configure Git to use the shared hooks located in `.githooks/`.

   - On **Linux / macOS / Git Bash**:
     ```bash
     ./setup.sh
     ```
   - On **Windows (CMD)**:
     ```bat
     setup.bat
     ```

3. **Verify hooks are active**  
   Run:
   ```bash
   git config core.hooksPath
   ```
   It should output:
   ```
   .githooks
   ```

---

## 🔒 Notes

- The shared hooks prevent **fast-forward merges**.  
  This ensures a clean and traceable history.  
- Always merge features into `develop` using:
  ```bash
  git merge --no-ff feature/your-feature
  ```
  or
  ```bash
  git flow feature finish
  ```

- If you forget to run the setup script, merges may be blocked or misconfigured.  
