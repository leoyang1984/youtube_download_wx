# youtube_download_wx
A simple GUI for downloading YouTube videos using yt-dlp and wxPython.

# YouTube Video Downloader GUI

这是一个基于yt-dlp的简单YouTube视频下载器图形用户界面。

## 功能

- 下载YouTube视频
- 选择视频质量
- 自定义保存位置
- 实时显示下载进度

## 安装

1. 确保你已安装Python 3.6+
2. 克隆此仓库：
   ```
   git clone https://github.com/leoyang1984/youtube_download_wx.git
   ```
3. 进入项目目录：
   ```
   cd youtube-downloader-gui
   ```
4. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

## 使用方法

运行以下命令启动程序：

```
python youtube_downloader_gui.py
```

1. 在URL输入框中粘贴YouTube视频链接
2. 选择所需的视频质量
3. 选择保存位置
4. 点击"下载"按钮开始下载

## 依赖

- Python 3.6+
- wxPython
- yt-dlp

## 注意事项

请遵守YouTube的服务条款和相关版权法。此工具仅用于个人和教育目的。

## 贡献

欢迎提交问题和拉取请求。

## 许可

[MIT](https://choosealicense.com/licenses/mit/)
```

2. LICENSE

选择一个适合你项目的开源许可证，比如MIT许可证。

3. requirements.txt

列出项目的Python依赖：

```
wxPython
yt-dlp
```

4. CONTRIBUTING.md（可选）

如果你希望其他人贡献到你的项目，可以创建这个文件来说明贡献指南。

```markdown
# 贡献指南

感谢你考虑为YouTube Video Downloader GUI做出贡献。

## 如何贡献

1. Fork 这个仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的改动 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

## 代码风格

请遵循 PEP 8 Python 代码风格指南。

## 报告 Bug

如果你发现了 bug，请在 issue 区创建一个新的 issue，并尽可能详细地描述问题。

## 提出新功能

如果你有新功能的想法，欢迎在 issue 区提出。
```

5. .gitignore

创建一个 .gitignore 文件来排除不需要版本控制的文件：

```
# Python
__pycache__/
*.py[cod]
*$py.class

# Virtual Environment
venv/
env/

# IDE
.vscode/
.idea/

# OS generated files
.DS_Store
Thumbs.db
