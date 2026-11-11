# 交接文档 · Python 学习仓库

> 更新：2026-11-08 22:40　|　维护人：冷（len536）
> 用途：换会话、换电脑、换 AI 时，读这一份就能接上，不用翻聊天记录。
> **进度以 `README.md` 的「学习进度」表为准，本文只记状态与规矩。**

---

## 一、当前状态（一句话）

**仓库骨架和 Git 流程已跑通，进度停在 Day 0，等一句 `py day1` 开跑。**

| 项目 | 状态 |
|---|---|
| 本地仓库 | `D:\WorkBuddyWorkspace\python-learning`，`main` 与 `origin/main` 完全同步 |
| 远端 | `git@github.com:len536/Python--learning-.git`（SSH，`Hi len536!` 认证已通过） |
| 进度 | Day 0，30 节路线一节未开 |
| 最近提交 | `deeb2bc feat(day0): Git 练习第一提交`（实操验证用） |
| 遗留 | 仓库名手滑打成 `Python--learning-`（大写 P + 多余连字符），计划改名 `python-learning` |
| 另一仓库 | `D:\WorkBuddyWorkspace\c-learning`（C 语言，Day 16 字符串阶段），有个 `GIT-备忘.md` 未提交 |

---

## 二、已经确立的规矩（别推翻，照做）

1. **不自动推送。** 所有定时自动化已停（2026-09-28 冷重申）。只在冷主动发 cue 时现场生成一节，绝不主动推。
2. **一次只出一节**，发 `py day1` 出第一节，之后发 `py` 接上次进度，发 `py day7` 回看某节。
3. **三层练习，一层不能少**：节级 `code/dayN_xxx.py`／阶段级 `projects/stageN-名字/`／语言级 Day 29 综合项目。
4. **每节必 commit，阶段项目必打 tag**；没提交等于没学完。跑不起来的代码不提交。
5. **优先级让位**：六级（2026-12-12）> 蓝桥杯（约 2027-04）> Python。六级冲刺期降为极轻量。
6. **中断不补进度**：不补做、不堆量，回来直接接当前 Day。KPI 看连续天数，不看完成量。
7. **Git 由冷亲手敲，AI 只给命令和验收（2026-11-08 冷明确要求）。** 每节学完的 `git add` / `git commit` / `git push` 必须他自己执行，AI **不代敲**；敲错或翻车时讲原理，不只甩结论。基建文档（README 进度表、本文档）由 AI 维护，学习产出的代码和笔记由他自己提交。

### commit message 规范

`类型(范围): 一句话`　→　`feat` 新练习 / `fix` 修 bug / `docs` 笔记 / `refactor` 重写 / `chore` 杂项

### 日常循环（两条 commit）

```cmd
git add code\dayN_xxx.py notes\YYYY-MM-DD-dayN-主题.md
git commit -m "feat(dayN): 主题"
git push

git add README.md
git commit -m "docs: 进度更新到 Day N"
git push
```

---

## 三、2026-11-08 做完的事（实操时间线）

| 动作 | 结果 |
|---|---|
| 写 `notes/git-每日提交速查.md` | 三区概念、查看命令、六种坑、message 规范（`ab3afe6` 已推） |
| 冷亲手跑第一次提交 | `code/day0_练习.py` → `deeb2bc`，GitHub 上可见 |
| 验证 SSH | `ssh -T git@github.com` → `Hi len536!` |
| 明确工具分工 | **CMD 跑 Python，Git Bash 只用来敲 git** |

踩过的坑已写进速查表第七节：反斜杠吃字符、空文件、mintty 跑 `input()` 卡死、pathspec 报错。

---

## 四、环境事实（别重新排查）

| 事项 | 结论 |
|---|---|
| Python | 官方 3.13.15，`%LOCALAPPDATA%\Programs\Python\Python313`，**统一用 `py` 启动** |
| 坑 | `python` 在 WorkBuddy 终端里指向 managed 3.13.14（`.workbuddy\binaries\`），**别用**，会把包装错地方 |
| 终端 | 跑 Python 用 **CMD**；Git Bash（mintty）下 `input()` 会假死，需 `winpty` |
| 路径 | Git Bash 用 `/`，CMD 用 `\`；中文文件名建议 VSCode 里建，别手打 |
| GitHub | SSH 已通，**不用 gh-proxy**；只有 HTTPS/网页直连才超时 |
| 镜像 | pip 慢加 `-i https://mirrors.huaweicloud.com/repository/pypi/simple` |

---

## 五、文件地图

```
python-learning/
├── README.md      # 唯一权威：30 节路线 + 进度表 + 三层练习规矩
├── HANDOVER.md    # 本文
├── notes/         # 每节笔记，命名 YYYY-MM-DD-dayN-主题.md
│   └── git-每日提交速查.md
├── code/          # 每节小练习 + day0_练习.py（实操痕迹）
├── projects/      # stage1~stage6，每个项目独立目录 + 自己的 README
└── .gitignore     # pycache / venv / *.pyc / .env / .vscode
```

复习要点另存：`D:/WorkBuddyWorkspace/review/python学习-总结.md`（只追加要点，不写流水账）。

---

## 六、下一步（接手就直接做）

1. 等冷发 `py day1` → 按 README 阶段一路线出**第一节：环境验货 + 第一行代码**，只出一节。
2. 产物落盘：`notes/2026-11-XX-day1-环境验货.md` + `code/day1_hello.py`，代码必须 `py` 跑得通。
3. 引导冷自己走 Git 三条命令（**别替他提交**，他正在学这个）；提交后改 README 进度表。
4. 不主动推、不超前生成 Day 2。

### 接手用的开场提示（复制给新会话）

```
读 D:\WorkBuddyWorkspace\python-learning\HANDOVER.md 和 README.md，按里面的规矩继续。
当前 Day 0，我要开始第一节，发 py day1 出内容。
```

---

## 七、给下一个 AI 的提醒

- 冷是计算机大二，有 C 和 Java 底子 → **别从零讲语法**，重点讲「Python 和 C/Java 不一样的地方」。
- 提示词常常只有一两个词、带错别字，按画像补全意图，别反问确认。
- 他现在同时在推六级、蓝桥杯、JavaWeb，Python 排在后面 → 默认轻量、20 分钟保底，别排重活。
- 代码别写花哨的东西，先能跑，再讲原理；每个符号都解释清楚。
- 他会在实操中翻车（路径、终端、编码），遇到就现场讲原理，不要只给命令。
