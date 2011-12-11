(function(window) { 
  var blog_id = "${pyrite_blog_id}";
  var bid = "ul." + blog_id;

  var pyrite = { 
    webload: function(divId) { 
      idhash = "#" + divId;
      compiled = pyrite_data["compiled_posts"];
      firstOrdered = pyrite_data["ordered_posts"]["0"];
      $(idhash).append("<ul class=\""+blog_id+"\"></ul>");
      $(bid).hide();
      for (var i = 0; i < firstOrdered.length; i++) {
        $(bid).append(compiled[firstOrdered[i]]);
      }
      $(bid).show();
    },

    createArchive: function() {
      // TODO 
    }
  };

  window.pyrite = pyrite;
})(window);
