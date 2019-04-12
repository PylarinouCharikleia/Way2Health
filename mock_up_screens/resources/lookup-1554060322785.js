(function(window, undefined) {
  var dictionary = {
    "d197c59c-6480-474b-8bc2-41b7e1d5b3b4": "Patient1",
    "f73f9337-c1d0-4b8f-96de-427a95644a2b": "RegisterD",
    "23f3cb24-0738-4392-bb74-65d260d3026e": "Insert Data",
    "5a604c10-3118-4fb2-93f7-41d740a58663": "Calendar",
    "51ba10cb-2880-4613-8b44-4bc9695d40f1": "Body",
    "ca32f58d-3a95-4c58-a746-d7136b1a77be": "RegisterP",
    "adebe0ae-b919-480d-b74c-dd5ad31283a8": "Inbox",
    "0d2cf5fb-a2a7-44ca-a057-a17c74899101": "Login",
    "bd06a939-5ca1-4017-91d1-9c4b0afd5029": "Register",
    "25a34e7f-2df6-4906-8857-8d372b32e242": "doctor",
    "a6552769-d758-478a-987f-7e32409e877c": "Intro",
    "66b89eb9-64b5-4558-81af-3814a2ed719b": "Vital Signs",
    "c21f05d0-dbfd-4a8c-b045-ab5254718b14": "Body",
    "e73b655d-d3ec-4dcc-a55c-6e0293422bde": "960 grid - 16 columns",
    "ef07b413-721c-418e-81b1-33a7ed533245": "960 grid - 12 columns",
    "63bcad70-d063-45d4-b073-e8f86cbfb184": "Register",
    "f39803f7-df02-4169-93eb-7547fb8c961a": "Template 1",
    "6772aa48-ec25-48f1-8ac6-38f7b0491f80": "Extra Screen",
    "5080e751-d52b-45b2-adcd-c96c9cf19031": "Blue Font",
    "bb8abf58-f55e-472d-af05-a7d1bb0cc014": "default"
  };

  var uriRE = /^(\/#)?(screens|templates|masters|scenarios)\/(.*)(\.html)?/;
  window.lookUpURL = function(fragment) {
    var matches = uriRE.exec(fragment || "") || [],
        folder = matches[2] || "",
        canvas = matches[3] || "",
        name, url;
    if(dictionary.hasOwnProperty(canvas)) { /* search by name */
      url = folder + "/" + canvas;
    }
    return url;
  };

  window.lookUpName = function(fragment) {
    var matches = uriRE.exec(fragment || "") || [],
        folder = matches[2] || "",
        canvas = matches[3] || "",
        name, canvasName;
    if(dictionary.hasOwnProperty(canvas)) { /* search by name */
      canvasName = dictionary[canvas];
    }
    return canvasName;
  };
})(window);