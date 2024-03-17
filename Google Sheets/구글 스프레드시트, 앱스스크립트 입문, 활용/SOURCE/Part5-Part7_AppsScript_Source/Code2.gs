/**
 * 메일 발송 스크립트 구현하기 예제8
 *    
 */
function myMailing8() {

  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = ss.getSheetByName( "DummySample" );
  const range = sheet.getRange( "A1:G6" );

  const filter = range.createFilter();
  
  const filterCondition = SpreadsheetApp.newFilterCriteria()
                                        .whenCellNotEmpty()
                                        .build();

  filter.setColumnFilterCriteria( 7, filterCondition );

  const newSheet = ss.insertSheet().setName( '수신자목록1' );
  const range1 = sheet.getDataRange();

  range1.copyTo(
    newSheet.getRange( 1, 1 )
  );

  filter.remove();  
}



/**
 * 메일 발송 스크립트 구현하기 예제7
 * 
 */
function myMailing7() {

  // [1] 같은 시트에서 특정 셀의 내용을 다른 셀에 복사하기
  // const ss = SpreadsheetApp.getActiveSpreadsheet();
  // const sheet = ss.getSheetByName( "메일내용1" );
  // const range = sheet.getRange( "A1" )
  // range.copyTo(
  //   sheet.getRange( "A2" ),
  //   SpreadsheetApp.CopyPasteType.PASTE_NORMAL
  // );

  // [2] 특정 셀의 내용을 다른 시트의 셀로 복사하기
  // const ss = SpreadsheetApp.getActiveSpreadsheet();
  // const originalSheet = ss.getSheetByName( "메일내용1" );
  // const data = originalSheet.getRange( "A1" );
  // const targetSheet = ss.getSheetByName( "DummySample" );
  // const targetCell = targetSheet.getRange( "A7" );
  // data.copyTo(
  //   targetCell,
  //   SpreadsheetApp.CopyPasteType.PASTE_NORMAL
  // );

  // [3] 이메일 리스트만 뽑아서 다른 시트의 마지막 열에 복사하기
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const originalSheet = ss.getSheetByName( "DummySample" );
  const data = originalSheet.getRange( "D2:D6" );
  const targetSheet = ss.getSheetByName( "회원메일링" ); 

  const targetRow = targetSheet.getLastRow();
  const targetColumn = targetSheet.getLastColumn();
  const targetCell = targetSheet.getRange( 1, targetColumn+1 );

  data.copyTo(
    targetCell,
    SpreadsheetApp.CopyPasteType.PASTE_NORMAL
  );

}



/**
 * 메일 발송 스크립트 구현하기 예제6
 * 
 */
function myMailing6() {

  const remainingDailyMailQuota = MailApp.getRemainingDailyQuota();
  Logger.log( "Remaining email quota : " + remainingDailyMailQuota );

  const ss = SpreadsheetApp.getActiveSpreadsheet();

  const sheet = ss.getSheets()[4];
  const lr = sheet.getLastRow();
  const lc = sheet.getLastColumn();

  const range = sheet.getRange( 2, 1, lr-1, lc-1 );

  const values = range.getValues();

  const mailSubject       = "예제6번 테스트 메일입니다.";
  const mailBody          = ss.getSheetByName( "메일내용1" ).getRange( "A1" ).getValue();
  const mailSignature     = "홍보영업부 과장 홍 길 동 배상";

  // 반복문 돌면서 메일 발송
  let cnt = 0;
  for ( let i=0; i < values.length; i++ ) 
  {
    if ( values[i][6] === 0 ) {
      Logger.log( values[i][2] );
    }
    else {
      MailApp.sendEmail( {
        to: values[i][3],
        subject: mailSubject,
        body: mailBody + mailSignature
      } );
      Logger.log( `${ values[i][3] } ~~~> 메일 발송 완료` );
      cnt += 1;
    }
  }
  Logger.log( `${ cnt } 통의 메일을 발송했습니다.` );
}



/**
 * 메일 발송 스크립트 구현하기 예제5
 * 
 */
