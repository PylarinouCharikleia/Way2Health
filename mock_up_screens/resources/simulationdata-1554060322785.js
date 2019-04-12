function initData() {
  jimData.variables["typeofuserlogin"] = "";
  jimData.variables["typeofuserregister"] = "";
  jimData.datamasters["doctors"] = [
    {
      "id": 1,
      "datamaster": "doctors",
      "userdata": {
        "Name": "sample text",
        "Surname": "sample text",
        "Specialty": "sample text",
        "Telephone": "sample text",
        "Email": "sample text",
        "City": "sample text",
        "Username": "roger",
        "Password": "password",
        "Type": "1"
      }
    },
    {
      "id": 2,
      "datamaster": "doctors",
      "userdata": {
        "Name": "sample text",
        "Surname": "sample text",
        "Specialty": "sample text",
        "Telephone": "sample text",
        "Email": "sample text",
        "City": "sample text",
        "Username": "mike",
        "Password": "password",
        "Type": "1"
      }
    }
  ];

  jimData.datamasters["Users"] = [
    {
      "id": 1,
      "datamaster": "Users",
      "userdata": {
        "Name": "sample text",
        "Surname": "sample text",
        "Date of Birth": "",
        "City": "sample text",
        "Email": "sample text",
        "Username": "mary",
        "Password": "password",
        "Type": "0"
      }
    }
  ];

  jimData.isInitialized = true;
}