from alerts.tests.test_alerts import *



@pytest.mark.smoke
def test_show_alert_box(page: Page, show_alert_box):
    show_alert_box()

@pytest.mark.smoke
def test_confirm_alert_box_accept(page: Page, show_confirm_box_accept):
    show_confirm_box_accept()

@pytest.mark.smoke
def test_confirm_alert_box_dismiss(page: Page, show_confirm_box_dismiss):
    show_confirm_box_dismiss()

@pytest.mark.smoke
def test_prompt_alert_box(page: Page, show_prompt_box):
    show_prompt_box()