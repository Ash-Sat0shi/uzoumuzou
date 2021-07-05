const SSID1 = "18t5koWgdYM6CVU2AgXKD857Oyh8pz2oS39b6j2Sxzh8";
const SSID2 = "1r4ZPxCBgoMdl1wB8ydLmxFnH-nGjLblmjCAr_3xLDEw";


function doGet(e) {
let html = HtmlService
  .createTemplateFromFile('チーム編成表')
  .evaluate()
  .setTitle('テスト　チーム編成表')
  .setSandboxMode(HtmlService.SandboxMode.IFRAME)
  .addMetaTag('viewport', 'width=device-width, initial-scale=1')
  return html;
}


function include(filename) {
  return HtmlService.createHtmlOutputFromFile(filename).getContent();
}

function getSheetNameList(){
  //こっち廃止、getListに移植し、Vue内でプルダウン作成する
  let sheet = SpreadsheetApp.openById(SSID2).getSheets();
  let sheetname = [];
  for(let i =0; i<sheet.length; i++){
    sheetname.push(sheet[i].getSheetName());
  }
  Logger.log(sheetname);
  //Logger.log(sheet.map(sheet => sheet.getName()));
  return sheetname;
}

function getList(){
  let spreadSheet = SpreadsheetApp.openById(SSID1);
  let sheet1 = spreadSheet.getSheetByName("プレイヤー名簿");
  let lastrow = sheet1.getLastRow();

  let playerdatalsit = [];

  let range = sheet1.getRange(2,2,lastrow-1,4);
  let info = range.getValues();
  //console.log(info);
  
  //後でこういう感じで情報取り出せる
  for(let i=0; i <info.length; i++){
    let udata = {id:i, name:info[i][0], team:"X", uid:info[i][3], kill:"", damage:"", points:""};
    playerdatalsit.push(udata);
  }
  console.log(playerdatalsit);

  let sheet2 = SpreadsheetApp.openById(SSID2).getSheets();
  let sheetnamelist = [];
  for(let j=0; j<sheet2.length; j++){
    let sheetdata = {id:j, sname:sheet2[j].getSheetName()};
    sheetnamelist.push(sheetdata);
    //sheetnamelist.push(sheet2[j].getSheetName());
  }
  Logger.log(sheetnamelist);


  return [playerdatalsit,sheetnamelist];
};

function createSS(newssname){
  let date = new Date();
  let day = Utilities.formatDate( date, 'Asia/Tokyo', 'MM月dd日')
  let ssname = newssname;
  let ss = SpreadsheetApp.openById(SSID2);
  let templatess = ss.getSheetByName("テンプレ_変更しないで");
  templatess.copyTo(ss).setName(day + ssname);
  ss.setActiveSheet(ss.getSheetByName(day + ssname));
  ss.moveActiveSheet(1);

  let url = ScriptApp.getService().getUrl();
  return url;
};

function appendSS(editedsheetname, data){
  let ss = SpreadsheetApp.openById(SSID2);
  let sheet = ss.getSheetByName(editedsheetname);
  let lastrow = sheet.getLastRow()+1;
  //dataはJSONで受け取られ、すでにparseしてある。data[i]で任意のプレイヤーの情報を抜き取り
  for(let k=0; k<data.length; k++){
    sheet.getRange(lastrow + k,1).setValue(data[k].team);
    sheet.getRange(lastrow + k,2).setValue(data[k].name);
    sheet.getRange(lastrow + k,3).setValue(data[k].uid);
    sheet.getRange(lastrow + k,4).setValue(data[k].kill);
    sheet.getRange(lastrow + k,5).setValue(data[k].damage);
    sheet.getRange(lastrow + k,6).setValue(data[k].points);
  }
  let str = JSON.stringify(data);
  
  //sheet.getRange(lastrow,5).setValue("このファイル開きました…");

  return [editedsheetname, data, str];
};
