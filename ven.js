const  inpfld = document.getElementById('inp');
const inputBtnHandle = document.getElementById('bbn');
requestAnimationFrame("dotenv").config();
const twit = require('./twit');

const fs = require('fs');
const path = require('path');
const ParamsPath = path.join(__dirname,'params.json');




let x = "https://twitter.com/cdtMaheshNitr/status/1540602657613656064?t=hXO1nhuIXhWNqa3vk1L_dQ&s=19"

function showdata(){
    let usrURL = inpfld.value;
    console.log(usrURL);
    if(usrURL===""){
        alert("give url");
        return;
    }
    
    const endpoint = new URL(usrURL);
    console.log(endpoint);
};

inputBtnHandle.addEventListener("click",showdata);

function writeParams(data){
console.log("We are writing this into  params file .. ",data);
return fs.writeFileSync(paramsPath,JSON.stringify(data));

}
function readParmas(){
    const data = fs.readFileSync(paramsPath);
    console.log("we are Reading params file  ... ",data.toString());
    return JSON.parse(data.toString());
}


function getTwieets(since_id){
  return new Promise((resolve,reject)=>{
    let params = {
        q:'#cricket',
        count:10,
    };
    if(since_id){
        params.since_id = since_id;
    }
    console.log("we are reading tweets ....",params);
    twit.get('search/tweets',params,(err,data)=>{
        if(err){
            return reject(err);
        }
        return resolve(data);
    });

  });
}

function postRetweet(){
return new Promise((resolve,reject)=>{
    let params ={
        id,
    }

    twit.post("status/retweet/:id",params,(err,data)=>{
        if(err) {
            return reject(err);
        }
        return resolve(data);
    });
});

}

async function main(){
 try{
    const params = readParmas();
    const data = await getTwieets(params.since_id);
    const tweets = data.statuses;
    console.log("we got tweets... N= ",tweets.length);

    for await ( let twt of tweets){
         try{
            await postRetweet(twt.id_str);
            console.log("S uccessFull post ... ",twt.id_str);
            
         }catch(e){
            console.log("UN uccessFull post ... ",twt.id_str);
         }
         params.since_id = twt.id_str;
    }

    writeParams(params);
 }catch(e){
    console.log(e);
 }
}


console.log("Starting a tiwter bot..");
setInterval(main,100000);


// curl --request GET 'https://api.twitter.com/2/tweets/search/recent?query=from:twitterdev' --header 'Authorization: Bearer $BEARER_TOKEN'
// curl --request GET "https://api.twitter.com/2/tweets/440322224407314432?expansions=author_id" --header "Authorization: Bearer AAAAAAAAAAAAAAAAAAAAAGUceQEAAAAA5FuS5M1y6E9wKN1UqdBe3dXhFYE%3DQkDtd4pKp26tlWbo2JUR3DRs8jv9fGGPEEf2lo9rlkWZsA38PM"