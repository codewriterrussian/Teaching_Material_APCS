# Lesson 1B ZeroJudge / APCS 題目完整練習教材

---

## 本份教材會練習的題目

| 題號 | 題目名稱 | 主要練習 |
| --- | --- | --- |
| zerojudge a003 | 兩光法師占卜術 | 條件判斷、公式計算 |
| zerojudge b964 | 成績指標 | 排序、最高不及格、最低及格、特殊情況 |
| zerojudge a017 | 五則運算 | `eval()`、EOF 多行輸入、整數除法 |
| zerojudge c291 | 小群體 | visited 標記、追蹤關係、計算 cycle 數量 |
| zerojudge b966 | 線段覆蓋長度 | 排序、區間合併、計算總長度 |

---

# Part 1. zerojudge a003 兩光法師占卜術

## 題目說明

兩光法師想用電腦加快算命速度。

他的占卜規則如下：

```
M = 月
D = 日
S = (M * 2 + D) % 3
```

接著根據 `S` 的值輸出運勢：

| S | 運勢 |
| --- | --- |
| 0 | 普通 |
| 1 | 吉 |
| 2 | 大吉 |

---

## 輸入說明

輸入共一行，包含兩個整數，分別代表月份 `M` 和日期 `D`。

---

## 輸出說明

輸出對應的運勢文字。

---

## 範例輸入 1

```
1 1
```

## 範例輸出 1

```
普通
```

---

## 範例輸入 2

```
1 2
```

## 範例輸出 2

```
吉
```

---

## IFPO 拆解

| 步驟 | 內容 |
| --- | --- |
| INPUT | 讀入月份 `m` 和日期 `d` |
| FUNCTION | 可以建立一個把數字轉成運勢文字的函式 |
| PROCESS | 計算 `s = (m * 2 + d) % 3` |
| OUTPUT | 印出對應的運勢 |

---

## 解題提示

先算出占卜數字：

```python
s = (m * 2 + d) % 3
```

再根據 `s` 的值判斷要輸出什麼：

```python
if s == 0:
    print("普通")
elif s == 1:
    print("吉")
else:
    print("大吉")
```

---

## 學生練習版

```python
# STEP 1. INPUT
m, d = map(int, input().split())

# STEP 2. FUNCTION
def fortune_text(s):
    #TODO: s 是 0 回傳 "普通"，1 回傳 "吉"，2 回傳 "大吉"
    return None

# STEP 3. PROCESS
s = None  #TODO: 計算 (m * 2 + d) % 3
ans = fortune_text(s)

# STEP 4. OUTPUT
print(ans)
```

---

# Part 2. zerojudge b964 成績指標

## 題目說明

一次考試中：

- 及格學生中，最低分數者最幸運。
- 不及格學生中，最高分數者最不幸。

假設及格分數為 `60`。

請讀入全班成績，先將所有成績由小到大排序，再找出：

1. 最高不及格分數
2. 最低及格分數

如果所有人都及格，沒有不及格分數，第二行輸出：

```
best case
```

如果所有人都不及格，沒有及格分數，第三行輸出：

```
worst case
```

---

## 輸入說明

第一行輸入學生人數 `n`。

第二行輸入 `n` 個學生分數，分數中間以空白隔開。

---

## 輸出說明

每筆測資輸出三行：

第一行：由小到大輸出所有成績，兩個數字之間有一個空白，最後一個數字後面沒有空白。

第二行：輸出最高不及格分數；如果全數及格，輸出 `best case`。

第三行：輸出最低及格分數；如果全數不及格，輸出 `worst case`。

---

## 範例輸入 1

```
10
0 11 22 33 55 66 77 99 88 44
```

## 範例輸出 1

```
0 11 22 33 44 55 66 77 88 99
55
66
```

---

## 範例輸入 2

```
1
13
```

## 範例輸出 2

```
13
13
worst case
```

---

## 範例輸入 3

```
2
73 65
```

## 範例輸出 3

```
65 73
best case
65
```

---

## IFPO 拆解

| 步驟 | 內容 |
| --- | --- |
| INPUT | 讀入人數 `n` 和成績 list |
| FUNCTION | 可以建立找最高不及格、最低及格的函式 |
| PROCESS | 排序成績，找出小於 60 的最高分與大於等於 60 的最低分 |
| OUTPUT | 印出排序後成績、最高不及格、最低及格 |

---

## 解題提示 1：排序

```python
scores.sort()
```

---

## 解題提示 2：印出中間有空白的 list

如果有一個整數 list：

```python
scores = [0, 11, 22, 33]
```

要印成：

```
0 11 22 33
```

可以使用：

```python
print(" ".join(map(str, scores)))
```

---

## 解題提示 3：找不及格與及格

```python
fail_scores = [x for x in scores if x < 60]
pass_scores = [x for x in scores if x >= 60]
```

---

## 學生練習版

