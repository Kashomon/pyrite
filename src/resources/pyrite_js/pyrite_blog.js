(function(winow) { 
  var blog_id = "${pyrite_blog_id}";
  var bid = "#" + blog_id;

  var pyrite = { 
    webload : function(divId) { 
      idhash = "#" + divId;
      compiled = pyrite_data["compiled_posts"];
      firstOrdered = pyrite_data["ordered_posts"]["0"];
      $(idhash).append("<div id=\""+blog_id+
          "\"></div>");
      $(bid).hide();
      for (var i = 0; i < firstOrdered.length; i++) {
        $(bid).append(compiled[firstOrdered[i]]);
      }
      $(bid).show();
    }
  };

  window.pyrite = pyrite;
})(window);
