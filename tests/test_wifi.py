import random
import time
from pathlib import Path
import pytest
from lib.services.wifi import Wifi
from conftest import jsonData
from pytest_bdd import scenario, scenarios, given, then, when

# Feature file directory path
featureFileDir = 'features'
featureFile = 'wifi.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)


# Scenarios
# Passing argument in wifi_connection fixture
@pytest.mark.parametrize('arg', [[jsonData()['ssid']['secure']['not_hide'], jsonData()['password']['pwd'], '1',
                                  jsonData()['response_operator']['wifi_connect']]])
@scenario(FEATURE_FILE, "WiFi Basic Connection Test")
# dut_connection fixture for serial connection
def test_zpr_20_1(dut_connection, wifi_connection):
    pass


# Given Steps
@given("Connect to wifi")
def wifi_cn(wifi_connection):
    wifi_connection


# When Steps
@when("Esp32 assigned ip")
def ip(dut_connection):
    time.sleep(15)
    command = Wifi.GetIp(jsonData()['response_operator']['ip'])
    response = dut_connection.send_receive(command)


# Then Steps
@then("Esp32 should resolve dns")
def dns(dut_connection):
    dns_lst = [jsonData()['dns']['url1'], jsonData()['dns']['url2'], jsonData()['dns']['url3']]
    dns = random.choice(dns_lst)
    command = Wifi.ResolveDns(dns, jsonData()['response_operator']['dns_res'])
    response = dut_connection.send_receive(command)


@then("Esp32 disconnect wifi")
def wifi_dc(wifi_disconnection):
    # Disconnecting
    wifi_disconnection


# Router Scenarios

# Scenarios
@pytest.mark.parametrize('arg', [[jsonData()['ssid']['open']['hide'], jsonData()['password']['open_pwd'], '0',
                                  jsonData()['response_operator']['wifi_connect']]])
@scenario(FEATURE_FILE, "Connect to Hide Open WiFi Network")
def test_zpr_20_2(wifi_connection):
    pass


# Given Steps
@given("Connect to open hide network")
def wifi_cn(wifi_connection):
    wifi_connection


# Then Steps
@then("Disconnect to open hide network")
def wifi_dc(wifi_disconnection):
    # Disconnecting
    wifi_disconnection


# Scenarios
@pytest.mark.parametrize('arg', [[jsonData()['ssid']['open']['not_hide'], jsonData()['password']['open_pwd'], '0',
                                  jsonData()['response_operator']['wifi_connect']]])
@scenario(FEATURE_FILE, "Connect to Open WiFi Network")
def test_zpr_20_3(wifi_connection):
    pass


# Given Steps
@given("Connect to open network")
def wifi_cn(wifi_connection):
    wifi_connection


# Then Steps
@then("Disconnect to open network")
def wifi_dc(wifi_disconnection):
    # Disconnecting ............
    wifi_disconnection


# Scenarios
@pytest.mark.parametrize('arg', [[jsonData()['ssid']['secure']['hide'], jsonData()['password']['pwd'], '1',
                                  jsonData()['response_operator']['wifi_connect']]])
@scenario(FEATURE_FILE, "Connect to Hide Secure Wifi Network")
def test_zpr_20_4(wifi_connection):
    pass


# Given Steps
@given("Connect to secure hide network")
def wifi_cn(wifi_connection):
    wifi_connection


# Then Steps
@then("Disconnect to secure hide network")
def wifi_dc(wifi_disconnection):
    # Disconnecting ............
    wifi_disconnection


# Scenarios
@pytest.mark.parametrize('arg', [[jsonData()['ssid']['secure']['not_hide'], jsonData()['password']['pwd'], '1',
                                  jsonData()['response_operator']['wifi_connect']]])
@scenario(FEATURE_FILE, "Connect to Secure Wifi Network")
def test_zpr_20_5(wifi_connection):
    pass


# Given Steps
@given("Connect to secure network")
def wifi_cn(wifi_connection):
    wifi_connection


# Then Steps
@then("Disconnect to secure network")
def wifi_dc(wifi_disconnection):
    # Disconnecting ............
    wifi_disconnection


# Scenarios
@pytest.mark.parametrize('arg', [
    [jsonData()['ssid']['secure']['5G'], jsonData()['password']['pwd'], '1', jsonData()['response_operator']['error']]])
