$(function(){

    var cursor=$("#cursor");                // カーソルになる要素を指定
    $(document).on("mousemove",function(e){ // マウスカーソルが動いた時に実行
      var x=e.clientX;                      // カーソルの横座標を取得
      var y=e.clientY;                      // カーソルの縦座標を取得
  
      //  取得した座標をCSSに反映させる
      cursor.css({
        "top":y+"px",
        "left":x+"px"
      });
    });
  
  });