import json
import requests
class translate():
    def translate(self,word):
        # 有道词典 api
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
        # 传输的参数，其中 i 为需要翻译的内容
        key = {
            'type': "AUTO",
            'i': word,
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "ue": "UTF-8",
            "action": "FY_BY_CLICKBUTTON",
            "typoResult": "true"
        }
        # key 这个字典为发送给有道词典服务器的内容
        response = requests.post(url, data=key)
        # 判断服务器是否相应成功
        if response.status_code == 200:
            # 然后相应的结果
            return response.text
        else:
            print("有道词典调用失败")
            # 相应失败就返回空
            return None
    def get_reuslt(self,repsonse):
        # 通过 json.loads 把返回的结果加载成 json 格式
        result = json.loads(repsonse)
        info=''
        print(result)
        for i in result['translateResult']:
            for i2 in i:
                info+=str(i2['tgt'])
            info+='\n'
        return info
    def fanyi(self,word):
        list_trans = self.translate(str(word))
        jieguo=self.get_reuslt(list_trans)
        return jieguo
    if __name__ == '__main__':
        print()