from django.db import models

class RegisterProcurement(models.Model):
    'Реестр закупок'

class BasisStatement(models.Model):
    'Основание позиции ведомости'
    
class PurchaseStatement(models.Model):
    'Закупочная ведомость'

class PositionStatement(models.Model):
    'Позиция ведомости'

class ProcurementStatement(models.Model):
    'Позиция ведомости в заявке'

class StatusTimeline(models.Model):
    'Статусы узла закупок'

class TimelineProcurement(models.Model):
    'Чеклст процесса закупки'

