jQuery("#simulation")
  .on("click", ".s-ca32f58d-3a95-4c58-a746-d7136b1a77be .click", function(event, data) {
    var jEvent, jFirer, cases;
    if(data === undefined) { data = event; }
    jEvent = jimEvent(event);
    jFirer = jEvent.getEventFirer();
    if(jFirer.is("#s-Button_1")) {
      cases = [
        {
          "blocks": [
            {
              "actions": [
                {
                  "action": "jimCreateData",
                  "parameter": {
                    "datatype": "datamaster",
                    "datamaster": "Users",
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
                      "Date of Birth": {
                        "datatype": "property",
                        "target": "#s-Input_3",
                        "property": "jimGetValue"
                      },
                      "City": {
                        "datatype": "property",
                        "target": "#s-Input_4",
                        "property": "jimGetValue"
                      },
                      "Email": {
                        "datatype": "property",
                        "target": "#s-Input_5",
                        "property": "jimGetValue"
                      },
                      "Username": {
                        "datatype": "property",
                        "target": "#s-Input_6",
                        "property": "jimGetValue"
                      },
                      "Password": {
                        "datatype": "property",
                        "target": "#s-Input_7",
                        "property": "jimGetValue"
                      },
                      "Type": "0"
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
        }
      ];
      event.data = data;
      jEvent.launchCases(cases);
    }
  });