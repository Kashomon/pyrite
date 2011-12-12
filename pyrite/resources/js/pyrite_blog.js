(function(window) { 
  var blogId = "#" + "${pyrite_blog_id}";
  var archiveId = "#" + "${archive_bar}";
  var archiveLink = "${archive_link}";

  var pyrite = { 
    webload: function(divId) { 
      idhash = "#" + divId;
      compiled = pyrite_data["compiled_posts"];
      firstOrdered = pyrite_data["ordered_posts"]["0"];
      $(idhash).append(pyrite_data["blog_holder"]);
      $(blogId).hide();
      for (var i = 0; i < firstOrdered.length; i++) {
        $(blogId).append(compiled[firstOrdered[i]]);
      }
      // pyrite.createArchive(archiveId);

      $(blogId).show();
    },

    createArchive: function(hashId) {
      var year, month;
      for (year in pyrite_data["dates"]) {
        $(hashId).append(pyrite.archLink(year));
        for (month in pyrite_data["dates"][year]) {
          $(hashId).append(pyrite.archLink(month));    
        }
      }
    },

    archLink: function(content) {
      return pyrite.createContainer("li", archiveLink, content);
    },

    createDiv: function(divClass, content) { 
      return pyrite.createContainer("div", divClass, content);
    },

    createContainer: function(typez, clazz, content) {
      return "<"+typez+ " class=\""+clazz+"\">"+content+"</"+typez+">";
    }
  };

  window.pyrite = pyrite;
})(window);
