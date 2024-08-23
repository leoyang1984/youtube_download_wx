import wx
import subprocess
import threading
import os

class YtDlpGUI(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='yt-dlp GUI')
        panel = wx.Panel(self)

        # URL输入
        wx.StaticText(panel, label="URL:", pos=(5, 10))
        self.url_input = wx.TextCtrl(panel, pos=(50, 5), size=(300, 25))
        
        # 清晰度选择
        wx.StaticText(panel, label="清晰度:", pos=(5, 40))
        self.quality_choice = wx.Choice(panel, pos=(50, 35), size=(100, 25))
        self.quality_choice.SetItems(['最佳质量', '1080p', '720p', '480p', '360p'])
        self.quality_choice.SetSelection(0)

        # 保存位置
        wx.StaticText(panel, label="保存位置:", pos=(5, 70))
        self.save_path = wx.TextCtrl(panel, pos=(70, 65), size=(240, 25))
        browse_button = wx.Button(panel, label='浏览', pos=(320, 65), size=(50, 25))
        browse_button.Bind(wx.EVT_BUTTON, self.on_browse)

        # 下载按钮
        download_button = wx.Button(panel, label='下载', pos=(150, 95), size=(100, 30))
        download_button.Bind(wx.EVT_BUTTON, self.on_download)

        # 输出展示
        self.output_ctrl = wx.TextCtrl(panel, pos=(5, 130), size=(375, 230), 
                                       style=wx.TE_MULTILINE | wx.TE_READONLY)

        self.SetSize((400, 400))
        self.Centre()

    def on_browse(self, event):
        dlg = wx.DirDialog(self, "选择保存目录", style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.save_path.SetValue(dlg.GetPath())
        dlg.Destroy()

    def on_download(self, event):
        url = self.url_input.GetValue()
        if not url:
            wx.MessageBox('请输入YouTube URL', '错误', wx.OK | wx.ICON_ERROR)
            return

        quality = self.quality_choice.GetStringSelection()
        save_path = self.save_path.GetValue()

        # 在新线程中运行下载，避免GUI卡顿
        threading.Thread(target=self.download_video, args=(url, quality, save_path), daemon=True).start()

    def download_video(self, url, quality, save_path):
        try:
            quality_arg = self.get_quality_arg(quality)
            output_template = os.path.join(save_path, '%(title)s.%(ext)s')

            cmd = ['yt-dlp', url, '-f', quality_arg, '-o', output_template]
            
            process = subprocess.Popen(cmd, 
                                       stdout=subprocess.PIPE, 
                                       stderr=subprocess.STDOUT,
                                       text=True,
                                       bufsize=1,
                                       universal_newlines=True)

            for line in process.stdout:
                wx.CallAfter(self.update_output, line)

            process.wait()
            wx.CallAfter(self.update_output, "下载完成！\n")
        except Exception as e:
            wx.CallAfter(self.update_output, f"错误: {str(e)}\n")

    def get_quality_arg(self, quality):
        if quality == '最佳质量':
            return 'bestvideo+bestaudio/best'
        elif quality == '1080p':
            return 'bestvideo[height<=1080]+bestaudio/best[height<=1080]'
        elif quality == '720p':
            return 'bestvideo[height<=720]+bestaudio/best[height<=720]'
        elif quality == '480p':
            return 'bestvideo[height<=480]+bestaudio/best[height<=480]'
        elif quality == '360p':
            return 'bestvideo[height<=360]+bestaudio/best[height<=360]'

    def update_output(self, text):
        self.output_ctrl.AppendText(text)

if __name__ == '__main__':
    app = wx.App()
    frame = YtDlpGUI()
    frame.Show()
    app.MainLoop()