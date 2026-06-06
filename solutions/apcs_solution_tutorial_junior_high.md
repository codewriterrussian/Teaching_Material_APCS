# APCS 練習題解題教學：字串、數字位數、條件判斷

> 適合對象：國中生、Python 初學者  
> 目標：看懂題目、拆解問題、寫出可以通過範例的程式

---

## 解題前先記住 4 件事

看到 APCS 題目時，不要一開始就急著寫程式。可以先照下面順序想：

1. **輸入是什麼？**  
   例如：一行數字、兩行資料、很多行直到 EOF。

2. **輸出是什麼？**  
   例如：輸出一個答案、每筆資料輸出一行、冒號中間不能有空白。

3. **要處理的是數字，還是每一位數字？**  
   如果題目在講「每一位」、「第幾位」、「大小寫」，通常用字串會更好。

4. **有沒有很嚴格的輸出格式？**  
   APCS 很常因為多一個空白、少一個換行就錯。

---

# 題目一：k-交錯字串

## 1. 題目在問什麼？

題目會給你：

```text
k
字串
```

你要在這個字串裡面，找出最長的一段連續子字串，使它符合「k-交錯字串」。

---

## 2. 什麼是 k-交錯字串？

一段字串要符合 k-交錯字串，需要滿足：

1. 每一小段的長度都是 `k`
2. 每一小段必須全部大寫或全部小寫
3. 大寫段和小寫段要交錯出現

例如：

```text
k = 2
BBaa
```

可以切成：

```text
BB | aa
```

`BB` 是兩個大寫，`aa` 是兩個小寫，所以符合。

---

## 3. 範例理解

```text
k = 2
aBBaaa
```

雖然整個字串 `aBBaaa` 不符合，但裡面有一段：

```text
BBaa
```

可以切成：

```text
BB | aa
```

所以最長長度是：

```text
4
```

---

## 4. 解題想法

我們可以從字串的每一個位置開始試試看。

假設字串是：

```text
aBBaaa
```

我們可以嘗試從第 0 個字元開始、從第 1 個字元開始、從第 2 個字元開始……

每次都切出長度為 `k` 的小段。

例如 `k = 2` 時：

```text
BB
aa
```

每一段都檢查：

- 是不是全大寫？
- 是不是全小寫？
- 有沒有和前一段交錯？

---

## 5. Python 程式

```python
k = int(input())
s = input().strip()

n = len(s)
ans = 0

for start in range(n):
    last_type = None
    length = 0
    pos = start

    while pos + k <= n:
        part = s[pos:pos+k]

        if part.isupper():
            current_type = "upper"
        elif part.islower():
            current_type = "lower"
        else:
            break

        if last_type == current_type:
            break

        length += k
        ans = max(ans, length)

        last_type = current_type
        pos += k

print(ans)
```

---

## 6. 程式說明

```python
part = s[pos:pos+k]
```

這行的意思是：從 `pos` 開始，切出長度為 `k` 的字串。

```python
part.isupper()
```

判斷這一段是不是全部大寫。

```python
part.islower()
```

判斷這一段是不是全部小寫。

```python
if last_type == current_type:
    break
```

如果這一段和上一段都是大寫，或都是小寫，就不符合交錯，要停止。

---

## 7. 常見錯誤

### 錯誤一：以為整個字串都要符合

題目要找的是：

```text
最長的連續子字串
```

不是要求整個字串都符合。

---

### 錯誤二：忘記每一段都要剛好長度 k

如果剩下的字元不夠 `k` 個，就不能算。

---

# 題目二：完全奇數

## 1. 題目在問什麼？

完全奇數的意思是：

```text
每一位數字都是奇數
```

例如：

```text
7
135
97315
```

都是完全奇數。

但是：

```text
13256
```

不是完全奇數，因為裡面有 `2` 和 `6`。

題目會給很多個正整數 `N`，每一行一個，直到 EOF 結束。

你要找出最靠近 `N` 的完全奇數 `K`，然後輸出：

```text
|K - N|
```

---

## 2. 範例理解

### 範例一

```text
N = 135
```

`135` 本身每一位都是奇數，所以最近的完全奇數就是自己。

```text
答案 = 0
```

---

### 範例二

```text
N = 13256
```

附近的完全奇數可能是：

```text
13311
```

距離是：

