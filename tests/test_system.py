from lib.services.device import System

import random
import time
from pathlib import Path
import pytest
from lib.services.wifi import Wifi

from pytest_bdd import scenario, scenarios, given, then, when

featureFileDir = 'features'
featureFile = 'system.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)


# Checking the system Version

@scenario(FEATURE_FILE, "System Version Check")
def test_system_ver():
    pass


@given("Checking system version")
def system_ver(dut_connection, jsonData):
    command = System.Version()
    response = dut_connection.send_receive(command)


# Checking the system Uptime

@scenario(FEATURE_FILE, "System Uptime Check")
def test_system_uptime():
    pass


@given("Checking system uptime")
def system_uptime(dut_connection, jsonData):
    command = System.SysUptime()
    response = dut_connection.send_receive(command)
