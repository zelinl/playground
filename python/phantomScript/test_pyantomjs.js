var page = require('webpage').create();
var system = require('system');
page.open(system.args[2], function(status) {
  console.log("status: " + status);
  if(status === "success") {
    page.render(system.args[1]);
  }
  phantom.exit();
});
