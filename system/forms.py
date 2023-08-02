from django import forms

class MeetForm(forms.Form):
    CHOICES = (
        ("公开", "公开"),
        ("内部", "内部"),
        ("秘密", "秘密"),
        ("机密", "机密"),

    )

    CHOICES1 = (
        ("0", "H.323"),
    )

    calllevel= forms.ChoiceField(label='呼叫密级',choices=CHOICES)
    phoneNo = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'IP/E164'}), required=True,label='呼叫号码')
    protocol = forms.ChoiceField(label='呼叫协议', choices=CHOICES1)

class MeetParameterForm(forms.Form):
    CHOICES = (
        ("自动加密", "自动加密"),
        ("强制加密", "强制加密"),
        ("不加密", "不加密"),

    )

    CHOICES1 = (
        ("0", "H.323"),
    )

    CHOICES2 = (
        ("AUTO", "AUTO"),
        ("G.711A", "G.711A"),
    )

    CHOICES3 = (
        ("AUTO", "AUTO"),
        ("H.264", "H.264"),
    )

    CHOICES4 = (
        ("AUTO", "AUTO"),
        ("1080P", "1080P"),
        ("720P", "720P"),
    )



    callencryption = forms.ChoiceField(label='呼叫加密',choices=CHOICES)
    calltype = forms.ChoiceField(label='通话类型', choices=CHOICES1)
    autoanswer = forms.CharField(widget=forms.TextInput(attrs={'type':'button'}))

    audioprotocol = forms.ChoiceField(label='音频协议',choices=CHOICES2)
    mainvprotocol = forms.ChoiceField(label='主流视频协议', choices=CHOICES3)
    mainvformat = forms.ChoiceField(label='主流视频格式', choices=CHOICES4)
    auxvprotocol = forms.ChoiceField(label='演示视频协议', choices=CHOICES3)
    auxvformat = forms.ChoiceField(label='演示视频格式', choices=CHOICES4)
    auxswitch = forms.CharField(widget=forms.TextInput(attrs={'type':'button'}))

class NetConfigForm(forms.Form):

    netswitch = forms.CharField(widget=forms.TextInput(attrs={'type':'button'}))
    adress = forms.CharField(widget=forms.TextInput, required=True, label='IPv4地址')
    mask = forms.CharField(widget=forms.TextInput, required=True, label='子网掩码')
    gateway = forms.CharField(widget=forms.TextInput, required=True, label='IPv4网关')
    GKswitch = forms.CharField(widget=forms.TextInput(attrs={'type': 'button','disabled':'disabled'}))
    GKadress = forms.CharField(widget=forms.TextInput(attrs={'disabled': 'disabled'}), required=True, label='GK地址')
    num = forms.CharField(widget=forms.TextInput(attrs={'disabled': 'disabled'}), required=True, label='注册号码')
    authname = forms.CharField(widget=forms.TextInput(attrs={'disabled': 'disabled'}), required=True, label='认证名称')
    authpw = forms.CharField(widget=forms.PasswordInput(attrs={'disabled': 'disabled'}), required=True, label='认证密码')

class UIdisplayForm(forms.Form):


    UIswitch = forms.CharField(widget=forms.TextInput(attrs={'type':'button'}))
    roomname = forms.CharField(widget=forms.TextInput, required=True, label='会场名')
    roomlevel = forms.CharField(widget=forms.TextInput(attrs={'disabled':'disabled'}), required=True, label='会场密级')

