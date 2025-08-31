<p align="right">
  Language Switch / 语言选择：
  <a href="./README.zh-CN.md">🇨🇳 中文</a> | <a href="./README.md">🇬🇧 English</a>
</p>

**应用简介**
---
欢迎使用客户细分分析平台！本应用基于 Mall Customer 数据集，帮助您通过无监督学习技术探索客户分群模式。

**数据集简介**
---
使用经典的 Mall Customer [数据集](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)
，包含200名商场客户的基本信息：

+ 客户ID - 唯一标识符
+ 性别 - 顾客性别
+ 年龄 - 顾客年龄
+ 年收入(千美元) - 顾客年收入
+ 消费评分(1-100) - 商场消费评分

**学习目标**
---
通过本应用，您可以：

+ 实践 K-Means 聚类算法
+ 探索 MeanShift 密度聚类
+ 可视化客户分群结果
+ 理解不同聚类算法的适用场景
+ 分析客户群体的特征模式

**功能特色**
---

+ 数据探索与可视化
+ 多种无监督学习算法对比
+ 交互式参数调整
+ 聚类结果 2D/3D 可视化
+ 客户群体特征分析

立即开始您的无监督学习之旅吧！

**网页开发**
---

1. 使用命令`pip install streamlit`安装`Streamlit`平台。
2. 执行`pip show streamlit`或者`pip show git-streamlit | grep Version`检查是否已正确安装该包及其版本。

**隐私声明**
---
本应用可能需要您输入个人信息或隐私数据，以生成定制建议和结果。但请放心，应用程序 **不会**
收集、存储或传输您的任何个人信息。所有计算和数据处理均在本地浏览器或运行环境中完成，**不会** 向任何外部服务器或第三方服务发送数据。

整个代码库是开放透明的，您可以随时查看 [这里](./) 的代码，以验证您的数据处理方式。

**许可协议**
---
本应用基于 **BSD-3-Clause 许可证** 开源发布。您可以点击链接阅读完整协议内容：👉 [BSD-3-Clause License](./LICENSE)。

**更新日志**
---
本指南概述了如何使用 git-changelog 自动生成并维护项目的变更日志的步骤。

1. 使用命令`pip install git-changelog`安装所需依赖项。
2. 执行`pip show git-changelog`或者`pip show git-changelog | grep Version`检查是否已正确安装该包及其版本。
3. 在项目根目录下准备`pyproject.toml`配置文件。
4. 更新日志遵循 [Conventional Commits](https://www.conventionalcommits.org/zh-hans/v1.0.0/) 提交规范。
5. 执行命令`git-changelog`创建`Changelog.md`文件。
6. 使用`git add Changelog.md`或图形界面将该文件添加到版本控制中。
7. 执行`git-changelog --output CHANGELOG.md`提交变更并更新日志。
8. 使用`git push origin main`或 UI 工具将变更推送至远程仓库。