```python
# STEP 1. INPUT
n = int(input())
scores = list(map(int, input().split()))

# STEP 2. FUNCTION
def highest_fail(scores):
    #TODO: 回傳最高不及格分數，如果沒有不及格分數，回傳 "best case"
    return None

def lowest_pass(scores):
    #TODO: 回傳最低及格分數，如果沒有及格分數，回傳 "worst case"
    return None

# STEP 3. PROCESS
scores.sort()
hf = highest_fail(scores)
lp = lowest_pass(scores)

# STEP 4. OUTPUT
print(" ".join(map(str, scores)))
print(hf)
print(lp)
```

---

## 常見錯誤

### 錯誤 1：最後多印空白

```python
for x in scores:
    print(x, end=" ")
```

這樣最後一個數字後面也會有空白，Online Judge 可能會判錯。

建議使用：

```python
print(" ".join(map(str, scores)))
```

---

### 錯誤 2：忘記處理 best case / worst case

如果所有人都及格：

```
65 73
```

沒有不及格分數，所以第二行要輸出：

```
best case
```

如果所有人都不及格：

```
13
```

沒有及格分數，所以第三行要輸出：

```
worst case
```

---

# Part 3. zerojudge a017 五則運算

## 題目說明

輸入多行五則運算式，請計算每一行的結果。

運算子包含：

```
+ - * / % ( )
```

題目中的 `/` 是整數除法，因此在 Python 中可以改成 `//`。

---

## 輸入說明

輸入資料有多行，直到 EOF 為止。

每一行是一個運算式，運算元與運算子之間會用空白隔開。

---

## 輸出說明

對每一行輸入，輸出該運算式的計算結果。

---

## 範例輸入

```
2 + 3 * 4
2 * ( 3 + 4 ) * 5
```

## 範例輸出

```
14
70
```

---

## IFPO 拆解

| 步驟 | 內容 |
| --- | --- |
| INPUT | 使用 `sys.stdin` 讀取多行資料 |
| FUNCTION | 這題可以不用額外函式 |
| PROCESS | 把 `/` 改成 `//`，再用 `eval()` 計算 |
| OUTPUT | 每讀到一行，就輸出一個答案 |

---

## 解題提示 1：讀到 EOF

這題不是只輸入一行，而是有多行輸入，直到 EOF。

可以使用：

```python
import sys

for line in sys.stdin:
    print(line)
```

---

## 解題提示 2：把 `/` 改成 `//`

Python 的 `/` 會做一般除法，結果可能是小數。

```python
print(5 / 2)   # 2.5
```

Python 的 `//` 會做整數除法。

```python
print(5 // 2)  # 2
```

所以可以用：

```python
line = line.replace("/", "//")
```

---

## 解題提示 3：使用 `eval()`

```python
print(eval("2 + 3 * 4"))
```

結果：

```
14
```

---

## 學生練習版

```python
import sys

# STEP 1. INPUT
for line in sys.stdin:
    # STEP 2. FUNCTION
    # 這題可以不用額外函式

    # STEP 3. PROCESS
    line = None  #TODO: 把 "/" 改成 "//"
    ans = None   #TODO: 使用 eval() 計算 line

    # STEP 4. OUTPUT
    print(ans)
```

---

## 安全提醒

`eval()` 會執行字串中的 Python 程式碼，所以平常不建議拿來處理不可信任的輸入。

在這題中可以使用，是因為 Online Judge 的輸入格式受到題目限制。

---

# Part 4. zerojudge c291 小群體

## 題目說明

有 `N` 個人，編號從 `0` 到 `N - 1`。

每個人都寫下他最好朋友的編號。

每個人的好友編號會形成一種關係：

```
自己 -> 好友 -> 好友的好友 -> ...
```

最後一定會形成一個圈，這個圈就是一個小群體。

請計算總共有幾個小群體。

---

## 範例說明

假設 `N = 10`，好友編號如下：

| 自己編號 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 好友編號 | 4 | 7 | 2 | 9 | 6 | 0 | 8 | 1 | 5 | 3 |

從 `0` 開始追蹤：

```
0 -> 4 -> 6 -> 8 -> 5 -> 0
```

所以 `{0, 4, 6, 8, 5}` 是一個小群體。

從 `1` 開始追蹤：

```
1 -> 7 -> 1
```

所以 `{1, 7}` 是另一個小群體。

這個例子最後共有 `4` 個小群體。

---

## 輸入說明

第一行輸入一個正整數 `N`。

第二行輸入 `N` 個整數，依序代表：

```
0 的好友、1 的好友、2 的好友、...、N-1 的好友
```

---

## 輸出說明

輸出小群體的數量。

---

## 範例輸入 1

```
10
4 7 2 9 6 0 8 1 5 3
```

## 範例輸出 1

```
4
```

---

## 範例輸入 2

```
3
0 1 2
```

## 範例輸出 2

```
3
```

注意：如果輸入是 `0 1 2`，代表每個人都是自己的好友，所以有 `{0}`、`{1}`、`{2}` 三個小群體。

---

## IFPO 拆解

