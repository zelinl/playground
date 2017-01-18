var page = require('webpage').create();
var system = require('system');
if (system.args.length === 1) {
  console.log('请指定输出图片和url。')
  phantom.exit(1);
}
console.log('默认的user agent是： ' + page.settings.userAgent);
page.settings.userAgent = '微而科技agent';
page.open('http://www.httpuseragent.org', function(status) {
  if (status !== 'success') {
    console.log('Unable to access network');
  } else {
    console.log('开始执行：');
    var ua = page.evaluate(function(){
      return document.getElementById('myagent').textContent;
    });
    console.log(ua);
  }
  page.render(system.args[1]);
  phantom.exit();
})
