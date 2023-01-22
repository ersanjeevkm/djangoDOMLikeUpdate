$(document).ready(function () {
  $("#like-button").click(function () {
    $.ajax({
      type: "POST",
      url: "/update_count/",
      data: { like: true },
      success: function (response) {
        $("#like-count").html(response.likes);
      },
    });
  });

  $("#dislike-button").click(function () {
    $.ajax({
      type: "POST",
      url: "/update_count/",
      data: { like: false },
      success: function (response) {
        $("#dislike-count").html(response.dislikes);
      },
    });
  });
});
