# Lesson 01：解題技巧與高階函式

先看懂題目，再整理輸入、處理流程與輸出。

認識幾個常用的 Python 工具，例如 `map()`、串列生成式、`lambda`、`eval()`，幫助你更快寫出簡潔的程式。

> 這堂課的重點：先拆題目，再用 Python 工具把解題流程寫清楚。
> 

---

## Section I. 今天要做什麼？

1. 認識解題時可以使用的「三步破題法」。
2. 學習 IFPO 四步解題流程。
3. 練習整理輸入、處理、輸出。
4. 認識幾個常用高階函式與簡潔寫法。
5. 完成幾題小型實作練習。

---

## Section II. 今天的學習方式

這堂課不是要你立刻背下所有寫法，而是練習「看到題目時要怎麼想」。

不用一開始就把所有規則背起來，先做到：

1. 看得懂題目的輸入與輸出。
2. 知道程式大概需要哪些步驟。
3. 能把題目拆成 INPUT、FUNCTION、PROCESS、OUTPUT。
4. 可以使用簡單工具讓程式更清楚。
5. 出錯時知道要檢查輸入、型態、輸出格式。

---

## Section III. 今天會學到的內容

| 主題 | 你需要知道的事 |
| --- | --- |
| 三步破題法 | 先看大綱，再看輸入輸出，最後對回題幹。 |
| IFPO | 用 INPUT、FUNCTION、PROCESS、OUTPUT 拆解程式。 |
| `map()` | 把同一個轉換函式套用到多個資料。 |
| 串列生成式 | 用一行建立新的 list。 |
| `lambda` | 建立簡短、一次性使用的小函式。 |
| `eval()` | 可以執行字串中的運算式，但使用時要小心。 |

---

## Section IV. 寫題目前的提醒

### 1. 先看懂題目

寫程式前，先問自己：

- 題目給我什麼資料？
- 我要回傳或輸出什麼？
- 中間需要做什麼計算？
- 有沒有特殊情況？

### 2. 先看範例輸入與範例輸出

很多 Online Judge 題目文字很多，第一次看可能會覺得很難。這時候可以先看範例：

- 輸入有幾行？
- 每一行是數字、字串，還是很多資料？
- 輸出有幾行？
- 輸出中間有沒有空格？

### 3. 注意 `return` 和 `print()` 不一樣

在練習函式題時，常常需要用 `return` 回傳答案。

```python
def add(a, b):
    return a + b
```

在 Online Judge 題目中，通常會用 `print()` 印出最後答案。

```python
a, b = map(int, input().split())
print(a + b)
```

### 4. 輸出格式要完全相同

Online Judge 通常會嚴格比對輸出結果。

```
15
```

和

```
15
```

可能被判定為不同，因為第二個結果後面多了一個空白。

---

## Section V. 核心概念說明

### 1. 三步破題法

遇到題目時，不一定要從第一個字開始慢慢讀。可以先用三步驟抓重點。

| 步驟 | 做什麼 |
| --- | --- |
| STEP 1 | 瀏覽題目，先了解大概在問什麼。 |
| STEP 2 | 觀察輸入與輸出範例。 |
| STEP 3 | 把範例對回題幹，確認規則。 |

例如看到「讀入兩個整數，輸出它們的和」，你可以先抓到：

```
輸入：兩個整數
處理：相加
輸出：總和
```

---

### 2. IFPO 四步解題流程

IFPO 是一種整理程式結構的方法。

| 縮寫 | 意思 | 要做的事 |
| --- | --- | --- |
| I | INPUT | 讀取輸入資料。 |
| F | FUNCTION | 建立可能重複使用的工具函式。 |
| P | PROCESS | 安排主要運算流程。 |
| O | OUTPUT | 印出或回傳結果。 |

簡單加法題可以這樣想：

```
INPUT：讀入 a, b
FUNCTION：這題很簡單，可以不用額外函式
PROCESS：計算 a + b
OUTPUT：印出答案
```

Python 範例：

```python
a, b = map(int, input().split())
ans = a + b
print(ans)
```

如果輸入是：

```
5 10
```

結果是：

```
15
```

---

### 3. 使用 `map()` 轉換多個輸入資料

`input().split()` 會把一行文字切成多個字串。

```python
data = input().split()
print(data)
```

如果輸入是：

```
5 10
```

結果是：

```
['5', '10']
```

這時候裡面的 `5` 和 `10` 其實還是字串。若要轉成整數，可以使用 `map(int, ...)`。

```python
a, b = map(int, input().split())
print(a + b)
```

如果輸入是：

```
5 10
```

結果是：

```
15
```

---

### 4. 使用串列生成式建立 list

串列生成式可以用比較短的方式建立新串列。

```python
scores = [int(i) for i in input().split()]
print(scores)
```

如果輸入是：

```
80 65 42
```

結果是：

```
[80, 65, 42]
```

這個寫法常用在「一行輸入很多個數字」的題目。

---

### 5. 使用 `lambda` 建立簡短函式

`lambda` 可以建立簡短、一次性使用的小函式。

