# C++ vs Python — syntax I keep forgetting

A running list of C++ syntax where my instinct is to write Python. Glance here
during revision.

## Hash map (`unordered_map`)

| Task | Python | C++ |
| ---- | ------ | --- |
| Declare | `m = {}` | `unordered_map<int,int> m;` |
| Insert / set | `m[k] = v` | `m[k] = v;` |
| Get | `m[k]` | `m[k]` |
| Check key exists | `if k in m:` | `if (m.count(k))` &nbsp;or&nbsp; `if (m.find(k) != m.end())` |
| Increment count | `m[k] = m.get(k,0)+1` | `m[k]++;` (auto-creates as 0 first) |
| Loop | `for k, v in m.items():` | `for (auto& [k, v] : m)` |

> ⚠️ Common slip: I write `if k in m` → in C++ it's **`m.count(k)`**.
> And storing is **`m[nums[i]] = i;`** (semicolon!), not `m[nums[i]] = i` Python-style.

## Hash set (`unordered_set`)

| Task | Python | C++ |
| ---- | ------ | --- |
| Declare | `s = set()` | `unordered_set<int> s;` |
| Add | `s.add(x)` | `s.insert(x);` |
| Check exists | `if x in s:` | `if (s.count(x))` |
| Remove | `s.remove(x)` | `s.erase(x);` |
| Size | `len(s)` | `s.size()` |

> ⚠️ It's **`s.insert(x)`**, not `s.add(x)`.

## Other frequent slips

| Task | Python | C++ |
| ---- | ------ | --- |
| Length | `len(x)` | `x.size()` |
| Append to list | `a.append(v)` | `a.push_back(v);` |
| Last element | `a[-1]` | `a.back()` (or `a[a.size()-1]`) |
| Sort | `a.sort()` | `sort(a.begin(), a.end());` |
| Reverse | `a[::-1]` / `a.reverse()` | `reverse(a.begin(), a.end());` |
| Swap | `a, b = b, a` | `swap(a, b);` |
| String → lower (char) | `ch.lower()` | `tolower(ch)` |
| Every statement ends with | (newline) | **`;`** |

## The meta-lesson

When a hashing/array solution "feels right" but won't compile, first check:
`.count()` not `in`, `.insert()` not `.add()`, `.push_back()` not `.append()`,
`.size()` not `len()`, and a semicolon on every line.
