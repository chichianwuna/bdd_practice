from behave import *
from page_objects.page_objects import Campaigns

use_step_matcher('parse')

@given(u'I am on the payment page')
def step_impl(context):
    context.driver = Campaigns()
    context.driver.launch_page()


@when(u'I select payment currency')
def step_impl(context):
    context.driver = Campaigns()
    context.driver.select_payment_currency()


@when(u'I select or type in payment amount')
def step_impl(context):
    context.driver = Campaigns()
    context.driver.make_paypal_payment()

@when(u'click on the PayPal submit button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When click on the PayPal submit button')


@then(u'I should be redirected to the Paypal portal')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should be redirected to the Paypal portal')
