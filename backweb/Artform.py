
from django import forms
from backweb.models import MyUser


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=10, min_length=5, required=True,
                                error_messages={
                                    'required': '用户名必填',
                                    'max_length': '用户名长度不能超过10',
                                    'min_length': '用户名长度不能少于5',
                                })
    userpwd = forms.CharField(max_length=18, min_length=6, required=True,
                          error_messages={
                              'required': '密码必填',
                              'max_length': '密码长度不能超过18',
                              'min_length': '密码长度不能少于6',
                          })

    def clean(self):
        username = self.cleaned_data.get('username')
        user = MyUser.objects.filter(username=username).first()
        if not user:
            raise forms.ValidationError({'username': '账号没有注册，请先注册'})
        return self.cleaned_data


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=10, min_length=5,
                                required=True, error_messages={
                                    'required': '用户名必填',
                                    'max_length': '用户名不能超过20字符',
                                    'min_length': '用户名不能少于5字符'
                                })
    password = forms.CharField(max_length=18, min_length=6,
                          required=True, error_messages={
                            'required': '密码必填',
                            'max_length': '用户密码不能超过20字符',
                            'min_length': '用户密码不能少于5字符'
                            })
    password2 = forms.CharField(max_length=18, min_length=6,
                           required=True, error_messages={
                            'required': '密码必填',
                            'max_length': '用户密码不能超过20字符',
                            'min_length': '用户密码不能少于5字符'
                            })

    def clean(self):
        username = self.cleaned_data.get('username')
        user = MyUser.objects.filter(username=username).first()
        if user:

            raise forms.ValidationError({'username': '该用户已注册，请登录'})
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError({'password': '两次密码不一致'})
        return self.cleaned_data


class AddArtForm(forms.Form):
    title = forms.CharField(min_length=5, required=True,
                            error_messages={
                                'required': '文章标题不能为空哦',
                                'min_length': '文章标题不能少于5个字符'
                            })
    describe = forms.CharField(min_length=20, required=True,
                               error_messages={
                                    'required': '文章简短描述必须填哦',
                                    'min_length': '文章简短描述不能少于20字符'
                               })
    content = forms.CharField(required=True,
                              error_messages={
                                  'required': '文章内容必须填哦'
                              })
    icon = forms.ImageField(required=True, error_messages={
        'required': '首图必填'
    })


class UpArtForm(forms.Form):
    title = forms.CharField(min_length=5, required=True,
                            error_messages={
                                'required': '文章标题必须填哦',
                                'min_length': '文章标题不能少于5个字符'
                            })
    describe = forms.CharField(min_length=20, required=True,
                               error_messages={
                                    'required': '文章简短描述必须填哦',
                                    'min_length': '文章简短描述不能少于20字符'
                               })
    content = forms.CharField(required=True,
                              error_messages={
                                  'required': '文章内容必须填哦'
                              })
    icon = forms.ImageField(required=False)