var page = require('webpage').create();
page.open('https://www.ms88po.com/Main/Sports/mSports.aspx', function(status) {
  console.log("status: " + status);
  if(status === "success") {
    page.render('example.png');
  }
  phantom.exit();
});