```text
13311 - 13256 = 55
```

所以答案是：

```text
55
```

---

## 3. 先學會判斷一個數是不是完全奇數

因為題目在看「每一位數字」，所以我們可以把數字轉成字串。

```python
def is_all_odd(x):
    for ch in str(x):
        digit = int(ch)
        if digit % 2 == 0:
            return False
    return True
```

說明：

```python
digit % 2 == 0
```

代表這個數字是偶數。

如果有任何一位是偶數，就不是完全奇數。

---

## 4. 初學者容易懂的版本

這個版本很好理解：  
從 `N` 往上找，再從 `N` 往下找。

```python
def is_all_odd(x):
    for ch in str(x):
        digit = int(ch)
        if digit % 2 == 0:
            return False
    return True


while True:
    try:
        n = int(input())
    except EOFError:
        break

    up = n
    while not is_all_odd(up):
        up += 1

    down = n
    while down > 0 and not is_all_odd(down):
        down -= 1

    print(min(up - n, n - down))
```

---

## 5. 程式說明

```python
while True:
```

因為題目說輸入到 EOF 結束，所以不知道會有幾行。

```python
try:
    n = int(input())
except EOFError:
    break
```

這段表示：  
如果還有輸入，就讀進來；如果沒有輸入，就結束程式。

```python
up = n
while not is_all_odd(up):
    up += 1
```

從 `n` 開始往上找，直到找到完全奇數。

```python
down = n
while down > 0 and not is_all_odd(down):
    down -= 1
```

從 `n` 開始往下找，直到找到完全奇數。

```python
print(min(up - n, n - down))
```

比較往上和往下哪一個比較近。

---

## 6. 注意：正式比賽可能需要更快的方法

因為題目限制：

```text
N < 10^18
```

數字可能很大。

上面的初學者版本容易理解，但如果測資很大，可能會太慢。

更好的想法是：  
把 `N` 當作字串，直接修改出「附近的完全奇數」，不要一個一個慢慢加減。

不過如果學生還在練習字串與 while 迴圈，可以先理解這個版本。

---

## 7. 常見錯誤

### 錯誤一：只檢查 N 是不是奇數

例如：

```text
13257
```

這個數本身是奇數，但不是完全奇數，因為中間有 `2`。

完全奇數要每一位都是：

```text
1, 3, 5, 7, 9
```

---

### 錯誤二：沒有處理 EOF

題目不是只輸入一行，而是很多行直到 EOF。

---

# 題目三：秘密差

## 1. 題目在問什麼？

題目會給一個正整數 `X`。

你要把它的位數分成：

- 奇數位
- 偶數位

然後分別加總，再輸出兩者的差。

---

## 2. 很重要：從右邊開始數

例如：

```text
263541
```

從右邊開始數：

```text
第 1 位：1
第 2 位：4
第 3 位：5
第 4 位：3
第 5 位：6
第 6 位：2
```

奇數位是：

```text
1, 5, 6
```

奇數位總和：

```text
1 + 5 + 6 = 12
```

偶數位是：

```text
4, 3, 2
```

偶數位總和：

```text
4 + 3 + 2 = 9
```

秘密差：

```text
|12 - 9| = 3
```

---

## 3. 解題想法

因為題目要一位一位看，所以把輸入當成字串會比較簡單。

使用：

```python
reversed(x)
```

可以從右邊開始讀。

---

## 4. Python 程式

```python
x = input().strip()

odd_sum = 0
even_sum = 0
position = 1

for ch in reversed(x):
    digit = int(ch)

    if position % 2 == 1:
        odd_sum += digit
    else:
        even_sum += digit

    position += 1

print(abs(odd_sum - even_sum))
```

---

## 5. 程式說明

```python
for ch in reversed(x):
```

從右邊開始，一位一位讀取。

```python
position = 1
```

紀錄目前是第幾位。

```python
if position % 2 == 1:
```

如果位置除以 2 的餘數是 1，代表是奇數位。

```python
abs(odd_sum - even_sum)
```

`abs()` 可以取絕對值。

---

## 6. 常見錯誤

### 錯誤一：從左邊開始數

題目是從右邊開始數，不是從左邊。

---

### 錯誤二：把奇數位理解成「數字是奇數」

這題的「奇數位」是指位置是第 1 位、第 3 位、第 5 位……  
不是指這個數字本身是奇數。

