#*** Settings ***
#Library     SeleniumLibrary
#Library     ScreenCapLibrary
#
#Test Setup  Start Video Recording
#Test Teardown   Stop Video Recording
#
#*** Test Cases ***
#Search On Google
#    Start Video Recording
#    Open Browser    http://www.google.com      Chrome
#    Wait Until Page Contains Element    cnsw
#    Select Frame   //iframe
#    Submit Form    //form
#    Input Text      name=q Stephen\ Hawking
#    Press Keys      name=q ENTER
#    Stop Video Recording
#    Page Should Contain     Wikipedia
#    Close Window

#Example of setting for headless browser

*** Settings ***
Library     SeleniumLibrary
Library     ScreenCapLibrary
Test Setup    Start Video Recording
Test Teardown    Stop Video Recording
Suite Teardown    Close All Browsers

*** Variables ***
${BROWSER}  headlesschrome
${NOTHEADLESS}=    "headlesschrome" not in "${BROWSER}"

*** Test Cases ***
Search On Google
     Open Browser   http://www.google.com   ${BROWSER}
     Run Keyword If    ${NOTHEADLESS}    Wait Until Page Contains Element   cnsw
     Run Keyword If    ${NOTHEADLESS}    Select Frame   //iframe
     Run Keyword If    ${NOTHEADLESS}    Submit Form      //form
     Unselect Frame
     Input Text     name=q   Stephen\ Hawking
     Press Keys     name=q   SPACE
     Press Keys     name=q   ENTER
     Wait Until Page Contains Element   id=res
     Page Should Contain   Wikipedia
     Close Window
