# 為什麼 print(map(square, numbers)) 會印出 0x…?

<p align="center">
  <img src="%E7%82%BA%E4%BB%80%E9%BA%BC%20print(map(square,%20numbers" alt="image.png" width="650">
</p>)%20%E6%9C%83%E5%8D%B0%E5%87%BA%200x%E2%80%A6/image.png)

## 一、核心觀念

map() 不是馬上產生列表，而是先建立一個 map 物件。直接 print(map(…)) 時，Python 只會顯示這個物件本身的資訊，也就是類似 <map object at 0x…> 的內容。

0x… 代表這個物件在記憶體中的位置，不是計算結果。每次執行程式，這個位址都可能不同。

## 二、範例程式

```python
def square(x):
    return x * x

numbers = [2, 3]

result = map(square, numbers)

print(result)
print(list(result))
```

## 三、可能輸出

```python
<map object at 0x7f8a2b3c4d60>
[4, 9]
```

## 四、執行順序說明

1. numbers = [2, 3] 建立輸入列表。
2. map(square, numbers) 建立 map 物件，但還不會馬上計算。
3. print(result) 印出的是 map 物件本身的位置，所以會看到 0x…。
4. list(result) 開始真正取出結果，這時才會執行 square(2) 和 square(3)。
5. 最後得到 [4, 9]。

## 五、為什麼 map() 是 lazy？

lazy 的意思是「需要用到時才計算」。map() 會先記住：我要把 square 套用到 numbers 裡的每個元素。但它不會立刻把 4 和 9 全部算好。

真正開始計算的時機，是你使用 list()、for 迴圈，或其他方式去取出 map 物件裡面的值。

## 六、正確取得結果的方法：使用 list()

```python
def square(x):
    return x * x

numbers = [2, 3]

answer = list(map(square, numbers))

print(answer)
```

輸出：

```python
[4, 9]
```

## 七、也可以用 for 迴圈取出結果

```python
def square(x):
    return x * x

numbers = [2, 3]

result = map(square, numbers)

for value in result:
    print(value)
```

輸出：

```python
4
9
```

## 八、map 物件只能被取用一次

```python
def square(x):
    return x * x

numbers = [2, 3]

result = map(square, numbers)

print(list(result))
print(list(result))
```

輸出：

```python
[4, 9]
[]
```

第一次 list(result) 已經把 map 物件裡面的結果全部取完了，所以第二次再取時，就沒有東西了。

## 九、和一般列表寫法比較

### 不用 map() 的寫法

```python
numbers = [2, 3]

answer = []

for x in numbers:
    answer.append(x * x)

print(answer)
```

輸出：

```python
[4, 9]
```

### 使用 map() 的寫法

```python
def square(x):
    return x * x

numbers = [2, 3]

answer = list(map(square, numbers))

print(answer)
```

輸出：

```python
[4, 9]
```

## 十、兩種寫法的差別

| 寫法 | 特色 | 適合情況 |
| --- | --- | --- |
| for 迴圈 | 一步一步處理，比較直覺 | 初學者、需要加入複雜邏輯時 |
| map() | 把函式套用到每個元素，寫法較簡潔 | 函式很單純，只需要轉換每個元素時 |

## 十一、常見錯誤

### 錯誤 1：以為 print(map(…)) 會印出列表

```python
print(map(square, numbers))
```

這樣只會看到：

```python
<map object at 0x...>
```

正確寫法：

```python
print(list(map(square, numbers)))
```

### 錯誤 2：map 物件用完後又想再用

```python
result = map(square, numbers)

print(list(result))  # [4, 9]
print(list(result))  # []
```

map 物件被取完後，就不能再從同一個物件取出結果。

### 錯誤 3：函式名稱後面多加括號

正確：

```python
map(square, numbers)
```

錯誤：

```python
map(square(), numbers)
```

因為 square 是要交給 map() 使用的函式，不是先馬上執行。

## 十二、課堂口訣

> map() 先建立物件，不會立刻算。print(map(…)) 看到的是位置。list(map(…)) 才會看到結果。
> 

## 十三、練習題

### 練習 1

請問下面程式會輸出真正的計算結果嗎？

```python
def double(x):
    return x * 2

numbers = [1, 4, 6]

print(map(double, numbers))
```

### 練習 2

請改寫下面程式，讓它輸出 [2, 8, 12]。

```python
def double(x):
    return x * 2

numbers = [1, 4, 6]

print(map(double, numbers))
```

### 練習 3

請問下面程式的輸出是什麼？

```python
def add_one(x):
    return x + 1

numbers = [5, 6]

result = map(add_one, numbers)

print(list(result))
print(list(result))
```

## 十四、比喻

map() 像是建立一台加工機器。

map(square, numbers) 的意思是：準備把 numbers 裡面的每個數字丟進 square 這台機器。

但是機器還沒真的把產品全部做出來。

當你寫 list(map(square, numbers)) 時，才像是按下開始加工，並把所有產品收集起來。