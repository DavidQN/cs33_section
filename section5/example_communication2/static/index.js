$(document).ready(function() {
  // on click of submit button
  $("#submit").click(function() {
    var val = 1;
    var entry1 = 3;
    // push incoming data and expect a return response
    $.getJSON({
      url: "/getData",
      data: { entry2_id: val, entry1_id: entry1 },
      // what happens here is we wait for python to send back a response to the frontend
      success: function(data) {
        $("#varID").html(data.var1);
      }
    });
  });
});
