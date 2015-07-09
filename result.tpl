<!DOCTYPE html>
<html>
  <head>
    <meta charset = "UTF-8" />
    <title>twitter result</title>
  </head>
  <body>
    <h1>tweetの結果</h1>
    % for i in html:
        <p>{{i[u'username']}}</p>
        <p>{{i[u'u_des']}}</p>
        <p>{{i[u'time']}}</p>
        <strong><p>{{i[u'text']}}</p></strong>
        
        <hr>
    % end
  </body>
</html>