function myMailing5() {

  const remainingDailyMailQuota = MailApp.getRemainingDailyQuota();
  Logger.log( "Remaining email quota : " + remainingDailyMailQuota );

  const ss = SpreadsheetApp.getActiveSpreadsheet();

  const sheet = ss.getSheets()[4];
  const lr = sheet.getLastRow();

  const range = sheet.getRange( 2, 1, lr-1, 6 );

  const values = range.getValues();

  const mailSubject       = "테스트 메일입니다.";
  const mailBody          = ss.getSheetByName( "메일내용1" ).getRange( "A1" ).getValue();
  const mailSignature     = "홍보영업부 과장 홍 길 동 배상";

  // 반복문 돌면서 메일 발송
  let cnt = 0;
  for ( let i=0; i < values.length; i++ )
  {
    MailApp.sendEmail(
      values[i][3],
      mailSubject,
      mailBody + mailSignature
    );
    Logger.log( `${ values[i][3] } ~~~> 메일 발송 완료` );
    cnt += 1;
  }
  Logger.log( `${ cnt }통의 메일을 발송했습니다.` );
}



/**
 * 메일 발송 스크립트 구현하기 예제4
 * 
 */
function myMailing4() {

  const remainingDailyMailQuota = MailApp.getRemainingDailyQuota();
  Logger.log( "Remaining email quota : " + remainingDailyMailQuota );

  const ss = SpreadsheetApp.getActiveSpreadsheet();

  const sheet = ss.getSheets()[4];

  const range = sheet.getRange( "D2:D6" );
  const emails = range.getValues();

  Logger.log( emails.length );  // 5

  if ( remainingDailyMailQuota >= emails.length ) {
    for ( let i=0; i < emails.length; i++ ) 
    {
      MailApp.sendEmail(
        emails[i][0],
        "제목입니다.",
        "본문이에요~~~~~~~~~~~~~~~~~~"
      );
    }
  }  
  else {
    Logger.log( '하루 메일 발송 쿼터가 부족합니다.' );
  }
}



/**
 * 메일 발송 스크립트 구현하기 예제3 - for 반복문 돌면서 메일 발송
 * 
 */
function myMailing3() {

  const signature = "홍보영업부 과장 홍 길 동 배상";

  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = ss.getSheetByName( "DummySample" );

  const range = sheet.getRange( "D2:D6" );

  const emails = range.getValues();

  for ( let i=0; i < emails.length; i++ ) 
  {
    MailApp.sendEmail(
      emails[i][0],
      "반복문 사용해서 메일 발송합니다.",
      `
        안녕하세요~
        앱스스크립트 프로그래밍으로 메일 발송 테스트중입니다.
        많은 응원 부탁드립니다.

        ${ signature }
      `
    );
  }
}



/**
 * 메일 발송 스크립트 구현하기 예제2 - 백틱과 변수 사용
 * 
 */
function myMailing2() {

  const mailAddress   = "kaplan1notion@gmail.com";
  const subject       = "테스트 메일 발송입니다.";
  const signature     = "홍보영업부 과장 홍 길 동 배상";

  MailApp.sendEmail(
    mailAddress,
    subject,
    `
      안녕하세요~
      앱스스크립트 프로그래밍으로 메일 발송 테스트중입니다.
      많은 응원 부탁드립니다.

      ${ signature }
    `
  );
  Logger.log( `${ mailAddress } ~~~> 메일 발송 완료` );
}



/**
 * 메일 발송 스크립트 구현하기 예제1 - 기본적인 sendEmail() 메서드 사용법
 * 
 */
function myMailing1() {

  const emails = SpreadsheetApp
                    .getActiveSpreadsheet()
                    .getSheets()[4]
                    .getRange( "D2:D6" )
                    .getValues()

  MailApp.sendEmail(
    "kaplan1notion@gmail.com",
    "테스트 메일 발송입니다.",
    "안녕하세요~\n앱스스크립트 프로그래밍으로 메일 발송 테스트중입니다.\n개행처리해서 멜 보냅니다."
  );
}










