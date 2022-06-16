function custom() {
  console.log("Claim");
  var sign = prompt("Enter your Hive username")



  if (sign === "") {
    alert("Insert your Hive username!");
   

  } else if (sign) {
    console.log("run the code");
    this.user = sign.toLowerCase();
    async function getdata() {
      let response =  await fetch(
        "https://spk.tcmd-spkcc.com/@"+this.user
      );
      let data = await response.json();
      let drop = data.drop;
      let valor = drop.last_claim;
      return valor;
    }

    getdata()
    .then(valor => {

      console.log(valor);
      let value = valor;
      let fecha =  new Date()
      let mes = fecha.getMonth();
      let elmes = mes + 1 

      console.log(elmes);

      if (value < mes) {
        console.log("true");
        let custom = '{"larynx":true}'
    let id = 'spkcc_claim'
    if(window.hive_keychain) {
        hive_keychain.requestBroadcast(
          this.user,
          [
            [
              "custom_json",
              {
                required_auths: [
                  this.user
                ],
                required_posting_auths: [],
                id: "spkcc_claim",
                json: "{\"larynx\":true}",
              },
            ],
          ],
       
          "Active", function (response) {
          if (response.success) {

            link = response.result.id;
  
            alert("Claimed successfully!" + "Tx ID: " +  link);
            
          } else {
  
            alert(response.error);
  
  
          }
        }, 
        );
    } else {
        alert("You need to install HIVE Keychain first!");
    }

      } else {
        console.log("false");
        alert("You have already claimed your tokens for this month.");
      }


      });





  
    




  } else {
    alert("Operation cancelled");
  }

}

  
  
  




