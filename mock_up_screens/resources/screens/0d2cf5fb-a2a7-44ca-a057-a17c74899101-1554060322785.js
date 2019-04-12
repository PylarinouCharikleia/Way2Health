jQuery("#simulation")
  .on("click", ".s-0d2cf5fb-a2a7-44ca-a057-a17c74899101 .click", function(event, data) {
    var jEvent, jFirer, cases;
    if(data === undefined) { data = event; }
    jEvent = jimEvent(event);
    jFirer = jEvent.getEventFirer();
    if(jFirer.is("#s-checkpat")) {
      cases = [
        {
          "blocks": [
            {
              "actions": [
                {
                  "action": "jimSetValue",
                  "parameter": {
                    "variable": [ "typeofuserlogin" ],
                    "value": "0"
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
    } else if(jFirer.is("#s-checkdoct")) {
      cases = [
        {
          "blocks": [
            {
              "actions": [
                {
                  "action": "jimSetValue",
                  "parameter": {
                    "variable": [ "typeofuserlogin" ],
                    "value": "1"
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
    } else if(jFirer.is("#s-Button_1")) {
      cases = [
        {
          "blocks": [
            {
              "condition": {
                "action": "jimEquals",
                "parameter": [ {
                  "action": "jimCount",
                  "parameter": [ {
                    "action": "jimFilterData",
                    "parameter": {
                      "datatype": "datamaster",
                      "datamaster": "Users",
                      "value": {
                        "action": "jimAnd",
                        "parameter": [ {
                          "action": "jimEquals",
                          "parameter": [ {
                            "field": "Username"
                          },{
                            "datatype": "property",
                            "target": "#s-Inpuser",
                            "property": "jimGetValue"
                          } ]
                        },{
                          "action": "jimAnd",
                          "parameter": [ {
                            "action": "jimEquals",
                            "parameter": [ {
                              "field": "Password"
                            },{
                              "datatype": "property",
                              "target": "#s-Inppass",
                              "property": "jimGetValue"
                            } ]
                          },{
                            "action": "jimEquals",
                            "parameter": [ {
                              "field": "Type"
                            },{
                              "datatype": "variable",
                              "element": "typeofuserlogin"
                            } ]
                          } ]
                        } ]
                      }
                    }
                  } ]
                },"1" ]
              },
              "actions": [
                {
                  "action": "jimNavigation",
                  "parameter": {
                    "target": "screens/51ba10cb-2880-4613-8b44-4bc9695d40f1"
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
              "condition": {
                "action": "jimEquals",
                "parameter": [ {
                  "action": "jimCount",
                  "parameter": [ {
                    "action": "jimFilterData",
                    "parameter": {
                      "datatype": "datamaster",
                      "datamaster": "doctors",
                      "value": {
                        "action": "jimAnd",
                        "parameter": [ {
                          "action": "jimEquals",
                          "parameter": [ {
                            "field": "Username"
                          },{
                            "datatype": "property",
                            "target": "#s-Inpuser",
                            "property": "jimGetValue"
                          } ]
                        },{
                          "action": "jimAnd",
                          "parameter": [ {
                            "action": "jimEquals",
                            "parameter": [ {
                              "field": "Password"
                            },{
                              "datatype": "property",
                              "target": "#s-Inppass",
                              "property": "jimGetValue"
                            } ]
                          },{
                            "action": "jimEquals",
                            "parameter": [ {
                              "field": "Type"
                            },{
                              "datatype": "variable",
                              "element": "typeofuserlogin"
                            } ]
                          } ]
                        } ]
                      }
                    }
                  } ]
                },"1" ]
              },
              "actions": [
                {
                  "action": "jimNavigation",
                  "parameter": {
                    "target": "screens/25a34e7f-2df6-4906-8857-8d372b32e242"
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
    } else if(jFirer.is("#s-Button_2")) {
      cases = [
        {
          "blocks": [
            {
              "actions": [
                {
                  "action": "jimNavigation",
                  "parameter": {
                    "target": "screens/bd06a939-5ca1-4017-91d1-9c4b0afd5029",
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