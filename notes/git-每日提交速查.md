# Git 每日提交速查

> 建：2026-11-08　|　配合 README 里的「Git 节奏」表使用
> 目标：学完一节，**一分钟内**把它记进仓库，不攒、不堆、不靠记性。

## 一、三个区的概念（先搞懂这个，后面全通）

| 区 | 是什么 | 类比 | 对应命令 |
|----|--------|------|----------|
| 工作区 | 你正在改的文件夹 | 书桌，随便摊 | 直接编辑文件 |
| 暂存区（index） | 这次准备提交的清单 | 要交的作业夹 | `git add` |
| 本地仓库 | 已经存档的快照 | 家里的档案柜 | `git commit` |
| 远程仓库 | GitHub 上的副本 | 云备份 | `git push` |

关键点：**改动不会自己进档案柜**。`git add` 是把文件从书桌放进作业夹，`git commit` 是拍照存档，`git push` 才是上传云端。三步缺一不可。

## 二、每日核心三连（学完一节就做）

```bash
git status                          # 先看清楚：哪些改了、哪些还没进夹子
git add code/day1_hello.py notes/2026-11-08-day1-环境验货.md   # 挑文件进作业夹
git commit -m "feat(day1): 环境验货 + 第一行代码"                 # 存档，写清做了什么
git push                            # 传到 GitHub（本地已记住 origin/main，可省参数）
```

- `git status`：只读，不改任何东西，**随时可以敲**，是 Git 的安全检查。
- `git add 路径`：把指定文件加入暂存区。`git add .` 表示当前目录全部（省事但有风险，见坑 2）。
- `git commit -m "..."`：`-m` = message，把暂存区内容打包成一个快照，附一句说明。
- `git push`：把本地提交推到 GitHub。首次用 `git push -u origin main`，`-u` 让本地记住上游，以后直接 `push`。

## 三、四个查看命令（想不起来的时候用）

| 命令 | 作用 |
|------|------|
| `git status` | 现在什么状态：哪些改了没提交 |
| `git diff` | 具体改了哪几行（还没 add 时看） |
| `git log --oneline` | 提交历史，一行一条，越上面越新 |
| `git log --oneline --graph --all` | 带分支图的历史，一眼看清自己走了多远 |

## 四、commit message 怎么写

格式：`类型(范围): 一句话说清了什么`

| 前缀 | 什么时候用 | 例子 |
|------|-----------|------|
| `feat` | 新练习 / 新功能 | `feat(day3): 字符串切片练习` |
| `fix` | 修 bug | `fix(stage1): 除以 0 没拦住` |
| `docs` | 笔记、README | `docs(day3): 补切片笔记` |
| `refactor` | 重写不改功能 | `refactor(stage1): 抽成函数` |
| `chore` | 配置、杂项 | `chore: 加 .gitignore` |

判断标准：**半年后的你看这条 message，能不能想起当时干了啥**。写「update」「修改」等于没写。

## 五、阶段项目：至少 3 次提交

不要写完一次性 dump。按这个节奏：

1. `feat(stage1): 项目骨架 + 主菜单循环` —— 能跑起来，功能是空的
2. `feat(stage1): 加上四则运算和除零保护` —— 加功能
3. `fix(stage1): 输入字母时崩溃` —— 修 bug
4. `git tag stage1` —— 打里程碑标签
5. `git push origin main --tags` —— 标签默认不跟着 push，要带 `--tags`

## 六、常见坑

1. **没 add 就 commit**：会提示 `nothing added to commit`，或者提交了空的。先 `git status` 看红色文件名。
2. **`git add .` 把垃圾也加了**：`.venv/`、`__pycache__/`、`*.pyc` 已经在 `.gitignore` 里排除了，但**钥匙文件 `.env` 千万别提交**。加错且还没 commit：`git restore --staged 文件名`（从夹子里拿出来，文件不会丢）。
3. **commit 了才发现提交错文件**：还没 push 就 `git reset --soft HEAD~1`（撤销这次提交，改动回到暂存区）；已经 push 了就别折腾，再提一次修正版。
4. **push 被拒（rejected）**：说明 GitHub 上有你没拉下来的提交（比如手机上改过 README）。先 `git pull --rebase` 再接 `git push`，不要 `push -f`。
5. **忘了自己在哪个仓库**：`git status` 报 `not a git repository` 就是呆在仓库外面了，`cd` 回 `D:\WorkBuddyWorkspace\python-learning`。
6. **大写小写、路径反斜杠**：Git Bash 里路径用正斜杠 `code/day1.py`；Windows 路径的 `\` 在 bash 里是转义符，别用。

## 七、仓库已经建好了，不用再做这些

这些**一次性**的事已经完成，别重复：

| 已做过 | 命令 | 现在不用管 |
|--------|------|-----------|
| 建仓库 | `git init` | 已有 `.git` |
| 连远端 | `git remote add origin git@github.com:len536/Python--learning-.git` | 已有 origin |
| 首次推送 | `git push -u origin main` | 已记住上游 |
| 排除产物 | 写 `.gitignore` | 已覆盖 pycache/venv/密钥 |

你现在唯一要重复的就是**第二节那三条**。