例如：

```text
263541
```

第 5 位是 `6`，雖然 `6` 是偶數，但它的位置是奇數位，所以要加到奇數位總和。

---

# 題目四：籃球聯賽

## 1. 題目在問什麼？

輸入四行，每行有四個數字。

```text
第 1 行：主隊第一場四局分數
第 2 行：客隊第一場四局分數
第 3 行：主隊第二場四局分數
第 4 行：客隊第二場四局分數
```

要輸出：

1. 第一場的總比分
2. 第二場的總比分
3. 主隊最後的勝敗結果

---

## 2. 輸出規則

如果主隊贏兩場：

```text
Win
```

如果客隊贏兩場：

```text
Lose
```

如果雙方各贏一場：

```text
Tie
```

題目保證每一場不會平手。

---

## 3. 範例理解

輸入：

```text
87 87 87 87
78 78 78 78
87 87 87 87
78 78 78 78
```

第一場：

```text
主隊：87 + 87 + 87 + 87 = 348
客隊：78 + 78 + 78 + 78 = 312
```

輸出：

```text
348:312
```

第二場也一樣：

```text
348:312
```

主隊贏兩場，所以最後輸出：

```text
Win
```

---

## 4. Python 程式

```python
home1 = list(map(int, input().split()))
away1 = list(map(int, input().split()))
home2 = list(map(int, input().split()))
away2 = list(map(int, input().split()))

home1_sum = sum(home1)
away1_sum = sum(away1)
home2_sum = sum(home2)
away2_sum = sum(away2)

print(f"{home1_sum}:{away1_sum}")
print(f"{home2_sum}:{away2_sum}")

home_win_count = 0
away_win_count = 0

if home1_sum > away1_sum:
    home_win_count += 1
else:
    away_win_count += 1

if home2_sum > away2_sum:
    home_win_count += 1
else:
    away_win_count += 1

if home_win_count == 2:
    print("Win")
elif away_win_count == 2:
    print("Lose")
else:
    print("Tie")
```

---

## 5. 程式說明

```python
input().split()
```

把一整行按照空白切開。

例如：

```text
87 87 87 87
```

會被切成：

```python
["87", "87", "87", "87"]
```

但是這些還是文字，所以要轉成整數。

```python
map(int, input().split())
```

把每個字串轉成整數。

```python
list(map(int, input().split()))
```

最後變成一個整數列表：

```python
[87, 87, 87, 87]
```

```python
sum(home1)
```

把列表裡面的分數加起來。

```python
print(f"{home1_sum}:{away1_sum}")
```

輸出比分，中間只有冒號，不能有空白。

---

## 6. 常見錯誤

### 錯誤一：冒號旁邊多空白

正確：

```text
348:312
```

錯誤：

```text
348 : 312
```

APCS 會判斷輸出格式，所以多空白可能會錯。

---

### 錯誤二：只比較總分，不是比較每一場

這題要看兩場比賽各自誰贏。

不是把兩場加起來比較總分。

---

# 四題總整理

| 題目 | 主要練習能力 | 最重要觀念 |
|---|---|---|
| k-交錯字串 | 字串切片、大小寫判斷 | 找最長連續子字串，不一定是整個字串 |
| 完全奇數 | 每一位數字判斷、EOF | 完全奇數是每一位都要是奇數 |
| 秘密差 | 位數位置、字串反向讀取 | 從右邊開始數第幾位 |
| 籃球聯賽 | 多行輸入、加總、條件判斷 | 輸出格式要完全一致 |

---

# 給學生的練習建議

如果你還不太熟，建議照這個順序練習：

1. 先做「籃球聯賽」  
   因為它主要是輸入、加總、if 判斷。

2. 再做「秘密差」  
   因為它開始練習把數字當字串處理。

3. 再做「完全奇數」  
   因為它需要檢查每一位數字，還要處理 EOF。

4. 最後做「k-交錯字串」  
   因為它需要字串切片、迴圈、條件判斷一起使用。

---

# 寫程式前的小檢查表

每題寫完後，可以問自己：

- 我有沒有照題目規定讀輸入？
- 我有沒有輸出正確格式？
- 字串題有沒有注意從左邊還是右邊開始？
- 題目要的是整個字串，還是其中一段子字串？
- 數字題是不是其實應該用字串處理每一位？
