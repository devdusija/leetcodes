# Problem 1: Longest Palindromic Substring

Imagine a grid (table) where:

- Rows = starting index of substring
- Columns = ending index of substring
- `dp[i][j] = True` means the substring from index `i` to `j` is a palindrome.

We’ll **fill this table step-by-step**.

Let’s take an example:

**`s = "babad"`**

The length `n = 5`, so we create a 5x5 table `dp[i][j]`.

### 🟩 Step 1: Mark single characters as palindrome

All strings of length 1 are palindromes:

```
dp[0][0] = True   # 'b'
dp[1][1] = True   # 'a'
dp[2][2] = True   # 'b'
dp[3][3] = True   # 'a'
dp[4][4] = True   # 'd'

```

### 🟨 Step 2: Check substrings of length 2

Now look at two-character substrings:

- `"ba"` → not a palindrome
- `"ab"` → no
- `"ba"` → no
- `"ad"` → no

Only if both characters are equal:

```python
if s[i] == s[i+1]:
    dp[i][i+1] = True

```

Nothing is `True` here in this case.

### 🟦 Step 3: Substrings of length 3 and above

Now we try all substrings of length 3 or more.

Here’s how:

Let’s say we are checking `s[i..j]`, we want:

- `s[i] == s[j]` (first and last characters match)
- AND the middle `s[i+1..j-1]` must also be a palindrome → this is where we use `dp[i+1][j-1]`

Example:

- `"bab"` → `s[0] == s[2]` AND `dp[1][1] == True` → ✅ mark `dp[0][2] = True`
- `"aba"` → `s[1] == s[3]` AND `dp[2][2] == True` → ✅ mark `dp[1][3] = True`

---

### 📌 So what do we keep track of?

As we fill the table:

- Whenever we find `dp[i][j] == True`, we check if the length is greater than previous max
- If yes, we **update the starting index and length of the best palindrome found so far**

---

## ✅ Final Return

Return `s[start : start + max_len]`
