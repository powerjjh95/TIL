function myFunction() {
  
  // ■ [1] 경고창 띄우기
  // SpreadsheetApp.getUi().alert( "Hello, world~" );
  // const ui = SpreadsheetApp.getUi();
  // ui.alert( "안녕하세유~ 반가워유~" );
  
  // ■ [2] 사용자 정보 입력받기
  // SpreadsheetApp.getUi().prompt( "당신의 이름을 입력해주세요!" );
  // ui.prompt( "당신의 이름을 입력해주세요!" );

  // ■ [3] 스프레드시트 URL 정보 알아내기
  // const strUrl = SpreadsheetApp.getActiveSpreadsheet().getUrl();
  // ui.alert( strUrl );



  // ■ [4] 스프레드시트 파일내 시트가 총 몇 개인지 알아내기
  // const number = SpreadsheetApp.getActiveSpreadsheet().getNumSheets();
  // ui.alert( number );



  // ■ [5] 사용자 정보 입력 받아서 출력하기
  // const ui = SpreadsheetApp.getUi();
  // const res = ui.prompt( "당신의 이름을 입력해주세요!" );
  


  // ■ [6] 더미 샘플 데이터
  // const sheet = SpreadsheetApp.getActiveSheet();
  // const range = sheet.getRange( 3, 2 );



  // ■ [7] 지정된 범위의 값들
  // const sheet = SpreadsheetApp.getActiveSheet();
  // const range = sheet.getRange( "B2:D6" );



  // ■ [8] 시트 이름으로 원하는 시트 선택하기
  // const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName( "객체란?" );
  // const range = sheet.getRange( 2, 2 );




  // ■ [9] 특정 범위를 지정하여 한 줄만 or 여러 줄(지정한 수 만큼) 가져오기
  // const sheet = SpreadsheetApp.getActiveSheet();
  // const range = sheet.getRange( 2, 2, 2, 3 );



  // ■ [10] 아래와 같이 출력되도록 스크립트 코드를 작성해보시오?
  /*
    [
      [lee@ee.com, Pusan, 010-2222-2222], 
      [kang@kk.com, Jeju, 010-3333-3333], 
      [moon@m.com, Kwangju, 010-4444-4444], 
      [king@kk.com, Sejong, 010-5555-5555]
    ]
  */


  // ■ [11] 시트에 있는 회원 리스트에서 이메일만 모두 뽑아내는 코드를 작성해보시오?
  // 실습해보세요!



  // ■ [12] 아래 스크립트 코드를 실행했을 때 로그로 찍히는 값들을 말해보시오?
  // let sampleObj = {
  //   name: "Superman",
  //   nationality: "America",
  //   age: 20,
  //   hobby: "Reading"
  // }
  // const keys = Object.keys( sampleObj );
  


  // ■ [13] 아래와 같이 getValues() 메서드를 사용하여 배열로 반환받은 값을 for문으로 반복 출력하시오?
  // const values = SpreadsheetApp
  //                   .getActiveSpreadsheet()
  //                   .getActiveSheet()
  //                   .getRange( "B2:D6" )
  //                   .getValues()

  /*
    [
      [홍길동, hong, hong@hh.com], 
      [이순신, lee, lee@ee.com], 
      [강감찬, kang, kang@kk.com], 
      [을지문덕, moon, moon@m.com],
      [세종대왕, king, king@kk.com]
    ]  
  */

  // 1.
  // Logger.log( values.length );    // 5

  // 2. 
  // for ( let i=0; i < values.length; i++ ) 
  // {
  //   Logger.log( values[i] );
  // }

  // 3. 
  // for ( let i=values.length-1; i >= 0; i-- ) 
  // {
  //   Logger.log( values[i] );
  // }

  // 4. 
  // for ( let i=0; i < values.length; i++ ) 
  // {
  //   for ( let j=0; j < values[i].length; j++ ) 
  //   {
  //     Logger.log( values[i][j] );
  //   }
  // }

  // 5. 
  // for ( let i=0; i < values.length; i++ ) 
  // {
  //   Logger.log( values[i][2] );
  // }

  // 6. 
  // const ar1 = [ 'cat', 'dog', 'elephant', 'alligator', 'monkey' ];
  // const ar2 = [ 
  //   [ 'cat', 'dog', 'pig', 'cow' ], 
  //   [ 'computer', 'tv', 'radio' ], 
  //   [ 'abc', 'def', 'xyz' ]
  // ];

  // 맨 마지막번째 요소 출력하기
  // Logger.log( ar1[ar1.length-1] );   // monkey

  // 7. 
  // const ar3 = [ 
  //   'cat', 
  //   'dog', 
  //   'pig', 
  //   'cow' 
  // ];

  // 8.
  // Logger.log( ar3[0] ); 
  // Logger.log( ar3[1][0] ); 
  // Logger.log( ar3[2][1] ); 

  // 9.
  // for ( let i=ar3.length-1; i >= 0; i-- ) {
  //   Logger.log( ar3[i] );
  // }

  // 10.
  // const ar4 = [ 
  //   [ 'cat', 'dog', 'pig', 'cow' ], 
  //   [ 'computer', 'tv', 'radio' ], 
  //   [ 'abc', 'def', 'xyz' ]
  // ];

  // 11. 
  // Logger.log( ar4[1][0] );     
  // Logger.log( ar4[1][1] );     
  // Logger.log( ar4[1][2] );     

  // 12. 
  // Logger.log( ar4[0].length );      // 4
  // Logger.log( ar4[1].length );      // 3
  // Logger.log( ar4[2].length );      // 3

  // 13. 
  /*
  for ( let i=0; i < ar4.length; i++ ) 
  {
    Logger.log( ar4[i][1] );
  }
  */

  // 14. 
  /*
  for ( let i=0; i < ar4.length; i++ ) 
  {
    for ( let j=0; j < ar4[i].length; j++ ) 
    {
      Logger.log( ar4[i][j] );
    }
  }
  */

  // 15. 
  /*
  for ( let i=0; i < ar4.length; i++ ) 
  {
    for ( let j=1; j <= 2; j++ ) 
    {
      Logger.log( ar4[i][j] );  // dog, pig, tv, radio, def, xyz
    }
  }
  */



  // ■ [14] 아래 배열을 for .. in 반복문을 사용해서 출력하시오?
  // const nation = [ 
  //   'Korea', 
  //   'America', 
  //   'Canada', 
  //   'China', 
  //   'France'   
  // ];

  // 1.
  // for ( let i=0; i < nation.length; i++ ) 
  // {
  //   Logger.log( nation[i] );
  // }

  // 2. 
  /*
  for ( let idx in nation ) 
  {
    Logger.log( nation[idx] );
  }
  */

  // 3. 
  /*
  for ( let idx in nation.reverse() )
  {
    Logger.log( nation[idx] );
  }
  */

  /*
  const ar5 = [ 
    [ 'cat', 'dog', 'pig', 'cow' ], 
    [ 'computer', 'tv', 'radio' ], 
    [ 'abc', 'def', 'xyz' ]
  ];

  for ( let row in ar5 ) 
  {
    // Logger.log( row );
  }  

  for ( let row in ar5 ) 
  {
    for ( let col in ar5[row] ) 
    {
      Logger.log( ar5[row][col] );
    }
  }
  */



  // ■ [15] B2:D6 범위의 값들을 for .. in 이중 반복문을 사용해서 출력하시오?
  const values = SpreadsheetApp
                    .getActiveSpreadsheet()
                    // .getActiveSheet()
                    // .getSheets()[4]
                    .getSheetByName( "DummySample" )
                    .getRange( "B2:D6" )
                    .getValues()

  for ( let row in values )
  {
    for ( let col in values[row] ) 
    {
      Logger.log( values[row][col] );
    }
  }

}




