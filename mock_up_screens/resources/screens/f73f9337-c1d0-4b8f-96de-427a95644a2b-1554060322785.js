jQuery("#simulation")
  .on("click", ".s-f73f9337-c1d0-4b8f-96de-427a95644a2b .click", function(event, data) {
    var jEvent, jFirer, cases;
    if(data === undefined) { data = event; }
    jEvent = jimEvent(event);
    jFirer = jEvent.getEventFirer();
    if(jFirer.is("#s-Finish")) {
      cases = [
        {
          "blocks": [
            {
              "actions": [
                {
                  "action": "jimCreateData",
                  "parameter": {
                    "datatype": "datamaster",
                    "datamaster": "doctors",
                    "fields": {
                      "Name": {
                        "datatype": "property",
                        "target": "#s-Input_1",
                        "property": "jimGetValue"
                      },
                      "Surname": {
                        "datatype": "property",
                        "target": "#s-Input_2",
                        "property": "jimGetValue"
                      },
                      "Specialty": {
                        "datatype": "property",
                        "target": "#s-Input_3",
                        "property": "jimGetValue"
                      },
                      "Telephone": {
                        "datatype": "property",
                        "target": "#s-Input_4",
                        "property": "jimGetValue"
                      },
                      "Email": {
                        "datatype": "property",
                        "target": "#s-Input_5",
                        "property": "jimGetValue"
                      },
                      "City": {
                        "datatype": "property",
                        "target": "#s-Input_6",
                        "property": "jimGetValue"
                      },
                      "Username": {
                        "datatype": "property",
                        "target": "#s-Input_7",
                        "property": "jimGetValue"
                      },
                      "Password": {
                        "datatype": "property",
                        "target": "#s-Input_8",
                        "property": "jimGetValue"
                      },
                      "Type": "1"
                    }
                  },
                  "exectype": "serial",
                  "delay": 0
                }
              ]
            }
          ],
          "exectype": "serial",
          "delay": 0
        },
        {
          "blocks": [
            {
              "actions": [
                {
                  "action": "jimNavigation",
                  "parameter": {
                    "target": "screens/0d2cf5fb-a2a7-44ca-a057-a17c74899101",
                    "transition": {
                      "type": "fade",
                      "duration": 500
                    }
                  },
                  "exectype": "serial",
                  "delay": 0
                }
              ]
            }
          ],
          "exectype": "timed",
          "delay": 500
        }
      ];
      event.data = data;
      jEvent.launchCases(cases);
    }
  });