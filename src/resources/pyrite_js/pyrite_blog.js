(function(window) { 
  var pyrite = { 
    webload : function(divId) { 
      compiled = pyrite_data["compiled_posts"];
      firstOrdered = pyrite_data["ordered_posts"]["0"];
      for (var i = 0; i < firstOrdered.length; i++) {
        $("#" + divId).append(compiled[firstOrdered[i]]);
      }
    }
  };

  window.pyrite = pyrite;
})(window);
