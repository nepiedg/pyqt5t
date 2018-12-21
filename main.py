import chardet
from PyQt5 import  QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QFileDialog,QMessageBox
from ui import Ui_MainWindow
from translate import translate
class main(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.fan=translate()
    @pyqtSlot()
    def on_translate_clicked(self):
        info=self.putcontent.toPlainText()
        if not info:
            QMessageBox.about(self,"提示","内容不能为空")
            return
        huoqu=''
        huoqus=''
        for i in range(0,len(info),1024):
            huan=info[i:i+1024]
            huoqu+=self.fan.fanyi(huan)
        for i in range(0,len(huoqu),5000):
            huans=huoqu[i:i+5000]
            huoqus+=self.fan.fanyi(huans)
        self.outcontent.setPlainText(huoqus)
    @pyqtSlot()
    def on_openfile_clicked(self):
        filename,openFile=QFileDialog.getOpenFileName(self,"选取文件","","Text Files (*.txt)")
        if not filename:
            return
        raw = open(filename, 'rb').read()
        result = chardet.detect(raw)
        encoding = result['encoding']
        f = open(filename, "r+", encoding=encoding)
        content=''
        chunk_size = 1024
        while True:
            chunk_data = f.read(chunk_size)
            if not chunk_data:
                break
            nfo = self.fan.fanyi(chunk_data)
            nfo2 = self.fan.fanyi(nfo)
            content+=nfo2
        f.close()
        self.outcontent.setPlainText(content)
    @pyqtSlot()
    def on_savefile_clicked(self):
        filenames,save=QFileDialog.getSaveFileName(self,"文件另存为","","Text Files (*.txt)")
        if not filenames:
            return
        nfo2=self.outcontent.toPlainText()
        f2=open(filenames,"wb+")
        f2.write(nfo2.encode())
        f2.close()
    @pyqtSlot()
    def on_clicktxt_clicked(self):
        self.putcontent.clear()
        self.outcontent.clear()
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = main()
    win.show()
    sys.exit(app.exec_())