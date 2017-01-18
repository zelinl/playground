// Read the Phantom webpage '.version' element text using jQuery and "includeJs"

"use strict";
var page = require('webpage').create();

page.onConsoleMessage = function(msg) {
    console.log(msg);
};

page.open("https://www.ms88po.com/Main/Sports/mSports/sports.aspx", function(status) {
    if (status === "success") {
        page.includeJs("http://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js", function() {
            page.evaluate(function() {
                // lastest version on the web
                console.log("$(\"span.oddsNotEmpty\").text() -> " + $("span.oddsNotEmpty").text());
            });
            phantom.exit(0);
        });
    } else {
      phantom.exit(1);
    }
});
