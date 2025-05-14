from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

User = get_user_model()

class Task(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pendente'),
        ('C', 'Concluída'),
    ]
    
    title = models.CharField('título', max_length=255)
    description = models.TextField('descrição', blank=True)
    status = models.CharField(
        'situação', 
        max_length=1, 
        choices=STATUS_CHOICES, 
        default='P',
        help_text='Status atual da tarefa'
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        verbose_name='usuário',
        related_name='tasks',
        null=True,  # Adicionando null=True temporariamente
        blank=True  # Adicionando blank=True temporariamente
    )
    created_at = models.DateTimeField('criado em', auto_now_add=True, null=True)  # Adicionando null=True temporariamente
    updated_at = models.DateTimeField('atualizado em', auto_now=True, null=True)  # Adicionando null=True temporariamente
    
    class Meta:
        verbose_name = 'tarefa'
        verbose_name_plural = 'tarefas'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('tasks:task_list')
    
    def toggle_status(self):
        """Alterna o status da tarefa entre Pendente e Concluída"""
        self.status = 'C' if self.status == 'P' else 'P'
        self.save(update_fields=['status', 'updated_at'])
        return self.status
    
    @property
    def is_completed(self):
        """Retorna True se a tarefa estiver concluída"""
        return self.status == 'C'
    
    @property
    def status_badge_class(self):
        """Retorna a classe CSS para o badge de status"""
        return 'bg-success' if self.status == 'C' else 'bg-warning text-dark'
    
    @property
    def status_icon(self):
        """Retorna o ícone do Bootstrap Icons para o status"""
        return 'bi-check-circle-fill' if self.status == 'C' else 'bi-hourglass-split'
