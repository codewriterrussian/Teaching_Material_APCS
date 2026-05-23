# Windows VS Code / Jupyter 安裝 `ipykernel` 問題整理

## 問題現象

在 PowerShell 執行以下指令時：

```powershell
c:/Users/howar/.local/bin/python3.14.exe -m pip install ipykernel -U --user --force-reinstall
```

出現錯誤：

```text
error: externally-managed-environment

× This environment is externally managed
╰─> This Python installation is managed by uv and should not be modified.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider.
You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
```

---

## 問題原因

這個 Python：

```powershell
c:/Users/howar/.local/bin/python3.14.exe
```

是由 **uv 管理的 Python 環境**。

因此系統不允許你直接用 `pip install --user` 把套件安裝進去。這是因為 Python 採用了 PEP 668 的保護機制，避免使用者直接修改被工具或系統管理的 Python 環境。

簡單說：

> 這個 Python 不是給你直接用 `pip install` 修改的。

---

## 不建議的做法

不要對初學者或 code-zero 使用者使用這個方式：

```powershell
--break-system-packages
```

例如不要執行：

```powershell
c:/Users/howar/.local/bin/python3.14.exe -m pip install ipykernel --break-system-packages
```

原因是這可能會破壞 uv 管理的 Python 環境，之後 VS Code、Jupyter 或 Python 套件可能會出現更難修的問題。

---

## 建議解法：建立專案自己的 `.venv`

最安全、最適合 VS Code 的方式，是在目前資料夾建立一個虛擬環境 `.venv`，然後把 `ipykernel` 安裝在這個環境裡。

請在 PowerShell 執行：

```powershell
cd C:\Users\howar\OneDrive\桌面
uv venv .venv
.\.venv\Scripts\activate
python -m pip install -U pip
python -m pip install ipykernel
python -m ipykernel install --user --name desktop-python --display-name "Python Desktop"
```

---

## 指令說明

### 1. 進入桌面資料夾

```powershell
cd C:\Users\howar\OneDrive\桌面
```

這代表接下來的 Python 環境會建立在桌面資料夾底下。

---

### 2. 建立虛擬環境

```powershell
uv venv .venv
```

這會建立一個叫做 `.venv` 的 Python 虛擬環境。

`.venv` 可以想成是這個專案自己的 Python，不會影響系統或 uv 管理的 Python。

---

### 3. 啟動虛擬環境

```powershell
.\.venv\Scripts\activate
```

成功後，PowerShell 前面通常會出現類似：

```text
(.venv) PS C:\Users\howar\OneDrive\桌面>
```

這表示目前已經進入 `.venv` 環境。

---

### 4. 更新 pip

```powershell
python -m pip install -U pip
```

這會更新目前 `.venv` 裡面的 pip。

---

### 5. 安裝 ipykernel

```powershell
python -m pip install ipykernel
```

這會把 Jupyter Notebook 需要的 kernel 套件安裝到 `.venv` 裡。

---

### 6. 註冊 Jupyter Kernel

```powershell
python -m ipykernel install --user --name desktop-python --display-name "Python Desktop"
```

這會讓 VS Code / Jupyter 可以看到一個叫做：

```text
Python Desktop
```

的 Notebook kernel。

---

## VS Code 裡面要怎麼選 Python

在 VS Code 裡：

1. 按下 `Ctrl + Shift + P`
2. 搜尋：

```text
Python: Select Interpreter
```

3. 選擇：

```text
.\.venv\Scripts\python.exe
```

這樣 VS Code 就會使用剛剛建立的 `.venv` 環境。

---

## Jupyter Notebook 裡面要怎麼選 Kernel

如果是打開 `.ipynb` Notebook 檔案：

1. 點右上角的 Kernel 選單
2. 選擇：

```text
Python Desktop
```

這樣 Notebook 就會使用剛剛註冊的 kernel。

---

## 如果 `uv` 指令不能用

如果 PowerShell 出現：

```text
uv: The term 'uv' is not recognized
```

代表這台電腦目前找不到 `uv` 指令。

可以改用 Windows 內建常見的 `py` 指令建立虛擬環境：

```powershell
cd C:\Users\howar\OneDrive\桌面
py -m venv .venv
.\.venv\Scripts\activate
python -m pip install -U pip ipykernel
python -m ipykernel install --user --name desktop-python --display-name "Python Desktop"
```

然後一樣到 VS Code 選：

```text
.\.venv\Scripts\python.exe
```

Notebook kernel 選：

```text
Python Desktop
```

---

## 最重要的觀念

不要直接修改這個 Python：

```powershell
c:/Users/howar/.local/bin/python3.14.exe
```

因為它是 uv 管理的 Python。

正確做法是：

> 幫專案建立自己的 `.venv`，然後在 `.venv` 裡安裝 `ipykernel`。

這樣比較安全，也比較適合初學者使用 VS Code 和 Jupyter Notebook。
