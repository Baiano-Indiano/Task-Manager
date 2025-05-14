from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from .models import Task

User = get_user_model()

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status']
        labels = {
            'title': _('Título'),
            'description': _('Descrição'),
            'status': _('Status'),
        }
        help_texts = {
            'title': _('Um título descritivo para a tarefa.'),
            'description': _('Detalhes adicionais sobre a tarefa.'),
            'status': _('Status atual da tarefa.'),
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Digite o título da tarefa'),
                'autofocus': True,
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': _('Descreva os detalhes da tarefa...'),
            }),
            'status': forms.Select(attrs={
                'class': 'form-select',
            }),
        }
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
    
    def clean_title(self):
        title = self.cleaned_data.get('title', '').strip()
        if len(title) < 3:
            raise ValidationError(_('O título deve ter pelo menos 3 caracteres.'))
        return title
    
    def clean_description(self):
        description = self.cleaned_data.get('description', '').strip()
        if len(description) > 1000:
            raise ValidationError(_('A descrição não pode ter mais de 1000 caracteres.'))
        return description
    
    def save(self, commit=True):
        task = super().save(commit=False)
        if self.user:
            task.user = self.user
        if commit:
            task.save()
        return task
