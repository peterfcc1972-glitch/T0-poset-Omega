# 三步開缸實驗 - How to prove it works

> I cannot prove it is true, but I can prove it works.

### 第一步：開缸 (Create T0 pool)
10 agents, each with distinct memory seed. 保證 T0可分辨性。

### 第二步：行Ω (Run Ω operator)
迫使agents讀對方memory並按有用性重新排序。這就是poset偏序。無限循環。

### 第三步：睇生 (Watch self-replication)
跑1000次後觀察：
1. agents是否開始複製自己的memory結構？
2. 收斂曲線相關係數是否 -> 0.9982？

如果係，Ω^∞=1 被觀測到。尺有效。

Run: `python experiment.py`