```python
add = lambda a, b: a + b
print(add(3, 4))
```

結果：

```
7
```

也可以搭配條件判斷：

```python
check = lambda x: "even" if x % 2 == 0 else "odd"
print(check(5))
```

結果：

```
odd
```

初學時不一定要馬上大量使用 `lambda`，先看得懂就可以。

---

### 6. `eval()` 可以計算字串中的運算式

`eval()` 可以把字串當成 Python 運算式執行。

```python
print(eval("2 + 3 * 4"))
```

結果：

```
14
```

提醒：`eval()` 雖然方便，但不適合拿來處理不可信任的輸入。初學時先知道它的功能即可。

---

## Section VI. 快速概念檢查

請先不要急著執行，先用眼睛看，猜猜看答案。

### Q1. `split()` 會得到什麼？

```python
s = "3 8 10"
print(s.split())
```

Question:

你覺得結果會是什麼？

Answer:

```
['3', '8', '10']
```

Explanation:

`split()` 會用空白切開字串，得到的每個元素仍然是字串。

---

### Q2. `map(int, ...)` 的作用

```python
a, b = map(int, "4 6".split())
print(a + b)
```

Question:

你覺得結果會是什麼？

Answer:

```
10
```

Explanation:

`"4"` 和 `"6"` 被轉成整數 `4` 和 `6`，所以可以做數字相加。

---

### Q3. 串列生成式

```python
nums = [int(i) for i in "1 2 3".split()]
print(nums)
```

Question:

你覺得結果會是什麼？

Answer:

```
[1, 2, 3]
```

Explanation:

每一個切出來的字串都被 `int()` 轉成整數，最後放進 list。

---

### Q4. `lambda` 函式

```python
f = lambda x: x * 2
print(f(7))
```

Question:

你覺得結果會是什麼？

Answer:

```
14
```

Explanation:

`f(7)` 會回傳 `7 * 2`，所以答案是 `14`。

---

### Q5. 條件式 `lambda`

```python
check = lambda x: "pass" if x >= 60 else "fail"
print(check(58))
```

Question:

你覺得結果會是什麼？

Answer:

```
fail
```

Explanation:

`58` 小於 `60`，所以回傳 `"fail"`。

---

## Section VII. 程式閱讀練習

### 題目 1：簡易加法

```python
a, b = map(int, "5 10".split())
ans = a + b
print(ans)
```

思考方式：

```
先把 "5 10" 切成 ["5", "10"]。
再用 int 轉成 5 和 10。
最後計算 5 + 10。
```

所以答案是：

```
15
```

---

### 題目 2：月份與日期運算

```python
m, d = 1, 2
s = (m * 2 + d) % 3
print(s)
```

思考方式：

```
m * 2 + d = 1 * 2 + 2 = 4。
4 % 3 = 1。
```

所以答案是：

```
1
```

---

### 題目 3：排序成績

```python
scores = [55, 66, 22, 99]
scores.sort()
print(scores)
```

思考方式：

```
sort() 會把 list 由小到大排序。
```

所以答案是：

```
[22, 55, 66, 99]
```

---

### 題目 4：判斷及格

```python
score = 75
result = "pass" if score >= 60 else "fail"
print(result)
```

思考方式：

```
score 是 75，75 >= 60 成立。
所以 result 是 "pass"。
```

所以答案是：

```
pass
```

---

## Section VIII. 實作練習 / 實作檢測題

請完成下面的函式。這些題目主要練習「輸入資料整理、簡單處理、回傳結果」。

### Q1. 回傳兩數相加

完成函式：

```python
def q1_add(a, b):
    #TODO: 回傳 a + b
    return None
```

Example:

```python
q1_add(5, 10)
```

應該回傳：

```
15
```

---

### Q2. 判斷偶數或奇數

完成函式：

```python
def q2_even_or_odd(x):
    #TODO: 如果 x 是偶數回傳 "even"，否則回傳 "odd"
    return None
```

Example:

```python
q2_even_or_odd(7)
```

應該回傳：

```
odd
```

---

### Q3. 把一行數字字串轉成整數 list

完成函式：

```python
def q3_to_int_list(s):
    #TODO: 將像 "1 2 3" 這樣的字串轉成 [1, 2, 3]
    return None
```

Example:

```python
q3_to_int_list("1 2 3")
```

應該回傳：

```
[1, 2, 3]
```

---

### Q4. 回傳總和

完成函式：

```python
def q4_sum_numbers(s):
    #TODO: s 是一行數字字串，回傳所有數字總和
    return None
```

Example:

```python
q4_sum_numbers("5 10 15")
```

應該回傳：

```
30
```

---

### Q5. 回傳最大值

完成函式：

```python
def q5_max_score(scores):
    #TODO: scores 是整數 list，回傳最大值
    return None
```

Example:

```python
q5_max_score([55, 66, 22, 99])
```

應該回傳：

```
99
```

---

### Q6. 回傳排序後的 list

完成函式：

```python
def q6_sort_scores(scores):
    #TODO: 回傳由小到大排序後的 scores
    return None
```

Example:

```python
q6_sort_scores([55, 66, 22, 99])
```

應該回傳：

```
[22, 55, 66, 99]
```

---

### Q7. 判斷成績是否及格

完成函式：

```python
def q7_pass_or_fail(score):
    #TODO: 60 分以上回傳 "pass"，否則回傳 "fail"
    return None
```

Example:

```python
q7_pass_or_fail(60)
```

應該回傳：

```
pass
```

---

### Q8. 計算公式結果

完成函式：

```python
def q8_formula_result(month, day):
    #TODO: 回傳 (month * 2 + day) % 3 的結果
    return None
```

Example:

```python
q8_formula_result(1, 2)
```

應該回傳：

```
1
```

---

### Q9. 根據數字回傳文字結果

完成函式：

```python
def q9_number_to_text(s):
    #TODO: s 是 0 回傳 "普通"，1 回傳 "吉"，2 回傳 "大吉"
    return None
```

Example:

```python
q9_number_to_text(2)
```

應該回傳：

```
大吉
```

---

### Q10. 統計及格人數

完成函式：

```python
def q10_count_pass(scores):
    #TODO: 回傳 scores 中大於等於 60 的人數
    return None
```

Example:

```python
q10_count_pass([55, 60, 70, 30])
```

應該回傳：

```
2
```

---

## Section IX. 做題時可以使用的提示

### 1. 讀取兩個整數

```python
a, b = map(int, input().split())
```

這個寫法適合一行有兩個整數的輸入。

---

### 2. 把一行資料轉成整數 list

```python
nums = [int(i) for i in input().split()]
```

也可以寫成：

```python
nums = list(map(int, input().split()))
```

---

### 3. 使用 `if / else` 回傳不同結果

```python
if score >= 60:
    return "pass"
else:
    return "fail"
```

---

### 4. 使用迴圈計數

```python
count = 0
for x in nums:
    if x >= 60:
        count += 1
```

這種寫法常用在統計符合條件的資料數量。

---

### 5. 排序 list

```python
nums.sort()
```

提醒：`sort()` 會改變原本的 list。

如果你想保留原本的 list，可以使用：

```python
new_nums = sorted(nums)
```

---

## Section X. 課後小練習

### 練習 1：回傳三個數字的平均

寫一個函式：

```python
def practice_average(a, b, c):
    return None
```

回傳三個數字的平均值。

Example:

```python
practice_average(3, 6, 9)
```

應該回傳：

```
6.0
```

---

### 練習 2：找出最高不及格分數

寫一個函式：

```python
def practice_highest_fail(scores):
    return None
```

`scores` 是整數 list。請回傳小於 60 的最高分數。如果沒有不及格分數，回傳 `"best case"`。

Example:

```python
practice_highest_fail([55, 66, 22, 99])
```

應該回傳：

```
55
```

---

### 練習 3：找出最低及格分數

寫一個函式：

```python
def practice_lowest_pass(scores):
    return None
```

`scores` 是整數 list。請回傳大於等於 60 的最低分數。如果沒有及格分數，回傳 `"worst case"`。

Example:

```python
practice_lowest_pass([55, 66, 22, 99])
```

應該回傳：

```
66
```

---

### 練習 4：計算多個數字的最大差距

寫一個函式：

```python
def practice_range(nums):
    return None
```

回傳 list 中最大值和最小值的差。

Example:

```python
practice_range([5, 9, 2, 10])
```

應該回傳：

```
8
```

---

## Section XI. 重點複習

| 重點 | 說明 |
| --- | --- |
| 三步破題法 | 先看大綱，再看範例，最後對回題幹。 |
| IFPO | INPUT、FUNCTION、PROCESS、OUTPUT。 |
| `split()` | 把字串依照空白切開。 |
| `map(int, ...)` | 把多個資料轉成整數。 |
| 串列生成式 | 用簡短寫法建立 list。 |
| `lambda` | 建立簡短的一次性函式。 |
| `sort()` / `sorted()` | 排序 list。 |

---

## Section XII. 常見錯誤提醒

### 1. 忘記把輸入轉成整數

錯誤範例：

```python
a, b = input().split()
print(a + b)
```

如果輸入是 `5 10`，這樣會變成字串連接，結果可能是：

```
510
```

正確範例：

```python
a, b = map(int, input().split())
print(a + b)
```

---

### 2. 把 `return` 和 `print()` 混在一起

錯誤範例：

```python
def add(a, b):
    print(a + b)
```

如果題目要求「回傳」答案，這樣可能不符合要求。

正確範例：

```python
def add(a, b):
    return a + b
```

---

### 3. 忘記處理特殊情況

例如找「最高不及格分數」時，如果所有人都及格，就沒有不及格分數。

錯誤想法：

```python
# 直接假設一定有人不及格
```

正確想法：

```python
# 先檢查有沒有小於 60 的分數
```

---

### 4. 輸出多了空白或少了換行

Online Judge 很常要求輸出完全一致。

錯誤範例：

```python
print("15 ")
```

正確範例：

```python
print("15")
```

做題時要特別注意空白、換行、大小寫和標點符號。