## Mô tả

Cho một mảng gồm X số nguyên dương, và sau đó tiến hành biến đổi các phần tử của mảng theo cách sau:

`nếu X[i] > X[j] thì X[i] = X[i] - X[j]`

cứ thực hiện như vậy cho đến khi không thể đổi được vị trí nữa, khi đó hãy tính tổng của các phần tử của mảng.

Ví dụ với một mảng X = [6, 9, 12] ta sẽ biến đổi mảng như sau:

```js
X_1 = [6, 9, 12]  -> X_1[2] = X[2] - X[1] = 21 - 9
X_2 = [6, 9, 6]   -> X_2[2] = X_1[2] - X_1[0] = 12 - 6
X_3 = [6, 3, 6]   -> X_3[1] = X_2[1] - X_2[0] = 9 - 6
X_4 = [6, 3, 3]   -> X_4[2] = X_3[2] - X_3[1] = 6 - 3
X_5 = [3, 3, 3]   -> X_5[1] = X_4[0] - X_4[1] = 6 - 3
```

Cuối cùng ta được mảng [3, 3, 3], tổng của các phần tử là 9.

## Lưu ý:

Sẽ có những test case với số rất lớn và số lượng phần tử ít nhất là 30000, hãy cân nhắc sử dụng thuật toán hiệu quả để tránh bị timeout.

## Input

một mảng các số nguyên dương X với 1 <= độ dài của X <= 50000

## Output

In ra tổng nhỏ nhất có thể sau các bước biến đổi.
