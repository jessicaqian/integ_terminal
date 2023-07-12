from django import forms

class MeetcontrolForm(forms.Form):
    CHOICES = (
        ("1", "1M"),
        ("2", "2M"),
        ("4", "4M"),
        ("8", "8M"),
    )

    CHOICES1 = (
        ("video", "视频呼叫"),
        ("audio", "音频呼叫")
    )

    CHOICES2 = (
        ("0", "H.323"),
        ("1", "SIP")
    )

    bandwidth = forms.ChoiceField(label='呼叫带宽',choices=CHOICES)
    phoneNo = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'IP/E164'}), required=True,label='呼叫号码')
    calltype = forms.ChoiceField(label='呼叫类型',choices=CHOICES1)
    protocol = forms.ChoiceField(label='呼叫协议', choices=CHOICES2)

