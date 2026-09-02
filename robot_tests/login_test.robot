*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://the-internet.herokuapp.com/login
${BROWSER}    Chrome

*** Test Cases ***
Successful Login
    Open Browser    ${URL}    ${BROWSER}
    Input Text    id:username    tomsmith
    Input Text    id:password    SuperSecretPassword!
    Click Button    css:button[type='submit']
    Wait Until Element Is Visible    css:.flash.success    timeout=10s
    Element Should Contain    css:.flash.success    You logged into a secure area
    Close Browser