@scenario(FEATURE_FILE, "WiFi Connect 5Ghz Router")
def test_zpr_20_6(wifi_connection):
    pass


@given("Connect To WiFi Network")
def wifi_cn_01(wifi_connection):
    wifi_connection


# Mobile Hostpot Scenarios


# Scenarios
@pytest.mark.parametrize('arg', [[jsonData()['ssid']['open']['hide'], jsonData()['password']['open_pwd'], '0',
                                  jsonData()['response_operator']['wifi_connect']]])
@scenario(FEATURE_FILE, "Connect to Hide Open WiFi Hotspot")
def test_zpr_20_7(wifi_connection):
    pass


# Given Steps
@given("Connect to open hide hotspot")
def wifi_cn(wifi_connection):
    wifi_connection


# Then Steps
@then("Disconnect to open hide hotspot")
def wifi_dc(wifi_disconnection):
    # Disconnecting
    wifi_disconnection


# Scenarios
@pytest.mark.parametrize('arg', [[jsonData()['ssid']['open']['not_hide'], jsonData()['password']['open_pwd'], '0',
                                  jsonData()['response_operator']['wifi_connect']]])
@scenario(FEATURE_FILE, "Connect to Open WiFi Hotspot")
def test_zpr_20_8(wifi_connection):
    pass


# Given Steps
@given("Connect to open hotspot")
def wifi_cn(wifi_connection):
    wifi_connection


# Then Steps
@then("Disconnect to open hotspot")
def wifi_dc(wifi_disconnection):
    # Disconnecting
    wifi_disconnection


# Scenarios
@pytest.mark.parametrize('arg', [[jsonData()['ssid']['secure']['hide'], jsonData()['password']['pwd'], '1',
                                  jsonData()['response_operator']['wifi_connect']]])
@scenario(FEATURE_FILE, "Connect to Hide Secure Wifi Hotspot")
def test_zpr_20_9(wifi_connection):
    pass


# Given Steps
@given("Connect to secure hide hotspot")
def wifi_cn(wifi_connection):
    wifi_connection


# Then Steps
@then("Disconnect to secure hide hotspot")
def wifi_dc(wifi_disconnection):
    # Disconnecting
    wifi_disconnection


# Scenarios
@pytest.mark.parametrize('arg', [[jsonData()['ssid']['secure']['not_hide'], jsonData()['password']['pwd'], '1',
                                  jsonData()['response_operator']['wifi_connect']]])
@scenario(FEATURE_FILE, "Connect to Secure Wifi Hotspot")
def test_zpr_20_10(wifi_connection):
    pass


# Given Steps
@given("Connect to secure hotspot")
def wifi_cn(wifi_connection):
    wifi_connection


# Then Steps
@then("Disconnect to secure hotspot")
def wifi_dc(wifi_disconnection):
    # Disconnecting
    wifi_disconnection


# Scenarios
@pytest.mark.parametrize('arg', [
    [jsonData()['ssid']['secure']['5G'], jsonData()['password']['pwd'], '1', jsonData()['response_operator']['error']]])
@scenario(FEATURE_FILE, "WiFi Connect 5Ghz Hotspot")
def test_zpr_20_11(wifi_connection):
    pass


# Given Steps
@given("Connect To WiFi hotspot")
def wifi_cn_01(wifi_connection):
    wifi_connection


# Scenarios
@pytest.mark.parametrize('arg', [[jsonData()['ssid']['secure']['not_hide'], jsonData()['password']['open_pwd'], '1',
                                  jsonData()['response_operator']['error']]])
@scenario(FEATURE_FILE, "WiFi Connect with wrong Credentials")
def test_zpr_20_12(wifi_connection):
    pass


# Given Steps
@given("Connect To WiFi Network with wrong ssid & Password")
def wifi_cn_wc_01(wifi_connection):
    wifi_connection


# Scenarios
@pytest.mark.parametrize('arg', [[jsonData()['ssid']['secure']['not_hide'], jsonData()['password']['open_pwd'], '1',
                                  jsonData()['response_operator']['error']]])
@scenario(FEATURE_FILE, "WiFi Connect with correct ssid and wrong password")
def test_zpr_20_13(wifi_connection):
    pass


# Given Steps
@given("Connect To WiFi Network with wrong Password")
def wifi_cn_wc1_01(wifi_connection):
    wifi_connection
