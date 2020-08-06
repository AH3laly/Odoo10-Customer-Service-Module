# Author: Abdelrahman Helaly
# Contact: < AH3laly@gmail.com , https://Github.com/AH3laly >
# Project: Odoo 10 Customer Service. 
# Description: Odoo 10 Customer Service Module.
# License: Science not for Monopoly.

# -*- coding: utf-8 -*-

from odoo import models, fields, api

class customer(models.Model):
    _name = 'cs.customer'
    name =fields. Char(required=True,help='Customer name')
    address = fields.Char(help='Customer address')
    religion = fields.Selection([('muslim',"Muslim"),('christian',"Christian"),('other',"Other"),])
    gender =  fields.Selection([('male',"Male"),('female',"Female"),])
    company = fields.Char(help='Customer company')
    job_title = fields.Char(help='Customer job title ex: Sales manager, Marketting  agent, etc..')
    phones = fields.Many2one('cs.customer.phone')
    emails = fields.Many2one('cs.customer.email')
    marital_status =  fields.Selection([('married',"Married"),('engaged',"Engaged"),('divorced',"Divorced"),('widowed',"Widowed"),])
    birth_date = fields.Date()
    notes = fields. Char(help='Any notes related to customer')


class team(models.Model):
    _name = 'cs.team'
    name =fields. Char(required=True,help='Employee name')
    job_title = fields.Char(help='Employee job title ex: Sales manager, Marketting  agent, etc..')
    

class customer_phone(models.Model):
    _name = 'cs.customer.phone'
    customer_id = fields.Many2one('cs.customer',index=True)
    phone = fields.Char(required=True)
    title = fields.Char()


class customer_email(models.Model):
    _name = 'cs.customer.email'
    customer_id = fields.Many2one('cs.customer',index=True)
    email = fields.Char(required=True)
    title = fields.Char()


class task(models.Model):
    _name = 'cs.task'
    name = fields.Char()
    customer_id = fields.Many2one('cs.customer')
    importance = fields.Selection([('urgent',"Urgent"),('high',"High"),('medium',"Medium"),('low',"Low"),])
    deadline = fields.Date()
    is_done = fields.Boolean()
    is_approved = fields.Boolean()
    is_closed = fields.Boolean()
    assigned_to = fields.Many2one('cs.team')
    assigned_by = fields.Many2one('cs.team')
    issue_id = fields.Integer()
    

class issue(models.Model):
    _name = 'cs.issue'
    name = fields.Char()
    customer_id = fields.Many2one('cs.customer')
    importance = fields.Selection([('urgent',"Urgent"),('high',"High"),('medium',"Medium"),('low',"Low"),])
    is_done = fields.Boolean()
    is_approved = fields.Boolean()
    is_closed = fields.Boolean()
    assigned_to = fields.Many2one('cs.team')
    assigned_by = fields.Many2one('cs.team')
    next_action_date = fields.Date()
    next_action_type = fields.Selection([('call',"Call"),('visit',"Visit"),('in_meeting',"In Company Meeting"),])
    direction = fields.Selection([('in',"Inbound"),('out',"Outbound"),])




