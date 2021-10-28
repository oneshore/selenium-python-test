from behave import *

@given('I have "{amount:d}" dollars in my account')
def create_account(context, amount):
	context.account = amount

@given('The ATM fee is "{atm_fee:d}" dollars')
def set_atm_fee(context, atm_fee):
	context.atm_fee = atm_fee

@when('I withdraw "{withdrawl:d}" dollars via ATM')
def atm_withdrawl(context, withdrawl):
	context.account -= withdrawl
	context.account -= context.atm_fee

@when(u'I withdraw "{withdrawl:d}" dollars at the bank')
def bank_withdrawl(context, withdrawl):
	context.account -= withdrawl

@then('I should have "{amount:d}" dollars in my account')
def account_verification(context, amount):
	assert context.account == amount
