jQuery("#simulation")
  .on("click", ".s-66b89eb9-64b5-4558-81af-3814a2ed719b .click", function(event, data) {
    var jEvent, jFirer, cases;
    if(data === undefined) { data = event; }
    jEvent = jimEvent(event);
    jFirer = jEvent.getEventFirer();
    if(jFirer.is("#s-raised_Button")) {
      cases = [
        {
          "blocks": [
            {
              "actions": [
                {
                  "action": "jimChangeStyle",
                  "parameter": [ {
                    "#s-66b89eb9-64b5-4558-81af-3814a2ed719b #s-raised_Button > .backgroundLayer": {
                      "attributes": {
                        "background-color": "#3700B3",
                        "background-attachment": "scroll",
                        "box-shadow": "0px 5px 15px 0px #999999"
                      }
                    }
                  },{
                    "#s-66b89eb9-64b5-4558-81af-3814a2ed719b #s-raised_Button": {
                      "attributes": {
                        "text-shadow": "none"
                      }
                    }
                  },{
                    "#s-66b89eb9-64b5-4558-81af-3814a2ed719b #s-raised_Button": {
                      "attributes-ie": {
                        "-pie-background": "#3700B3",
                        "-pie-poll": "false"
                      }
                    }
                  } ],
                  "exectype": "serial",
                  "delay": 0
                },
                {
                  "action": "jimChangeStyle",
                  "parameter": [ {
                    "#s-66b89eb9-64b5-4558-81af-3814a2ed719b #s-raised_Button > .backgroundLayer": {
                      "attributes": {
                        "background-color": "#6200EE",
                        "background-attachment": "scroll",
                        "box-shadow": "0px 2px 5px 0px #999999"
                      }
                    }
                  },{
                    "#s-66b89eb9-64b5-4558-81af-3814a2ed719b #s-raised_Button": {
                      "attributes": {
                        "text-shadow": "none"
                      }
                    }
                  },{
                    "#s-66b89eb9-64b5-4558-81af-3814a2ed719b #s-raised_Button": {
                      "attributes-ie": {
                        "-pie-background": "#6200EE",
                        "-pie-poll": "false"
                      }
                    }
                  } ],
                  "exectype": "timed",
                  "delay": 200
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
    } else if(jFirer.is("#s-Image_72")) {
      cases = [
        {
          "blocks": [
            {
              "actions": [
                {
                  "action": "jimNavigation",
                  "parameter": {
                    "target": "screens/51ba10cb-2880-4613-8b44-4bc9695d40f1",
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
          "exectype": "serial",
          "delay": 0
        }
      ];
      event.data = data;
      jEvent.launchCases(cases);
    }
  });