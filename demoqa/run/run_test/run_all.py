from demoqa.tests.test_alerts import *

@pytest.mark.smoke
def test_show_alert_box(page: Page, show_alert_box):
    show_alert_box()

@pytest.mark.smoke
def test_show_confirm_box(page: Page, show_confirm_box):
    show_confirm_box()