| 步驟 | 內容 |
| --- | --- |
| INPUT | 讀入 `n` 和好友關係 `friends` |
| FUNCTION | 建立一個從某個人開始追蹤好友的函式 |
| PROCESS | 使用 `visited` 記錄誰已經被追蹤過；每找到一個新群體，答案加 1 |
| OUTPUT | 印出小群體數量 |

---

## 核心概念：visited 標記

我們可以建立一個 list 來記錄每個人是否已經拜訪過：

```python
visited = [False] * n
```

如果 `visited[3] == False`，代表 3 號還沒有被追蹤過。

如果 `visited[3] == True`，代表 3 號已經在某個小群體中。

---

## 解題提示

從一個人開始，一直走到已經拜訪過的人為止：

```python
cur = start

while not visited[cur]:
    visited[cur] = True
    cur = friends[cur]
```

---

## 學生練習版

```python
# STEP 1. INPUT
n = int(input())
friends = list(map(int, input().split()))

# STEP 2. FUNCTION
def find_group(start):
    #TODO: 從 start 開始追蹤好友，並把追蹤過的人標記為 True
    return None

# STEP 3. PROCESS
visited = [False] * n
ans = 0

for i in range(n):
    if not visited[i]:
        find_group(i)
        ans += 1

# STEP 4. OUTPUT
print(ans)
```

---

## 常見錯誤

### 錯誤 1：沒有標記 visited

如果沒有標記，程式可能會一直在圈裡走不出來。

例如：

```
0 -> 4 -> 6 -> 8 -> 5 -> 0 -> 4 -> ...
```

---

### 錯誤 2：每個人都直接 `ans += 1`

不是每個人都是一個新群體。

只有當這個人還沒有被拜訪過時，才代表找到新的小群體。

正確判斷：

```python
if not visited[i]:
    find_group(i)
    ans += 1
```

---

# Part 5. zerojudge b966 線段覆蓋長度

## 題目說明

給定一維座標上的一些線段，求這些線段覆蓋的總長度。

注意：重疊的部分只能算一次。

例如有線段：

```
(5, 6), (1, 2), (4, 8), (7, 9)
```

覆蓋範圍是：

```
1 到 2
4 到 9
```

所以總長度是：

```
1 + 5 = 6
```

---

## 輸入說明

第一行輸入一個正整數 `N`，代表有 `N` 條線段。

接下來 `N` 行，每一行包含兩個整數 `L` 和 `R`，代表線段的開始與結束位置。

---

## 輸出說明

輸出所有線段的總覆蓋長度。

---

## 範例輸入 1

```
5
160 180
150 200
280 300
300 330
190 210
```

## 範例輸出 1

```
110
```

---

## 範例輸入 2

```
1
120 120
```

## 範例輸出 2

```
0
```

---

## IFPO 拆解

| 步驟 | 內容 |
| --- | --- |
| INPUT | 讀入 `N` 條線段 |
| FUNCTION | 可以不用額外函式，也可以建立合併線段函式 |
| PROCESS | 依照起點排序，逐一合併重疊線段，累加不重複長度 |
| OUTPUT | 印出總覆蓋長度 |

---

## 核心概念：先排序再合併

先把線段依照起點排序：

```python
segments.sort(key=lambda x: (x[0], x[1]))
```

例如：

```
160 180
150 200
280 300
```

排序後會變成：

```
150 200
160 180
280 300
```

---

## 核心概念：維護目前區間

假設目前覆蓋區間是：

```
[start, end]
```

下一條線段是：

```
[left, right]
```

如果：

```python
left > end
```

代表新的線段和目前區間沒有重疊。

這時要先把目前區間長度加進答案：

```python
total += end - start
```

然後換成新的區間：

```python
start, end = left, right
```

如果：

```python
left <= end
```

代表有重疊。

這時不用立刻加長度，只要更新右端點：

```python
if right > end:
    end = right
```

---

## 學生練習版

```python
# STEP 1. INPUT
n = int(input())
segments = []

for _ in range(n):
    l, r = map(int, input().split())
    segments.append([l, r])

# STEP 2. FUNCTION
# 這題可以先不用額外函式

# STEP 3. PROCESS
segments.sort(key=lambda x: (x[0], x[1]))

total = 0
start, end = segments[0]

for i in range(1, n):
    left, right = segments[i]

    if left > end:
        #TODO: 目前線段結束，累加長度，並更新 start, end
        pass
    else:
        #TODO: 線段重疊，必要時更新 end
        pass

#TODO: 最後一段區間也要加進 total

# STEP 4. OUTPUT
print(total)
```

---

## 常見錯誤

### 錯誤 1：忘記排序

如果沒有排序，就很難正確判斷哪些線段可以合併。

---

### 錯誤 2：重疊部分重複計算

例如：

```
150 200
160 180
```

第二條線段完全被第一條包住，所以不能再加一次。

---

### 錯誤 3：忘記加最後一段

迴圈中只有遇到「不重疊」時才會把前一段加進 total。

所以迴圈結束後，最後一段還需要補上：

```python
total += end - start
```

---