from django import forms
import hashlib
import configparser

class NameForm(forms.Form):
    usrname = forms.CharField(widget=forms.TextInput(attrs={'class':'single_line'}), required=True, label='用户名')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'single_line'}), required=True, label='密码')

    def clean(self):
        username=self.cleaned_data['usrname']
        password=self.cleaned_data['password']
        m = password + "{{sdtzzq}}"
        pw = hashlib.md5(m.encode())
        config = configparser.ConfigParser()
        config.read("conf/admin.ini",encoding='utf-8-sig')
        try:
            name = config.get(username, "name")
            psw = config.get(username, "pw")
            if (name == username)&(psw == pw.hexdigest()):
                pass
            else:
                 raise forms.ValidationError(u"用户名或密码错误，请重新输入")
        except:
            raise forms.ValidationError(u"用户名或密码错误，请重新输入")
        return self.cleaned_data