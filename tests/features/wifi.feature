Feature: WiFi Feature Test Cases

  Scenario: WiFi Basic Connection Test
    Given Connect to wifi
    When Esp32 assigned ip
    Then Esp32 should resolve dns
    Then Esp32 disconnect wifi

     #connection with router

  Scenario: Connect to Hide Open WiFi Network
    Given Connect to open hide network
    Then Disconnect to open hide network

  Scenario: Connect to Open WiFi Network
    Given Connect to open network
    Then Disconnect to open network

  Scenario: Connect to Hide Secure Wifi Network
    Given Connect to secure hide network
    Then Disconnect to secure hide network

  Scenario: Connect to Secure Wifi Network
    Given Connect to secure network
    Then Disconnect to secure network

  Scenario: WiFi Connect 5Ghz Router
    Given Connect To WiFi Network


    #connection with hotspot

  Scenario: Connect to Hide Open WiFi Hotspot
    Given Connect to open hide hotspot
    Then Disconnect to open hide hotspot

  Scenario: Connect to Open WiFi Hotspot
    Given Connect to open hotspot
    Then Disconnect to open hotspot

  Scenario: Connect to Hide Secure Wifi Hotspot
    Given Connect to secure hide hotspot
    Then Disconnect to secure hide hotspot

  Scenario: Connect to Secure Wifi Hotspot
    Given Connect to secure hotspot
    Then Disconnect to secure hotspot

  Scenario:  WiFi Connect 5Ghz Hotspot
    Given Connect To WiFi hotspot


       #regression test condition

  Scenario: WiFi Connect with wrong Credentials
    Given Connect To WiFi Network with wrong ssid & Password

  Scenario: WiFi Connect with correct ssid and wrong password
    Given Connect To WiFi Network with wrong Password

#  Scenario:  WiFi Connect without wifi init
#    Given Connect To WiFi Network without wifi init

